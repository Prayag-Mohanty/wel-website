"""End-to-end exercise of the new admin editing + live-update mechanism."""
import os, sys, tempfile, shutil

os.environ['ADMIN_EMAIL'] = 'admin@iitb.ac.in'
os.environ['ADMIN_PASSWORD'] = 'test-pass-123'
os.environ['SECRET_KEY'] = 'test-key'

tmp = tempfile.mkdtemp()
os.environ['DATABASE_URL'] = 'sqlite:///' + os.path.join(tmp, 'test.db').replace(os.sep, '/')
sys.path.insert(0, os.path.abspath('.'))

import app as A

with A.app.app_context():
    assert str(A.db.engine.url).endswith('test.db'), 'not isolated: ' + str(A.db.engine.url)
A.app.config['TESTING'] = True


with A.app.app_context():
    A.db.drop_all()
    A.init_db()


def ok(label, cond, extra=''):
    print(('  PASS  ' if cond else '  FAIL  ') + label +
          (('   -> ' + str(extra)) if (extra != '' and not cond) else ''))
    if not cond:
        ok.bad += 1


ok.bad = 0

c = A.app.test_client()

r = c.post('/admin/login', data={'email': 'admin@iitb.ac.in', 'password': 'test-pass-123'},
           follow_redirects=True)
ok('admin can log in', b'Dashboard' in r.data or b'Admin' in r.data, r.status_code)


def rev():
    return c.get('/api/version').get_json()['rev']


print('\n-- creating and editing components --')
r0 = rev()
c.post('/admin/component/new', data={
    'component_type': 'Op-amp', 'model_no': 'LM358N', 'description': 'Dual op-amp, DIP-8',
    'link': 'https://example.com/lm358', 'location': 'Rack B, drawer 4', 'quantity': '25'},
    follow_redirects=True)
with A.app.app_context():
    comp = A.Component.query.filter_by(model_no='LM358N').first()
ok('create component', comp is not None and comp.quantity == 25)
ok('  sr_no auto-assigned', comp and comp.sr_no == 1, comp.sr_no if comp else None)
ok('  create bumps revision', rev() > r0)
cid = comp.id

r1 = rev()
c.post('/admin/component/new', data={'component_type': 'Nothing', 'quantity': '5'},
       follow_redirects=True)
with A.app.app_context():
    n = A.Component.query.count()
ok('blank component rejected', n == 1, n)
ok('  rejection does not bump revision', rev() == r1)

c.post('/admin/component/%d/edit' % cid, data={
    'sr_no': '7', 'component_type': 'Op-amp (precision)', 'model_no': 'OP07CP',
    'description': 'Precision op-amp', 'link': '', 'location': 'Rack C', 'quantity': '4'},
    follow_redirects=True)
with A.app.app_context():
    comp = A.db.session.get(A.Component, cid)
    ok('edit changes every field, not just qty',
       comp.model_no == 'OP07CP' and comp.location == 'Rack C' and comp.sr_no == 7
       and comp.component_type == 'Op-amp (precision)' and comp.quantity == 4,
       (comp.model_no, comp.location, comp.sr_no, comp.quantity))

print('\n-- student request and live approval --')
s = A.app.test_client()
s.post('/register', data={
    'team_name': 'Team Alpha', 'email': 'stu@iitb.ac.in',
    'password': 'stud-pass-123', 'confirm': 'stud-pass-123',
    'member_name': 'Asha', 'member_reg': '24M1001'}, follow_redirects=True)
with A.app.app_context():
    u = A.User.query.filter_by(email='stu@iitb.ac.in').first()
ok('student can register', u is not None)

req = None
if u:
    s.post('/login', data={'email': 'stu@iitb.ac.in', 'password': 'stud-pass-123'},
           follow_redirects=True)
    r = s.get('/inventory')
    ok('student sees the component', b'OP07CP' in r.data)
    s.post('/cart/add/%d' % cid, data={'quantity': '2'}, follow_redirects=True)
    r2 = rev()
    s.post('/request', data={'notes': 'For EDL project'}, follow_redirects=True)
    with A.app.app_context():
        req = A.ComponentRequest.query.first()
    ok('request created', req is not None and req.status == 'pending')
    ok('  new request bumps revision (admin sees it live)', rev() > r2)
    ok('  pending count exposed by /api/version',
       c.get('/api/version').get_json()['pending'] == 1)

