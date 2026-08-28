"""Run pythonanywhere_wsgi.py the way PythonAnywhere runs it.

PythonAnywhere executes that file from a working directory that is NOT the
project folder, with none of the project's environment variables set, and
reaches the code only through sys.path. That is exactly the situation a Flask
app that works locally tends to fall over in, so reproduce it rather than
assume: cwd elsewhere, environment stripped, .env found by absolute path.

The file under test is the real `pythonanywhere_wsgi.py` that ships in this
folder, with only the PROJECT line pointed here - so if that file is wrong,
this fails.

    python tests/test_pythonanywhere_wsgi.py
"""
import http.cookiejar
import os
import shutil
import sqlite3
import sys
import tempfile
import threading
import urllib.error
import urllib.parse
import urllib.request

PROJECT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
WSGI_FILE = os.path.join(PROJECT, 'pythonanywhere_wsgi.py')

HOME = tempfile.mkdtemp()
os.chdir(HOME)                      # cwd is NOT the project, as on PythonAnywhere

for k in ('SECRET_KEY', 'ADMIN_EMAIL', 'ADMIN_PASSWORD', 'DATABASE_URL', 'COOKIE_SECURE'):
    os.environ.pop(k, None)         # prove .env is doing the work, not the shell

DB = os.path.join(HOME, 'pa.db').replace(os.sep, '/')
ENV_PATH = os.path.join(PROJECT, '.env')
env_existed = os.path.exists(ENV_PATH)
env_backup = ENV_PATH + '.testbackup'
if env_existed:
    shutil.copy2(ENV_PATH, env_backup)

with open(ENV_PATH, 'w') as f:
    f.write('SECRET_KEY=pa-secret-from-dotenv\n'
            'ADMIN_EMAIL=lab@iitb.ac.in\n'
            'ADMIN_PASSWORD=pa-pass-12345\n'
            'COOKIE_SECURE=1\n'
            'DATABASE_URL=sqlite:///%s\n' % DB)

bad = 0


def ok(label, cond, extra=''):
    global bad
    print(('  PASS  ' if cond else '  FAIL  ') + label +
          (('   -> ' + str(extra)) if (extra != '' and not cond) else ''))
    if not cond:
        bad += 1


def cleanup():
    if env_existed:
        shutil.move(env_backup, ENV_PATH)
    elif os.path.exists(ENV_PATH):
        os.remove(ENV_PATH)
    shutil.rmtree(HOME, ignore_errors=True)


try:
    # -- execute the shipped WSGI file, with only PROJECT repointed ---------
    src = open(WSGI_FILE).read()
    assert "PROJECT = '/home/USERNAME/wel-website/inventory-app'" in src, \
        'the PROJECT placeholder line in pythonanywhere_wsgi.py has changed'
    src = src.replace("PROJECT = '/home/USERNAME/wel-website/inventory-app'",
                      'PROJECT = %r' % PROJECT)
    ns = {'__name__': 'pa_wsgi', '__file__': WSGI_FILE}
    exec(compile(src, WSGI_FILE, 'exec'), ns)
    application = ns['application']

    print('WSGI file')
    ok('the shipped file executes with cwd outside the project', True)
    ok('it exposes an `application` callable', callable(application))
    ok('.env found by absolute path, not via cwd',
       os.environ.get('SECRET_KEY') == 'pa-secret-from-dotenv',
       os.environ.get('SECRET_KEY'))

    import app as A
    ok('the secret key reached the app',
       A.app.secret_key == 'pa-secret-from-dotenv', A.app.secret_key)
    ok('COOKIE_SECURE from .env was applied',
       A.app.config['SESSION_COOKIE_SECURE'] is True)

    # That setting marks the session cookie Secure, so it is not sent back over
    # plain http - which is precisely its job, and which wsgiref below is. Turn
    # it off for the HTTP drive; PythonAnywhere serves HTTPS, so it stays on
    # there. (Getting this wrong is worth knowing about: set COOKIE_SECURE=1
    # on a host without HTTPS and nobody can log in.)
    A.app.config['SESSION_COOKIE_SECURE'] = False
    with A.app.app_context():
        ok('DATABASE_URL honoured', str(A.db.engine.url).endswith('pa.db'),
           str(A.db.engine.url))
    ok('database created at import time', os.path.exists(DB))
    with A.app.app_context():
        ok('admin account seeded from .env',
           A.User.query.filter_by(email='lab@iitb.ac.in').first() is not None)
        ok('revision row present, so live updates work',
           A.db.session.get(A.Revision, 1) is not None)

    # -- serve it for real and drive it over HTTP ---------------------------
    from wsgiref.simple_server import WSGIRequestHandler, make_server

    class Quiet(WSGIRequestHandler):
        def log_message(self, *a):
            pass

    httpd = make_server('127.0.0.1', 0, application, handler_class=Quiet)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = 'http://127.0.0.1:%d' % httpd.server_address[1]
    print('\nServed over real HTTP on %s' % base)

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    def req(u, data=None):
        body = urllib.parse.urlencode(data).encode() if data else None
        try:
            r = opener.open(base + u, body, timeout=15)
            return r.getcode(), r.read()
        except urllib.error.HTTPError as e:
            return e.code, e.read()

    ok('landing page served', req('/')[0] == 200)
    ok('admin login page served', req('/admin/login')[0] == 200)
    code, body = req('/admin/login', {'email': 'lab@iitb.ac.in',
                                      'password': 'pa-pass-12345'})
    ok('admin can log in over HTTP', code == 200 and b'Dashboard' in body, code)
    code, body = req('/admin/component/new', {
        'component_type': 'IC', 'model_no': 'NE555', 'description': 'Timer',
        'location': 'Bin 3', 'quantity': '12'})
    ok('component added over HTTP', code == 200 and b'NE555' in body, code)
    code, body = req('/api/version')
    ok('live-update endpoint responds', code == 200 and b'"rev"' in body, code)
    code, body = req('/admin/inventory')
    ok('inventory page lists it', code == 200 and b'NE555' in body, code)
    code, body = req('/static/js/live.js')
    ok('static files served', code == 200 and b'data-live-url' in body, code)
    ok('unknown path is a clean 404, not a crash', req('/no-such-page')[0] == 404)

    httpd.shutdown()

    n = sqlite3.connect(DB).execute(
        "SELECT COUNT(*) FROM component WHERE model_no='NE555'").fetchone()[0]
    ok('data is on disk, so it survives a reload', n == 1, n)

finally:
    cleanup()

print('\nFAILURES: %d' % bad)
sys.exit(1 if bad else 0)
