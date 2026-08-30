# Wadhwani Electronics Laboratory — website

A complete rebuild of the WEL website for IIT Bombay. It carries over every section of the old
WordPress site (`ee.iitb.ac.in/~wel_iitb`) and every section of the current Drupal site
(`wel.ee.iitb.ac.in`), including the WEL Inventory, which sits under **Online Request**.

Link: https://prayag-mohanty.github.io/wel-website/

The site is **plain static HTML/CSS/JS** — no framework, no build tooling to install, no database.
Drop it on any web server (or open `index.html` directly) and it works.

---

## Quick start — the editing loop

```bash
python _src/dev.py
```

That is the whole workflow. It opens <http://localhost:8000>, watches the source files, and the
moment you save anything it rebuilds the site and **refreshes the browser by itself** — keeping your
scroll position, so you stay exactly where you were on the page. Edit, save, look. Typically under a
second.

If a build breaks, you get the Python error as a red banner across the bottom of the browser and the
last working version of the page stays on screen. Fix the file, save, the banner disappears.

Stop it with `Ctrl+C`. It needs nothing installed — Python's standard library only.

To build once without the server (this is also what the deploy runs):

```bash
python _src/build.py
```

That regenerates all 43 HTML files in the project root and fails loudly if any internal link no
longer resolves.

---

## What is in here

```
WEL website/
├── index.html … 404.html            43 generated pages — this is what you deploy
├── assets/
│   ├── css/style.css                the entire design system, one file
│   ├── js/main.js                   nav, lightbox, filters, counters — vanilla, no deps
│   ├── js/inventory.js              the on-site component browser
│   ├── data/inventory.json          component listing the browser reads
│   └── img/                         site imagery, people, boards, facilities,
│                                    instruments and 67 gallery photos (+ thumbnails)
├── _src/                            page sources — edit here, then rebuild
│   ├── dev.py                       live editing server (rebuild + auto-refresh)
│   ├── build.py                     layout, navigation, header, footer, site constants
│   ├── pages_main.py                home, about, programs, achievements, contact, 404
│   ├── pages_labs.py                teaching labs, autumn, spring, online request
│   ├── pages_resources.py           resources, facilities, instruments, components,
│   │                                made-in-wel, inventory
│   ├── pages_people.py              people, faculty, staff, gallery
│   ├── pages_courses.py             one detail page per lab course (8)
│   ├── pages_boards.py              board detail pages, the ELL and EMI/EMC facilities
│   ├── pages_products.py            achievement/product detail pages (5)
│   ├── pages_workshops.py           workshops, NPTEL year by year
│   ├── pages_publications.py        the publications list
│   ├── pages_blog.py                blogs index and the hosted post
│   ├── inventory_import.py          spreadsheet → assets/data/inventory.json
│   ├── make_favicons.py             regenerates the favicons from the logo
│   └── gallery_manifest.json        gallery filenames and their categories
├── inventory-app/                   the Flask inventory app, restyled to match the site
├── docker/ + compose.yaml           container packaging — see DOCKER.md
├── .github/workflows/deploy.yml     rebuilds and publishes to GitHub Pages on every push
└── .claude/launch.json              local preview config
```

### The pages

43 pages, all generated. Grouped by the module that produces them:

| Section | Pages |
|---|---|
| **Main** — `pages_main.py` | `index` · `about` · `programs` · `achievements` · `contact` · `404` |
| **Teaching** — `pages_labs.py` | `teaching-labs` · `autumn-semester` · `spring-semester` · `online-request` |
| **Courses** — `pages_courses.py` | `course-ee214` · `ee230` · `ee236` · `ee337` · `ee340` · `ee344` · `ee616` · `ee712` |
| **Resources** — `pages_resources.py` | `resources` · `advanced-facilities` · `made-in-wel` · `instruments` · `components` · **`inventory`** |
| **Boards & facilities** — `pages_boards.py` | `board-xen10` · `board-pt51` · `board-picoiris` · `board-iq-modulator` · `facility-ell` · `facility-emi-emc` |
| **People** — `pages_people.py` | `people` · `faculty` · `staff` · `gallery` |
| **Programs** — `pages_workshops.py`, `pages_blog.py` | `workshops` · `blogs` · `blog-online-lab-courses` |
| **Achievements** — `pages_products.py`, `pages_publications.py` | `product-nirmiti` · `product-acpad` · `product-welpcr` · `product-qmagpi` · `product-inspec` · `publications` |

