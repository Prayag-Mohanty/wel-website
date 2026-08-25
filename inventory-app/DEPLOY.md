# Putting WEL Inventory online

WEL Inventory is a Flask application. It needs a host that can **run Python**.

That matters because the rest of the website is static files on GitHub Pages,
and **GitHub Pages cannot run Python** — it only serves files. So the site and
the inventory app live in the same repository but run in two different places:

```
prayag-mohanty.github.io/wel-website/   the website        (GitHub Pages, static)
        │
        └── "Open WEL Inventory" ──────► wherever you host this app  (runs Python)
```

Once the app is running somewhere, put its address in **one place**:

```python
# _src/build.py
"inventory_app": "https://your-address-here",
```

Rebuild (`python _src/build.py`), push, and every inventory link across the
site points at it. Leave it empty and the site says the portal is not online
yet rather than linking somewhere broken.

---

## Option 1 — the lab server (best for real use)

The lab already runs a server. This keeps stock data inside the institute and
costs nothing.

```bash
cd inventory-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt gunicorn
cp .env.example .env        # then edit it - see "Settings" below
gunicorn wsgi:app --bind 0.0.0.0:5000
```

Then set `"inventory_app": "http://wel.ee.iitb.ac.in:5000"` in `_src/build.py`.

To keep it running after you log out, use systemd — `SETUP_GUIDE_UBUNTU.md` has
the details. Put it behind nginx if you want it on port 80/443 with HTTPS.

**Note:** if the server is only reachable inside the institute network, students
off-campus will not be able to open it. That is the same limitation the old
`10.107.68.191` portal had.

## Option 2 — PythonAnywhere (free, and the data persists)

Best free option, because the filesystem persists — your SQLite database
survives restarts.

1. Sign up at <https://www.pythonanywhere.com> (Beginner plan, free).
2. **Consoles → Bash**:
   ```bash
   git clone https://github.com/Prayag-Mohanty/wel-website.git
   cd wel-website/inventory-app
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Web → Add a new web app → Manual configuration → Python 3.12**.
4. In the Web tab set:
   - **Source code**: `/home/USERNAME/wel-website/inventory-app`
   - **Virtualenv**: `/home/USERNAME/wel-website/inventory-app/venv`
   - **WSGI configuration file**: click it and replace the contents with:
     ```python
     import os, sys
     path = '/home/USERNAME/wel-website/inventory-app'
     if path not in sys.path:
         sys.path.insert(0, path)
     from dotenv import load_dotenv
     load_dotenv(os.path.join(path, '.env'))
     from wsgi import app as application
     ```
5. Create the `.env` file (Files tab) — see **Settings** below.
6. Hit **Reload**.

Your address is `https://USERNAME.pythonanywhere.com`.

To update later: `git pull` in a Bash console, then **Reload**.

## Option 3 — Render (free, but the database resets)

`render.yaml` in this folder is ready to use: **New → Blueprint → pick this
repo**. Set `ADMIN_EMAIL` and `ADMIN_PASSWORD` in the dashboard when prompted.

**Read this before choosing Render:** the free instance has no persistent disk.
The SQLite database is wiped on every restart and redeploy, and free services
sleep after inactivity. Every team registration and every stock change would be
lost. Fine for showing someone how it works; not fine for real stock records.

To use Render properly, either attach a paid disk or switch the app to Render's
managed Postgres by changing `SQLALCHEMY_DATABASE_URI` in `app.py` to read
`os.environ['DATABASE_URL']`.

---

## Settings

Copy `.env.example` to `.env` and fill it in:

```
SECRET_KEY=<a long random string>
ADMIN_EMAIL=your_roll_number@iitb.ac.in
ADMIN_PASSWORD=<a strong password>
# DATABASE_URL=sqlite:////var/lib/wel-inventory/inventory.db
# COOKIE_SECURE=1
```

- **`SECRET_KEY`** signs the login session cookies. If it is guessable, someone
  can forge a session and log in as anybody, including an admin. Generate one:
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- **`ADMIN_EMAIL`** gets the admin account. Log in at `/admin/login`.
- **`DATABASE_URL`** moves the database off the default `instance/inventory.db`.
  Use it to put the file on a mounted disk that your backups actually reach.
- **`COOKIE_SECURE=1`** stops the session cookie being sent over plain HTTP.
  Set it as soon as the app is behind HTTPS, and not before, or you will not be
  able to log in over `http://`.
- **`.env` is gitignored** and must never be committed.

## First run

1. Open the app and go to **Admin → Upload Excel**.
2. Upload your component list. Recognised columns: `Sr No`, `Type of Component`,
   `Model No`, `Description`, `Link`, `Location`, `Quantity`. A missing
   `Quantity` defaults to 1.
   You can also import straight from a Google Sheet link, if the sheet is shared
   as "anyone with the link can view".
3. Students register their team at `/register` with an `@iitb.ac.in` address,
   then browse stock, add to a cart and submit a request.
4. You approve or reject at **Admin → Requests**. Approving decrements stock.

You do not have to start from a spreadsheet: **Admin → Inventory → Add
component** builds the list by hand, and every field of an existing part can be
edited from the same page. `ADMIN_GUIDE.md` covers the day-to-day side of that,
including how the screens keep themselves up to date.

## Upgrading an existing installation

Safe to do in place. On start-up the app adds the one new column and the one new
table it needs, leaving existing stock, teams and request history untouched.
Take a copy of the database first anyway:

```bash
cp instance/inventory.db instance/inventory-before-upgrade.db
```

## Two things worth fixing before real use

Both are in the app as you wrote it — flagged, not changed:

1. **No password reset.** If a team forgets their shared password, an admin has
   to fix it directly in the database. Consider adding a reset flow.
2. **Bootstrap and its icon font load from a CDN.** If the host has no outbound
   internet, download those two files into `static/` and update the two `<link>`
   tags at the top of `templates/base.html`.
