# Tests

Plain Python, no test framework to install. Run them from `inventory-app/`:

```bash
python tests/test_admin_and_live.py
python tests/test_upgrade_existing_db.py
python tests/test_all_pages_render.py
python tests/test_pythonanywhere_wsgi.py
```

Each one prints a PASS/FAIL line per check and exits non-zero if anything
failed.

They each build their own throwaway database in a temp directory via
`DATABASE_URL`, and assert that they did before touching anything — so running
them can never write to `instance/inventory.db`.

- **test_admin_and_live** — adding, editing, archiving and deleting components;
  the guard that stops you deleting a part with request history; approve and
  reject; that stock is deducted on approval; that every change moves the
  revision counter the live updates depend on; and that students and anonymous
  visitors are kept out of all of it.
- **test_upgrade_existing_db** — builds a database in the *old* shape, starts
  the current code against it, and checks the new column and table are added
  with every existing row, quantity and past request left intact.
- **test_all_pages_render** — every page as admin, as a student, and logged out.
- **test_pythonanywhere_wsgi** — runs the shipped `pythonanywhere_wsgi.py` the
  way that host runs it: working directory outside the project, environment
  stripped, `.env` found by absolute path. Then serves the WSGI callable over
  real HTTP and drives a login, an edit and the live-update endpoint through
  it. It borrows the project's `.env` while it runs and puts the original back
  afterwards.