print('\n-- fragments used by the live refresh --')
f = c.get('/admin/requests/fragment?status=pending')
ok('admin request fragment renders', f.status_code == 200 and b'Team Alpha' in f.data, f.status_code)
ok('  it is a partial, not a whole page', b'<html' not in f.data.lower())
f = c.get('/admin/inventory/fragment?show=active')
ok('admin inventory fragment renders', f.status_code == 200 and b'OP07CP' in f.data)
f = s.get('/my-requests/fragment')
ok('student fragment renders', f.status_code == 200 and b'PENDING' in f.data)
f = c.get('/admin/dashboard/fragment')
ok('dashboard fragment renders', f.status_code == 200 and b'Pending Requests' in f.data)

if req:
    r3 = rev()
    c.post('/admin/request/%d/approve' % req.id, follow_redirects=True)
    with A.app.app_context():
        req2 = A.db.session.get(A.ComponentRequest, req.id)
        comp = A.db.session.get(A.Component, cid)
    ok('approve marks the request approved', req2.status == 'approved')
    ok('  stock deducted 4 -> 2', comp.quantity == 2, comp.quantity)
    ok('  approve bumps revision (student sees it live)', rev() > r3)
    f = s.get('/my-requests/fragment')
    ok('  student fragment now reads APPROVED', b'APPROVED' in f.data)

print('\n-- archive and delete --')
c.post('/admin/component/%d/archive' % cid, follow_redirects=True)
with A.app.app_context():
    comp = A.db.session.get(A.Component, cid)
ok('archive sets the flag', comp.archived is True)
ok('  archived part hidden from students', b'OP07CP' not in s.get('/inventory').data)
ok('  hidden from admin active view',
   b'OP07CP' not in c.get('/admin/inventory/fragment?show=active').data)
ok('  still visible in admin archived view',
   b'OP07CP' in c.get('/admin/inventory/fragment?show=archived').data)

c.post('/admin/component/%d/delete' % cid, follow_redirects=True)
with A.app.app_context():
    still = A.db.session.get(A.Component, cid)
ok('delete REFUSED while named on a request (history stays intact)', still is not None)

c.post('/admin/component/new', data={'model_no': 'TYPO-XYZ', 'quantity': '1'}, follow_redirects=True)
with A.app.app_context():
    junk = A.Component.query.filter_by(model_no='TYPO-XYZ').first()
c.post('/admin/component/%d/archive' % junk.id, follow_redirects=True)
c.post('/admin/component/%d/delete' % junk.id, follow_redirects=True)
with A.app.app_context():
    gone = A.Component.query.filter_by(model_no='TYPO-XYZ').first()
ok('delete allowed when the part was never requested', gone is None)

c.post('/admin/component/%d/archive' % cid, follow_redirects=True)
with A.app.app_context():
    comp = A.db.session.get(A.Component, cid)
ok('archive toggles back / restores', comp.archived is False)

print('\n-- authorisation --')
anon = A.app.test_client()
for url in ('/admin/component/new', '/admin/component/%d/edit' % cid,
            '/admin/component/%d/archive' % cid, '/admin/component/%d/delete' % cid):
    ok('anonymous blocked from POST %s' % url,
       anon.post(url).status_code in (302, 401, 403))
for url in ('/admin/inventory/fragment', '/admin/requests/fragment', '/admin/dashboard/fragment'):
    ok('anonymous blocked from %s' % url, anon.get(url).status_code in (302, 401, 403))
ok('anonymous blocked from /api/version', anon.get('/api/version').status_code in (302, 401, 403))

r = s.post('/admin/component/new', data={'model_no': 'HACK'}, follow_redirects=False)
ok('logged-in STUDENT blocked from admin create', r.status_code in (302, 401, 403), r.status_code)
with A.app.app_context():
    ok('  and it had no effect',
       A.Component.query.filter_by(model_no='HACK').first() is None)
ok('logged-in STUDENT blocked from admin fragment',
   s.get('/admin/inventory/fragment').status_code in (302, 401, 403))

print('\n-- cookie hardening --')
ok('SameSite=Lax set', A.app.config['SESSION_COOKIE_SAMESITE'] == 'Lax')
ok('HttpOnly set', A.app.config['SESSION_COOKIE_HTTPONLY'] is True)

print('\nFAILURES: %d' % ok.bad)
shutil.rmtree(tmp, ignore_errors=True)
sys.exit(1 if ok.bad else 0)