`404.html` is served by nginx for unknown paths under Docker, and GitHub Pages picks it up
automatically — one page covers both hosts.

---

## Editing content

### Cheat sheet — where things live

| I want to change… | Edit |
|---|---|
| Phone number, email, address, portal URLs | `SITE` at the top of `_src/build.py` |
| The menu — add, rename, reorder, remove | `NAV` in `_src/build.py` |
| Header, footer, breadcrumbs — anything on every page | `header()` / `footer()` in `_src/build.py` |
| Colours, spacing, fonts, any styling | `assets/css/style.css` (tokens are in `:root` at the top) |
| Homepage hero, stats, sections | `HOME_HERO` / `HOME_BODY` in `_src/pages_main.py` |
| About, Programs, Achievements, Blogs, Contact | `_src/pages_main.py` |
| Teaching labs, course lists, online requests | `_src/pages_labs.py` |
| Facilities specs, instruments, components, inventory page | `_src/pages_resources.py` |
| A lab course's detail page | `COURSES` in `_src/pages_courses.py` |
| A development board, the ELL or the EMI/EMC facility | `BOARDS` / `ELL_KIT` / `EMI_PHOTOS` in `_src/pages_boards.py` |
| Workshops and the NPTEL editions | `EDITIONS` in `_src/pages_workshops.py` |
| The publications list | `PAPERS` in `_src/pages_publications.py` |
| An achievement / product page | `PRODUCTS` in `_src/pages_products.py` |
| Faculty, staff, research assistants | `FACULTY` / `STAFF_GROUPS` / `RESEARCH_ASSISTANTS` in `_src/pages_people.py` |
| Gallery photos and their categories | `_src/gallery_manifest.json` |
| Add a whole new page | copy an entry in any `PAGES` list, then add it to `NAV` |

The structured lists (`FACULTY`, `STAFF_GROUPS`, `BOARDS`, `COURSES`, `PAPERS`, …) are plain
Python tuples — editing them is filling in text between quotes, no code involved. Everything else is
ordinary HTML inside triple-quoted strings.

### The general rule

Everything that appears on more than one page — header, navigation, footer, phone numbers, the
inventory portal URL — lives at the top of **`_src/build.py`**:

```python
SITE = {
    "email": "wel@ee.iitb.ac.in",
    "phone_lab": "+91-22-2576-4484",
    "linkedin": "https://www.linkedin.com/company/wel-iit-bombay/",
    "youtube": "https://www.youtube.com/@WEL_IITB",
    "inventory_app": "",        # WEL Inventory — see "The portal needs its own host"
    ...
}
```

Change a value there, run `python _src/build.py`, and it updates on all 43 pages.

The navigation is the `NAV` list right below it. Add or reorder entries and every page's menu
follows.

Page bodies are ordinary HTML strings in the `pages_*.py` files. Structured content — the facility
specs, the staff list, the boards, the course lists — is held as Python lists at the top of each
module so you can edit the data without touching markup. For example, adding an instrument is one
line in `pages_resources.py`:

```python
SIGNAL_GENERATORS = [
    ("Anritsu MG3601A", "assets/img/instruments/anritsu-mg3601a.png", "Signal generator, 1040 MHz"),
    ...
]
```

### Adding gallery photos

1. Put the full-size image in `assets/img/gallery/`
2. Put a smaller version with the same filename in `assets/img/gallery/thumbs/`
3. Add an entry to `_src/gallery_manifest.json`:
   `{"file": "img_1234.jpg", "cat": "EDL project"}`
4. Rebuild

Categories in use: `EDL project`, `NPTEL`, `guest visit`, `WEL Facilities`, `School Workshop`,
`Research product`. The filter chips build themselves from whatever categories are present.

### If you would rather not use the build script

The generated HTML is completely standalone — you can edit the `.html` files directly and never
touch `_src/`. The only cost is that header/footer changes then have to be made in 43 places. If you
go that route, delete `_src/` so nobody later regenerates over your edits.

---

## Publishing on GitHub Pages

**The site is already live** at <https://prayag-mohanty.github.io/wel-website/>, published by
`.github/workflows/deploy.yml` on every push to `main`. Nothing needs setting up.

If you ever have to recreate it: create an empty repo, `git push -u origin main`, then
**Settings → Pages → Build and deployment → Source → GitHub Actions** (not "Deploy from a branch").

