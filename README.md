# Wadhwani Electronics Laboratory — website

A complete rebuild of the WEL website for IIT Bombay. It carries over every section of the old
WordPress site (`ee.iitb.ac.in/~wel_iitb`) and every section of the current Drupal site
(`wel.ee.iitb.ac.in`), including the IITB WEL Inventory, which now sits under **Resources**.

The site is **plain static HTML/CSS/JS** — no framework, no build tooling to install, no database.
Drop it on any web server (or open `index.html` directly) and it works.

---

## Quick start

Preview it locally:

```bash
python -m http.server 8123
```

Then open <http://localhost:8123>.

To rebuild the pages after editing content:

```bash
python _src/build.py
```

That regenerates all 20 HTML files in the project root and verifies that every internal link
resolves.

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
│   ├── build.py                     layout, navigation, header, footer, site constants
│   ├── pages_main.py                home, about, programs, achievements, blogs, contact
│   ├── pages_labs.py                teaching labs, autumn, spring, online request
│   ├── pages_resources.py           resources, facilities, boards, instruments,
│   │                                components, inventory
│   ├── pages_people.py              people, faculty, staff, gallery
│   └── gallery_manifest.json        gallery filenames and their categories
├── inventory-app/                   the Flask inventory app, restyled to match the site
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
| **IITB WEL Inventory** | `inventory.html` |
| Online Request | `online-request.html` |
| People | `people.html` |
| Faculty Members | `faculty.html` |
| Staff Members | `staff.html` |
| WEL Gallery | `gallery.html` |
| Contact Us | `contact.html` |

---

## Editing content

Everything that appears on more than one page — header, navigation, footer, phone numbers, the
inventory portal URL — lives at the top of **`_src/build.py`**:

```python
SITE = {
    "email": "wel@ee.iitb.ac.in",
    "phone_lab": "+91-22-2576-4484",
    "request_portal": "http://10.107.68.191",   # equipment / board requests
    "inventory_app": "http://10.107.68.191",    # IITB WEL Inventory
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

## Deploying

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

## The inventory app

`inventory-app/` is your Flask application with its interface reskinned to match the site — same
logo, typography, blue, red, dark header strip and footer. **No application logic was changed**;
`app.py` is byte-identical to what you sent. What changed:

- `templates/base.html` — rewritten with the WEL header, topbar and footer, and links back to
  the main site
- `static/css/wel-theme.css` — new; a theme layer loaded after Bootstrap so it overrides it
- `static/img/wel-logo.png` — new
- the other templates — only the two hard-coded colours (`#003366`, `#c8a84b`) swapped for the
  theme variables, so they follow the palette

Running it is unchanged, and `SETUP_GUIDE.md` still applies:

```bash
cd inventory-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python app.py
```

Two notes for the lab server:

- Bootstrap and Bootstrap Icons load from jsDelivr, as they did before. If the server has no
  outbound internet, download those two files into `static/` and change the two `<link>` tags in
  `templates/base.html` to point at them.
- `.env` is deliberately not included — copy `.env.example` and set a real `SECRET_KEY`,
  `ADMIN_EMAIL` and `ADMIN_PASSWORD`. Do not reuse the sample secret key in production.

---

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

1. **Prof. Arun S.'s email** is listed as `sarun.laha@ee.iitb.ac.in` on the current site. That looks
   like it may have picked up part of Prof. Apurba Laha's address. Verify it.
2. **V. V. Shahin has no photograph** — the image on the current site returns a 404, so the card
   falls back to initials. Drop a photo at `assets/img/people/vv-shahin.jpg` and add the path to
   `STAFF` in `_src/pages_people.py`.
3. **The instruments page** lists the five signal generators in full, because those are the only
   ones the current site actually populates. The other five categories are described but have no
   model listings yet. Add them to `SIGNAL_GENERATORS`-style lists in `pages_resources.py` as the
   data becomes available.
4. **Research assistants are described but not named.** The old site's RA list covers M.Tech 2026
   and 2027 batches and some of those students have since graduated, so publishing it unverified
   would be wrong. Add the current roster to `pages_people.py` when you have it.
5. **Course descriptions** on the semester pages are short, factual summaries. The course codes and
   titles are exactly as the current site lists them; the one-line descriptions are new and should
   be reviewed by whoever runs each course.
