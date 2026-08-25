"""Simulate an OLD database (no `archived` column, no `revision` table) and
check that starting the new code upgrades it in place without losing data."""
import os, sys, sqlite3, tempfile, shutil

os.environ['ADMIN_EMAIL'] = 'admin@iitb.ac.in'
os.environ['ADMIN_PASSWORD'] = 'test-pass-123'
os.environ['SECRET_KEY'] = 'test-key'
sys.path.insert(0, os.path.abspath('.'))

tmp = tempfile.mkdtemp()
dbp = os.path.join(tmp, 'old.db')
os.environ['DATABASE_URL'] = 'sqlite:///' + dbp.replace(os.sep, '/')

# ---- build a database exactly as the ORIGINAL app.py would have -----------
con = sqlite3.connect(dbp)
con.executescript("""
CREATE TABLE team (id INTEGER PRIMARY KEY, name VARCHAR(120) UNIQUE NOT NULL,
                   members_json TEXT);
CREATE TABLE user (id INTEGER PRIMARY KEY, email VARCHAR(120) UNIQUE NOT NULL,
                   password_hash VARCHAR(256) NOT NULL, team_id INTEGER,
                   is_admin BOOLEAN, created_at DATETIME);
CREATE TABLE component (id INTEGER PRIMARY KEY, sr_no INTEGER,
                        component_type VARCHAR(100), model_no VARCHAR(100),
                        description TEXT, link VARCHAR(500),
                        location VARCHAR(200), quantity INTEGER);
CREATE TABLE component_request (id INTEGER PRIMARY KEY, team_id INTEGER NOT NULL,
                        status VARCHAR(20), notes TEXT,
                        created_at DATETIME, updated_at DATETIME);
CREATE TABLE request_item (id INTEGER PRIMARY KEY, request_id INTEGER NOT NULL,
                        component_id INTEGER NOT NULL, quantity INTEGER NOT NULL);
INSERT INTO component (sr_no, component_type, model_no, description, link,
                       location, quantity)
VALUES (1,'Sensor','MPU6050','6-axis IMU','','Rack A',12),
       (2,'IC','LM7805','5V regulator','','Rack A',40),
       (3,'Board','Arduino Uno','ATmega328P board','','Cupboard 2',7);
INSERT INTO team (name, members_json) VALUES ('Legacy Team','[]');
INSERT INTO component_request (team_id, status, notes, created_at, updated_at)
VALUES (1,'approved','old request','2025-01-01','2025-01-02');
INSERT INTO request_item (request_id, component_id, quantity) VALUES (1, 1, 3);
""")
con.commit()

before = con.execute('SELECT id, model_no, quantity FROM component ORDER BY id').fetchall()
cols_before = [r[1] for r in con.execute('PRAGMA table_info(component)')]
con.close()

print('BEFORE upgrade')
print('  component columns :', cols_before)
print('  rows              :', before)
assert 'archived' not in cols_before

# ---- now start the NEW code against that same file -----------------------
import app as A
with A.app.app_context():
    assert str(A.db.engine.url).endswith('old.db'), 'not isolated: ' + str(A.db.engine.url)
A.app.config['TESTING'] = True

with A.app.app_context():
    A.init_db()          # this is what wsgi.py / app.py run at start-up

con = sqlite3.connect(dbp)
cols_after = [r[1] for r in con.execute('PRAGMA table_info(component)')]
after = con.execute('SELECT id, model_no, quantity FROM component ORDER BY id').fetchall()
tables = sorted(r[0] for r in con.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"))
archived_vals = [r[0] for r in con.execute('SELECT archived FROM component ORDER BY id')]
items = con.execute('SELECT request_id, component_id, quantity FROM request_item').fetchall()
con.close()

print('\nAFTER upgrade')
print('  component columns :', cols_after)
print('  rows              :', after)
print('  archived defaults :', archived_vals)
print('  tables            :', tables)
print('  request history   :', items)

bad = 0


def ok(label, cond):
    global bad
    print(('  PASS  ' if cond else '  FAIL  ') + label)
    if not cond:
        bad += 1


print('\nCHECKS')
ok('archived column added', 'archived' in cols_after)
ok('revision table created', 'revision' in tables)
ok('every existing row survived, quantities intact', before == after)
ok('existing rows default to not-archived', all(v == 0 for v in archived_vals))
ok('past request history untouched', items == [(1, 1, 3)])

# and the upgraded database is actually usable
c = A.app.test_client()
c.post('/admin/login', data={'email': 'admin@iitb.ac.in', 'password': 'test-pass-123'},
       follow_redirects=True)
r = c.get('/admin/inventory/fragment?show=active')
ok('admin inventory renders on the upgraded database',
   r.status_code == 200 and b'MPU6050' in r.data and b'Arduino Uno' in r.data)
ok('/api/version works', c.get('/api/version').status_code == 200)

# running init_db a second time must be harmless (every restart calls it)
with A.app.app_context():
    A.init_db()
con = sqlite3.connect(dbp)
n = con.execute('SELECT COUNT(*) FROM component').fetchone()[0]
ncols = len([r[1] for r in con.execute('PRAGMA table_info(component)')])
con.close()
ok('second start-up is a no-op (idempotent)', n == 3 and ncols == len(cols_after))

print('\nFAILURES: %d' % bad)
shutil.rmtree(tmp, ignore_errors=True)
sys.exit(1 if bad else 0)