### After that, editing is a push

```bash
git add -A && git commit -m "Update the staff list" && git push
```

The workflow rebuilds and redeploys automatically — roughly a minute from push to live. If the build
fails (a broken link, a Python typo), the deploy is skipped and the old site stays up, so you cannot
push a broken site by accident.

You can also **edit straight on github.com** — open any file in `_src/`, click the pencil, commit.
The Action rebuilds and deploys. Useful for a quick fix from a phone or someone else's machine.

### A custom address

Free options, in order of effort:

- **Rename the repo** to `Prayag-Mohanty.github.io` and the site serves from
  `https://prayag-mohanty.github.io/` with no subfolder.
- **Use a domain you own** — add it under Settings → Pages → Custom domain, and GitHub issues the
  HTTPS certificate for free.
- **Ask the department** for something like `wel.ee.iitb.ac.in` to point at the Pages site with a
  CNAME. Then the public site is on GitHub and the lab server only has to run the inventory app.

Every link in the site is relative, so it works correctly whether it is served from a subfolder, a
domain root, or a `file://` path.

### Before you make the repository public

Two things become world-readable the moment you push to a public repo:

1. **Whatever address you put in `SITE["inventory_app"]`** appears in the built HTML. A hostname
   is better than a bare internal IP there: an RFC 1918 address is not reachable from outside and
   so not exploitable, but it does advertise a piece of internal network layout. (The old
   `10.107.68.191` portal has been removed from the site entirely.)
2. **Staff names, emails and phone numbers.** These are already published on the current public WEL
   site, so nothing new is exposed — but confirm the staff are happy with the mobile numbers in
   particular, since `staff.html` lists them and they were carried over verbatim.

If either is a problem, make the repository **private** — GitHub Pages still works from a private
repo on free accounts, and the published site stays public while the source stays closed.

No secrets are committed: `.gitignore` excludes `inventory-app/.env` and the SQLite database, and
only `.env.example` with placeholder values is tracked.

---

## Running it with Docker

`compose.yaml` packages the website and the inventory app so they run the same
anywhere with one command:

```bash
docker compose up -d
```

Website on :8080, WEL Inventory on :5000. There is also a `dev` profile that gives you the
live-editing loop without installing Python. **See [DOCKER.md](DOCKER.md)** for what Docker is, when
it is worth using here, and how to back up the inventory database.

`compose.yaml` validates, but **the images have never actually been built** — no Docker daemon has
been available on the machine this was written on. Expect to fix a small thing or two on the first
`docker compose up --build`. One bug has already been found and fixed by reading the file rather
than running it: `site.Dockerfile` claimed a broken internal link would fail the build, and it did
not, because `|| true` binds to the whole `&&` chain rather than to the command before it.

---

## Other ways to deploy

**Option A — serve it directly (simplest).** Copy the `.html` files and `assets/` to the web root on
the lab server. Nothing else is required: no PHP, no database, no Drupal. This also removes the
attack surface that made the old site a problem — there is no CMS to exploit.

**Option B — keep Drupal, use this as the theme.** `assets/css/style.css` and `assets/js/main.js` are
framework-neutral. The header and footer markup generated by `build.py` maps directly onto
`page.html.twig`, and the class names (`.card`, `.person`, `.lcard`, `.section`) can be reused in
your node templates.

Either way, set `SITE["inventory_app"]` in `_src/build.py` to the real portal address before the
final build, then rerun the build.

The CSS and JS are referenced with a content hash (`style.css?v=91e6269b`) that changes whenever
either file changes, so browsers pick up updates immediately instead of serving a stale cache.

---

## WEL Inventory

`inventory-app/` is the Flask application you were sent, reskinned to match the site and extended so
the lab can actually run stock from it.

**`app.py` is no longer byte-identical to the original zip** — it was, until admin editing and live
updates were added. Everything the original did, it still does.

Around it:

- `templates/base.html` — rewritten with the WEL header and footer
- `static/css/wel-theme.css` — a theme layer loaded after Bootstrap
- `static/js/live.js` — the polling that keeps every screen current
- `wsgi.py` — production entry point (see below)
- `pythonanywhere_wsgi.py` — ready to paste into that host's WSGI configuration
- `tests/` — 4 suites; run them with plain `python`, nothing to install
- [`ADMIN_GUIDE.md`](inventory-app/ADMIN_GUIDE.md) — day-to-day instructions for lab staff
- [`DEPLOY.md`](inventory-app/DEPLOY.md), `render.yaml` — hosting

