# Wadhwani Electronics Laboratory — website

A complete rebuild of the WEL website for IIT Bombay. It carries over every section of the old
WordPress site (`ee.iitb.ac.in/~wel_iitb`) and every section of the current Drupal site
(`wel.ee.iitb.ac.in`), including the WEL Inventory, which now sits under **Resources**.

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

That regenerates all 20 HTML files in the project root and fails loudly if any internal link no
longer resolves.

---

## What is in here

```
WEL website/
├── index.html … contact.html        20 generated pages — this is what you deploy
├── assets/
│   ├── css/style.css                the entire design system, one file
│   ├── js/main.js                   nav, lightbox, filters, counters — vanilla, no deps
│   └── img/                         site imagery, people, boards, facilities,
│                                    instruments and 67 gallery photos (+ thumbnails)
├── _src/                            page sources — edit here, then rebuild
│   ├── dev.py                       live editing server (rebuild + auto-refresh)
│   ├── build.py                     layout, navigation, header, footer, site constants
│   ├── pages_main.py                home, about, programs, achievements, blogs, contact
│   ├── pages_labs.py                teaching labs, autumn, spring, online request
│   ├── pages_resources.py           resources, facilities, boards, instruments,
│   │                                components, inventory
│   ├── pages_people.py              people, faculty, staff, gallery
│   └── gallery_manifest.json        gallery filenames and their categories
├── inventory-app/                   the Flask inventory app, restyled to match the site
├── .github/workflows/deploy.yml     rebuilds and publishes to GitHub Pages on every push
└── .claude/launch.json              local preview config
```

### The pages

| Page | File |
|---|---|
| Home | `index.html` |
| About WEL | `about.html` |
| Achievements | `achievements.html` |
| Blogs | `blogs.html` |
| Teaching Labs in WEL | `teaching-labs.html` |
| Autumn Semester | `autumn-semester.html` |
| Spring Semester | `spring-semester.html` |
| Programs | `programs.html` |
| Resources | `resources.html` |
| Advanced Facilities in WEL Lab | `advanced-facilities.html` |
| Development Boards Made in WEL | `made-in-wel.html` |
| Instruments | `instruments.html` |
| Components | `components.html` |
| **WEL Inventory** | `inventory.html` |
| Online Request | `online-request.html` |
| People | `people.html` |
| Faculty Members | `faculty.html` |
| Staff Members | `staff.html` |
| WEL Gallery | `gallery.html` |
| Contact Us | `contact.html` |

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
| Facilities specs, boards, instruments, components, inventory | `_src/pages_resources.py` |
| Faculty and staff names, roles, emails, phones | `FACULTY` / `STAFF` in `_src/pages_people.py` |
| Gallery photos and their categories | `_src/gallery_manifest.json` |
| Add a whole new page | copy an entry in any `PAGES` list, then add it to `NAV` |

The structured lists (`FACULTY`, `STAFF`, `FACILITIES`, `BOARDS`, `AUTUMN_COURSES`, …) are plain
Python tuples — editing them is filling in text between quotes, no code involved. Everything else is
ordinary HTML inside triple-quoted strings.

### The general rule

Everything that appears on more than one page — header, navigation, footer, phone numbers, the
inventory portal URL — lives at the top of **`_src/build.py`**:

```python
SITE = {
    "email": "wel@ee.iitb.ac.in",
    "phone_lab": "+91-22-2576-4484",
    "request_portal": "http://10.107.68.191",   # equipment / board requests
    "inventory_app": "http://10.107.68.191",    # WEL Inventory
    ...
}
```

Change a value there, run `python _src/build.py`, and it updates on all 20 pages.

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
touch `_src/`. The only cost is that header/footer changes then have to be made in 20 places. If you
go that route, delete `_src/` so nobody later regenerates over your edits.

---

## Publishing free on GitHub Pages

The repository is already initialised, committed on `main`, and carries a workflow that rebuilds and
publishes on every push. You only need to create the remote and push once.

**1. Create an empty repository** at <https://github.com/new>. Name it exactly `wel-website`,
owner `Prayag-Mohanty`. Do **not** tick "Add a README" — the repo already has one.

**2. Push.** The remote is already configured, so this is the whole command:

```bash
git push -u origin main
```

The first push opens a browser window to sign in to GitHub (Git Credential Manager). Approve it once
and it is remembered for every push after that.

