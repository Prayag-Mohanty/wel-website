"""Hit every page as admin and as student and check none of them 500."""
import os, sys, tempfile, shutil

os.environ['ADMIN_EMAIL'] = 'admin@iitb.ac.in'
os.environ['ADMIN_PASSWORD'] = 'test-pass-123'
os.environ['SECRET_KEY'] = 'test-key'
tmp = tempfile.mkdtemp()
os.environ['DATABASE_URL'] = 'sqlite:///' + os.path.join(tmp, 'smoke.db').replace(os.sep, '/')
sys.path.insert(0, os.path.abspath('.'))

import app as A

with A.app.app_context():
    assert str(A.db.engine.url).endswith('smoke.db')
    A.init_db()

bad = 0
c = A.app.test_client()
c.post('/admin/login', data={'email': 'admin@iitb.ac.in', 'password': 'test-pass-123'},
       follow_redirects=True)
c.post('/admin/component/new', data={
    'component_type': 'IC', 'model_no': 'NE555', 'description': 'Timer',
    'location': 'Bin 3', 'quantity': '20'}, follow_redirects=True)

s = A.app.test_client()
s.post('/register', data={'team_name': 'Smoke', 'email': 'smoke@iitb.ac.in',
                          'password': 'smoke-pass-1', 'confirm': 'smoke-pass-1',
                          'member_name': 'Ann', 'member_reg': '24M9'},
       follow_redirects=True)
s.post('/cart/add/1', data={'quantity': '1'}, follow_redirects=True)
s.post('/request', data={'notes': 'x'}, follow_redirects=True)

ADMIN = ['/admin', '/admin/requests', '/admin/requests?status=approved',
         '/admin/requests?status=rejected', '/admin/inventory',
         '/admin/inventory?show=archived', '/admin/teams', '/admin/upload',
         '/admin/dashboard/fragment', '/admin/requests/fragment',
         '/admin/inventory/fragment', '/api/version']
STUDENT = ['/', '/inventory', '/inventory?q=NE555', '/inventory?type=IC',
           '/request', '/my-requests', '/my-requests/fragment', '/api/version']
ANON = ['/', '/login', '/register', '/admin/login']

print('ADMIN')
for u in ADMIN:
    r = c.get(u)
    okk = r.status_code in (200, 302)
    print(('  %-3d  ' % r.status_code) + u + ('' if okk else '   <-- FAIL'))
    if not okk:
        bad += 1

print('STUDENT')
for u in STUDENT:
    r = s.get(u)
    okk = r.status_code in (200, 302)
    print(('  %-3d  ' % r.status_code) + u + ('' if okk else '   <-- FAIL'))
    if not okk:
        bad += 1

print('ANONYMOUS')
anon = A.app.test_client()
for u in ANON:
    r = anon.get(u)
    okk = r.status_code in (200, 302)
    print(('  %-3d  ' % r.status_code) + u + ('' if okk else '   <-- FAIL'))
    if not okk:
        bad += 1

print('\nFAILURES: %d' % bad)
shutil.rmtree(tmp, ignore_errors=True)
sys.exit(1 if bad else 0)