### What an admin can do

- **Edit the component list.** Add a part, and edit every field of an existing one — type, model
  number, description, datasheet link, location, quantity. Not just the quantity.
- **Retire a part by archiving it.** It disappears from the student list but stays in the database,
  so past requests still read correctly, and it can be restored. Permanent deletion is offered only
  for a part that has never appeared on a request; otherwise the app refuses and says why, because
  deleting it would leave old requests pointing at nothing.
- **Approve or reject requests.** Approving deducts the quantities from stock automatically. If a
  line asks for more than you hold, nothing is approved and it names the part that is short.
- **Bulk import** from an Excel file or a Google Sheets link.

### Every screen updates itself

Submit a request as a student and it appears in the admin queue without anyone reloading. Approve
it and the student's page flips to APPROVED on its own. The pending count in the navigation bar is
live everywhere.

This is polling, not websockets — a small endpoint reports a revision counter that every change
bumps, and the page re-fetches only when it moves. Deliberate: it works on an ordinary gunicorn
worker, through any proxy, with no special server configuration. Two details worth knowing: the
refresh pauses while you are typing or have a dialog open, so it cannot wipe half-entered work, and
a background tab drops from a 5-second to a 30-second interval.

`ADMIN_GUIDE.md` has the rest. **Returns are not tracked** — approving reduces stock and nothing
puts it back, so adjust by hand when components come in.

### Two halves

The component stock appears in two places, both fed by the same spreadsheet:

**1. On the website** (`inventory.html`) — a searchable listing of everything the lab holds, with a
request list you can email. Works on GitHub Pages, no sign-in, nothing to run. This is what most
students need.

**2. The portal** (`inventory-app/`) — the Flask app, which adds team accounts, a tracked request
queue, admin approval and automatic stock decrement. Needs a host that runs Python.

### Keeping the listing current

The site reads `assets/data/inventory.json`. Regenerate it from the component spreadsheet — the same
file the app's "Upload Excel" screen takes:

```bash
python _src/inventory_import.py path/to/components.xlsx
```

```bash
python _src/build.py
```

Then commit and push. It accepts `.xlsx`, `.xls` and `.csv`, and the same column names the app
accepts: `Sr No`, `Type of Component`, `Model No`, `Description`, `Link`, `Location`, `Quantity`.
Blank rows are skipped and a missing quantity becomes 1. Reading `.xlsx` needs
`pip install pandas openpyxl`; `.csv` needs nothing.

**The file currently holds sample data**, and the page says so in an amber notice until you replace
it. Run the importer once on the real spreadsheet and the notice disappears.

### The portal needs its own host

The website is static files on GitHub Pages. **GitHub Pages cannot run Python.** So the two halves
run in different places:

```
prayag-mohanty.github.io/wel-website/   the website     (GitHub Pages, static)
        │
        └── "Open WEL Inventory" ──────► wherever you host the app  (runs Python)
```

Once the app is running, set its address in **one place** and every inventory link on the site
follows:

```python
# _src/build.py
"inventory_app": "https://your-address-here",
```

While it is empty, the site says the portal is not online yet instead of linking somewhere broken.

**[`inventory-app/DEPLOY.md`](inventory-app/DEPLOY.md) has three options.** In short:

| Host | Free | Data survives a restart |
|---|---|---|
| **Lab server** (Docker or gunicorn) | yes | yes — and the data stays inside the institute |
| **PythonAnywhere** | yes | yes — best free option |
| Render | yes | **no** — SQLite is wiped on every restart and redeploy |

For a free host, use **PythonAnywhere**: paste `pythonanywhere_wsgi.py` into its WSGI configuration
and change one line. That path is tested — `tests/test_pythonanywhere_wsgi.py` runs the shipped file
the way that host runs it, with the working directory outside the project and the environment
stripped, then serves it over real HTTP.

For real use the lab server is better, because the database holds student names and roll numbers.

### Why wsgi.py exists

`app.py` sets the database up inside `if __name__ == '__main__'`. A production server imports the
module rather than running it, so that block never fires and the app would start against an empty
database. `wsgi.py` runs the same setup at import time — creating tables, upgrading an older
database, seeding the admin account — and exposes `app`. Serve it with `gunicorn wsgi:app`.

Start-up also **upgrades an existing database in place**, adding the column and table that the
newer features need while leaving stock, teams and request history intact. Take a copy first
anyway.