**3. Turn Pages on.** In the repository: **Settings → Pages → Build and deployment → Source →
GitHub Actions**. That is the only click required; do not pick "Deploy from a branch".

**4. Watch it build.** The **Actions** tab shows the run. After about a minute the site is live at:

```
https://prayag-mohanty.github.io/wel-website/
```

That URL is public, shareable, HTTPS, and free with no bandwidth bill.

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

1. **The internal portal address.** `SITE["request_portal"]` is currently `http://10.107.68.191`,
   and it appears in the built HTML. It is an RFC 1918 address that nobody outside the institute
   network can reach, so it is not exploitable — but it does advertise a piece of internal network
   layout. If that bothers whoever runs the network, point those links at a hostname
   (`https://wel.ee.iitb.ac.in/request`) or at `online-request.html`, and let the lab server
   redirect internally.
2. **Staff names, emails and phone numbers.** These are already published on the current public WEL
   site, so nothing new is exposed — but confirm the staff are happy with the mobile numbers in
   particular, since `staff.html` lists them and they were carried over verbatim.

If either is a problem, make the repository **private** — GitHub Pages still works from a private
repo on free accounts, and the published site stays public while the source stays closed.

No secrets are committed: `.gitignore` excludes `inventory-app/.env` and the SQLite database, and
only `.env.example` with placeholder values is tracked.

---

## Other ways to deploy

**Option A — serve it directly (simplest).** Copy the `.html` files and `assets/` to the web root on
the lab server. Nothing else is required: no PHP, no database, no Drupal. This also removes the
attack surface that made the old site a problem — there is no CMS to exploit.

**Option B — keep Drupal, use this as the theme.** `assets/css/style.css` and `assets/js/main.js` are
framework-neutral. The header and footer markup generated by `build.py` maps directly onto
`page.html.twig`, and the class names (`.card`, `.person`, `.lcard`, `.section`) can be reused in
your node templates.

Either way, set `SITE["request_portal"]` and `SITE["inventory_app"]` in `_src/build.py` to the
real portal address before the final build, then rerun the build.

The CSS and JS are referenced with a content hash (`style.css?v=91e6269b`) that changes whenever
either file changes, so browsers pick up updates immediately instead of serving a stale cache.

---

## WEL Inventory

`inventory-app/` **is** the Flask application you sent, with its interface reskinned to match the
site. `app.py` is byte-identical to your zip — verified by diff. What was added around it:

- `templates/base.html` — rewritten with the WEL header and footer
- `static/css/wel-theme.css` — a theme layer loaded after Bootstrap
- `wsgi.py` — production entry point (see below)
- `render.yaml`, `DEPLOY.md` — hosting
- the other templates — only the two hard-coded colours swapped for theme variables

### It needs its own host

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

**`inventory-app/DEPLOY.md` has the three options** — the lab server, PythonAnywhere (free, and the
data persists), or Render (free, but the SQLite database resets on every restart, so not for real
stock records).

### Why wsgi.py exists

`app.py` creates the database tables inside `if __name__ == '__main__'`. A production server imports
the module rather than running it, so that block never fires and the app would start against an
empty database. `wsgi.py` does that setup at import time and exposes `app`, leaving `app.py`
untouched. Serve it with `gunicorn wsgi:app`.

### Running it locally

```bash
cd inventory-app
python -m venv venv
venv\Scriptsctivate
pip install -r requirements.txt
copy .env.example .env
python app.py
```

`.env` is gitignored and must stay that way — `SECRET_KEY` signs the login cookies, and a guessable
one lets someone forge an admin session.

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
2. **V. V. Shahin has no photograph** anywhere on either site, so his card falls back to initials.
   Drop a photo at `assets/img/team/vv-shahin.jpg` and add the path to his entry in `STAFF_GROUPS`
   in `_src/pages_people.py`.
3. **The instruments page** lists the five signal generators in full, because those are the only
   ones the current site actually populates. The other five categories are described but have no
   model listings yet. Add them to `SIGNAL_GENERATORS`-style lists in `pages_resources.py` as the
   data becomes available.
4. **Research assistants** are the five named in `RESEARCH_ASSISTANTS` in `_src/pages_people.py`.
   The old team page also lists Vineesh Modi, Prabhakar Singh, Jaydev Bapat and Tarun Choudhary
   (M.Tech 2026 batches, so they may have graduated) - add them back if they are still with the lab.
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