### Running it locally

```bash
cd inventory-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python app.py
```

Then edit `.env`: `SECRET_KEY` must be a long random value (`python -c "import secrets;
print(secrets.token_hex(32))"`), and `ADMIN_EMAIL` / `ADMIN_PASSWORD` create the first admin
account. `.env` is gitignored and must stay that way — a guessable `SECRET_KEY` lets someone forge
an admin session.

Student portal on <http://localhost:5000>, admin at `/admin/login`.

### Tests

```bash
cd inventory-app
python tests/test_admin_and_live.py
python tests/test_upgrade_existing_db.py
python tests/test_all_pages_render.py
python tests/test_pythonanywhere_wsgi.py
```

No test framework to install. Each builds its own throwaway database and asserts it did before
touching anything, so running them can never write to `instance/inventory.db`.

## Where the content came from

Text and data were taken from the two existing sites, not invented:

- **Old site** (`ee.iitb.ac.in/~wel_iitb`) — About, Programs, Resources, Achievements, Blogs, the
  founder profile, the statistics, and most photography
- **Current site** (`wel.ee.iitb.ac.in`) — teaching lab courses, the advanced facilities
  specifications, the Made in WEL boards, the instruments, components, faculty and staff lists, and
  the 67 gallery photographs

Images are stored locally in `assets/img/` — the site makes no requests to either old host, so it
keeps working if they go away.

### Worth checking before you publish

A few things are reproduced exactly as the current site publishes them, and may want a second look:

1. **Prof. Arun S.'s email is corrected here.** The current WEL site publishes
   `sarun.laha@ee.iitb.ac.in`, which appears to have absorbed part of Prof. Apurba Laha's address.
   His EE department profile gives `sarun@ee.iitb.ac.in`, and that is what this site uses. Worth
   fixing on the Drupal site too.
2. **The component listing on the website is sample data.** `assets/data/inventory.json` holds 20
   made-up rows so the browser can be seen working, and the page carries an amber notice saying so.
   Run `python _src/inventory_import.py` on the real spreadsheet and the notice disappears.
3. **The instruments page** lists the five signal generators in full, because those are the only
   ones the current site actually populates. The other five categories are described but have no
   model listings yet. Add them to `SIGNAL_GENERATORS`-style lists in `pages_resources.py` as the
   data becomes available.
4. **Utkarsh Shukla's photograph has two people in it** - him and a colleague at a lab bench - so
   the card crop is ambiguous about which one he is. Replace `assets/img/team/utkarsh-shukla.jpg`
   with a single-subject photo, or say which person he is and the existing one can be cropped to
   him.
5. **Course pages** carry many links to `10.107.68.222`, the old lab server. They are tagged
   `internal` because they only resolve on the institute network. Some sidebar items on the source
   pages - EDL group allotment and timeline, EE 230 batch lists, EE 712 lab schedule - had no
   destination at all, so they are described in a note rather than linked.
6. **NPTEL 2025 videos are private.** The playlist has 12 videos but YouTube reports all of them as
   unavailable, so nothing is publicly playable and an embed would show "Video unavailable". That
   edition links the playlist instead. Set the videos to Public or Unlisted on YouTube and they can
   be embedded like every other year - add their ids to the 2025 entry in
   `_src/pages_workshops.py`. The 2025 courses and dates are not published anywhere I could find,
   so that entry is deliberately thin; fill in `courses` and `dates` when you have them.
7. **Course descriptions** on the semester pages and course pages come from the current Drupal
   site. The one-line summaries in the semester lists are new and worth a review by whoever runs
   each course.
8. **The EMI/EMC page was written from photographs.** The old site's EMI/EMC page carried no text
   at all — only five images. The description on `facility-emi-emc.html` is written from those
   photographs and from what the rest of the site records about the advanced measurements wing. No
   instrument models, frequency ranges or standards are claimed, because none were published. If
   you have those details they are worth adding.
9. **The NIRMITI photograph** is a crop from the project's own poster, because no separate product
   photo was published. Replace `assets/img/products/nirmiti.jpg` if you have a better one.
10. **Returns are not tracked in WEL Inventory.** Approving a request reduces stock; nothing puts
    it back when a team brings components in. Adjust the quantity by hand for now. If issue-and-
    return becomes the normal pattern it is worth building properly.
11. **The Docker images have never been built** — see the Docker section above.
