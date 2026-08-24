#!/usr/bin/env python3
"""
Static site builder for the Wadhwani Electronics Laboratory website.

Usage:      python _src/build.py
Output:     *.html in the project root (assets/ is used as-is)

Everything that appears on more than one page - the header, navigation,
footer, meta tags - lives here.  Page bodies live in _src/pages_*.py.
"""
import os
import re
import sys
import html
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

SITE = {
    "name": "Wadhwani Electronics Laboratory",
    "short": "WEL",
    "dept": "Department of Electrical Engineering, IIT Bombay",
    "tagline": "Think it. Make it. Prove it.",
    "address": "Wadhwani Electronics Laboratory, 3rd Floor, Electrical Engineering Department, "
               "IIT Bombay, Powai, Mumbai 400076, India",
    "email": "wel@ee.iitb.ac.in",
    "phone_lab": "+91-22-2576-4484",
    "phone_office": "+91-22-2159-3524",
    "linkedin": "https://www.linkedin.com/company/wel-iit-bombay/",
    "youtube": "https://www.youtube.com/@WEL_IITB",
    "old_site": "https://www.ee.iitb.ac.in/~wel_iitb/index.php",

    # ------------------------------------------------------------------
    # WEL Inventory - the Flask app in inventory-app/.
    #
    # Put its address here once it is running and every link on the site
    # points at it.  Leave it empty and the site says so honestly instead of
    # linking somewhere broken.
    #
    #   on the lab server   "http://wel.ee.iitb.ac.in:5000"
    #   on PythonAnywhere   "https://welinventory.pythonanywhere.com"
    #   on Render           "https://wel-inventory.onrender.com"
    #
    # See inventory-app/DEPLOY.md.
    # ------------------------------------------------------------------
    "inventory_app": "",

    "facilities_form": "https://wel.ee.iitb.ac.in/wel_facilities_update",
}


def inventory_url(fallback="inventory.html"):
    """Where inventory links should point.  Falls back to the info page while
    the app has no address, so the site never carries a dead link."""
    return SITE["inventory_app"] or fallback


def inventory_live():
    return bool(SITE["inventory_app"])

# ---------------------------------------------------------------------------
# Navigation:  (label, href, [(sub label, sub href, sub note), ...])
# ---------------------------------------------------------------------------
NAV = [
    ("Home", "index.html", None),
    ("About", "about.html", [
        ("About WEL", "about.html", "What we are, who we are, what we do"),
        ("Achievements", "achievements.html", "Products, publications and recognition"),
        ("Blogs", "blogs.html", "Reports and writing from the lab"),
    ]),
    ("Teaching Labs", "teaching-labs.html", [
        ("Autumn Semester", "autumn-semester.html", "Courses running July - November"),
        ("Spring Semester", "spring-semester.html", "Courses running January - April"),
    ]),
    ("Programs", "programs.html", [
        ("Programs overview", "programs.html", "Workshops, courses, internships, MOOCs"),
        ("Workshops", "workshops.html", "NPTEL, teacher training and outreach"),
    ]),
    ("Resources", "resources.html", [
        ("Advanced Facilities in WEL", "advanced-facilities.html", "Chambers, printers, cutters, winders"),
        ("Development Boards - Made in WEL", "made-in-wel.html", "PicoIRIS, PT-51, Xen-10, IQ Modulator"),
        ("Instruments", "instruments.html", "Generators, scopes, analyzers, meters"),
        ("Components", "components.html", "Stock, datasheets and component lists"),
        ("WEL Inventory", "inventory.html", "Search stock and raise a component request"),
    ]),
    ("Online Request", "online-request.html", [
        ("Special Facilities Request", "online-request.html#special-facilities", "Chambers, EMI/EMC, PCB, prototyping"),
        ("Development Boards & Modules", "online-request.html#dev-boards", "Borrow boards for a project"),
        ("Equipment Loan", "online-request.html#equipment-loan", "Borrow instruments for a period"),
    ]),
    ("People", "people.html", None),
    ("Gallery", "gallery.html", None),
    ("Contact", "contact.html", None),
]

# ---------------------------------------------------------------------------
# Inline SVG icons
# ---------------------------------------------------------------------------
ICONS = {
    "caret": '<svg class="nav__caret" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2.5" y="4.5" width="19" height="15" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M3 7l9 6 9-6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6.6 3h3l1.5 4-2 1.5a12 12 0 006.4 6.4l1.5-2 4 1.5v3a2 2 0 01-2.2 2A17 17 0 014.6 5.2 2 2 0 016.6 3z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 21s7-6.1 7-11a7 7 0 10-14 0c0 4.9 7 11 7 11z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.6" stroke="currentColor" stroke-width="1.7"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="11" cy="11" r="6.5" stroke="currentColor" stroke-width="1.8"/><path d="M16 16l4.5 4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "up": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "prev": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M15 19l-7-7 7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "next": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M9 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "external": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M14 4h6v6M20 4l-8.5 8.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M18 14.5V19a1.5 1.5 0 01-1.5 1.5h-11A1.5 1.5 0 014 19V8a1.5 1.5 0 011.5-1.5H10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 11-.02 5 2.5 2.5 0 01.02-5zM3 9h4v12H3zM10 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.4c0-1.29-.02-2.95-1.8-2.95-1.8 0-2.08 1.4-2.08 2.85V21h-4z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 12s0-3.4-.44-5.03a2.6 2.6 0 00-1.83-1.84C19.1 4.7 12 4.7 12 4.7s-7.1 0-8.73.43A2.6 2.6 0 001.44 6.97C1 8.6 1 12 1 12s0 3.4.44 5.03a2.6 2.6 0 001.83 1.84c1.63.43 8.73.43 8.73.43s7.1 0 8.73-.43a2.6 2.6 0 001.83-1.84C23 15.4 23 12 23 12zM9.75 15.5v-7l6 3.5z"/></svg>',
    "chip": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="7" y="7" width="10" height="10" rx="1.6" stroke="currentColor" stroke-width="1.7"/><path d="M10 3.5v3M14 3.5v3M10 17.5v3M14 17.5v3M3.5 10h3M3.5 14h3M17.5 10h3M17.5 14h3" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "board": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2.5" stroke="currentColor" stroke-width="1.7"/><circle cx="8.5" cy="8.5" r="1.6" stroke="currentColor" stroke-width="1.5"/><path d="M8.5 10.5V16h7M12 8h5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "scope": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2.5" y="4.5" width="19" height="13" rx="2" stroke="currentColor" stroke-width="1.7"/><path d="M5.5 12.5h2.2l1.6-4 2 7 1.7-5 1.3 2h3.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M8.5 21h7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "flask": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M9.5 3v5.6L4.6 17a2.2 2.2 0 001.9 3.3h11a2.2 2.2 0 001.9-3.3l-4.9-8.4V3" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M8 3h8M7 14h10" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "box": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3.5 7.5L12 3l8.5 4.5v9L12 21l-8.5-4.5z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M3.5 7.5L12 12m0 0l8.5-4.5M12 12v9" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "clipboard": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="5" y="4.5" width="14" height="16" rx="2" stroke="currentColor" stroke-width="1.7"/><rect x="9" y="2.5" width="6" height="4" rx="1.3" stroke="currentColor" stroke-width="1.7"/><path d="M9 11h6M9 15h4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "people": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="9" cy="8" r="3.2" stroke="currentColor" stroke-width="1.7"/><path d="M3.5 20a5.5 5.5 0 0111 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M16 5.4a3.2 3.2 0 010 5.2M17.5 20a5.5 5.5 0 00-2-4.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 5.5A2 2 0 016 3.5h5v17H6a2 2 0 01-2-2z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M20 5.5a2 2 0 00-2-2h-5v17h5a2 2 0 002-2z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
    "tool": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M14.5 6a4 4 0 105.2 5.2l-3-3z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M13 10.5L4.8 18.7a1.8 1.8 0 002.5 2.5l8.2-8.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 2.5l2.2 6.1 6.3 2.2-6.3 2.2L12 19.5l-2.2-6.5-6.3-2.2 6.3-2.2z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>',
    "camera": '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="2.5" y="6.5" width="19" height="13" rx="2.5" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="13" r="3.6" stroke="currentColor" stroke-width="1.7"/><path d="M8.5 6.5l1.4-2.4h4.2l1.4 2.4" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>',
}


_ASSET_V = None


def asset_version():
    """Short hash of the CSS + JS so browsers pick up changes after a rebuild.

    Line endings are normalised before hashing: git hands out CRLF on Windows
    and LF on the Linux CI runner, and without this the same source would
    produce a different hash on each, leaving the generated HTML permanently
    dirty after a checkout.
    """
    global _ASSET_V
    if _ASSET_V is None:
        import hashlib
        h = hashlib.md5()
        for rel in ("assets/css/style.css", "assets/js/main.js"):
            path = os.path.join(ROOT, rel.replace("/", os.sep))
            if os.path.exists(path):
                with open(path, "rb") as fh:
                    h.update(fh.read().replace(b"\r\n", b"\n"))
        _ASSET_V = h.hexdigest()[:8]
    return _ASSET_V


def icon(name, cls=""):
    svg = ICONS[name]
    if cls:
        svg = svg.replace("<svg ", '<svg class="%s" ' % cls, 1)
    return svg


# ---------------------------------------------------------------------------
# Fragments
# ---------------------------------------------------------------------------
def build_nav(active, active_sub):
    out = []
    for label, href, kids in NAV:
        is_active = (href == active)
        if kids:
            links = []
            for k_label, k_href, k_note in kids:
                cls = " class=\"is-active\"" if k_href == active_sub else ""
                note = '<small>%s</small>' % k_note if k_note else ""
                links.append('<a href="%s"%s>%s%s</a>' % (k_href, cls, k_label, note))
            out.append(
                '<li class="nav__item nav__item--has-children">'
                '<a class="nav__link%s" href="%s" aria-haspopup="true">%s %s</a>'
                '<div class="dropdown">%s</div></li>'
                % (" is-active" if is_active else "", href, label, icon("caret"), "".join(links))
            )
        else:
            out.append(
                '<li class="nav__item"><a class="nav__link%s" href="%s">%s</a></li>'
                % (" is-active" if is_active else "", href, label)
            )
    return "\n          ".join(out)


def header(active, active_sub):
    return """  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="site-header" id="siteHeader">
    <div class="wrap header__inner">
      <a class="brand" href="index.html" aria-label="Wadhwani Electronics Laboratory - home">
        <img src="assets/img/site/wel-logo.png" alt="Wadhwani Electronics Laboratory" width="95" height="52">
      </a>

      <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav">
        <span></span><span></span><span></span>
      </button>

      <nav class="nav" id="nav" aria-label="Main navigation">
        <ul style="display:contents;list-style:none;margin:0;padding:0">
          {nav}
        </ul>
        <div class="nav__mobile-cta">
          <a class="btn btn--red btn--sm" href="inventory.html">WEL Inventory</a>
        </div>
      </nav>

      <div class="header__cta">
        <a class="btn btn--red btn--sm" href="inventory.html">WEL Inventory</a>
      </div>
    </div>
  </header>
  <div class="nav-scrim" id="navScrim"></div>
""".format(nav=build_nav(active, active_sub))


def footer(extra_js=""):
    return """  <footer class="site-footer">
    <div class="wrap">
      <div class="footer__grid">
        <div class="footer__brand">
          <img src="assets/img/site/wel-logo.png" alt="Wadhwani Electronics Laboratory" width="102" height="56">
          <p>Where electronics lives. WEL provides students at IIT Bombay the space, hardware and
             mentorship to make impactful innovations in electronic systems, through curricular and
             co-curricular activities.</p>
          <div class="social">
            <a href="{linkedin}" target="_blank" rel="noopener" aria-label="WEL on LinkedIn">{li}</a>
            <a href="{youtube}" target="_blank" rel="noopener" aria-label="WEL on YouTube">{yt}</a>
            <a href="mailto:{email}" aria-label="Email WEL">{mail}</a>
          </div>
        </div>

        <div>
          <h5>Explore</h5>
          <ul>
            <li><a href="about.html">About WEL</a></li>
            <li><a href="teaching-labs.html">Teaching Labs</a></li>
            <li><a href="programs.html">Programs</a></li>
            <li><a href="achievements.html">Achievements</a></li>
            <li><a href="gallery.html">Gallery</a></li>
            <li><a href="blogs.html">Blogs</a></li>
          </ul>
        </div>

        <div>
          <h5>Resources</h5>
          <ul>
            <li><a href="advanced-facilities.html">Advanced Facilities</a></li>
            <li><a href="made-in-wel.html">Made in WEL Boards</a></li>
            <li><a href="instruments.html">Instruments</a></li>
            <li><a href="components.html">Components</a></li>
            <li><a href="inventory.html">WEL Inventory</a></li>
            <li><a href="online-request.html">Online Requests</a></li>
          </ul>
        </div>

        <div class="footer__contact">
          <h5>Reach us</h5>
          <div>{pin}<span>3rd Floor, Electrical Engineering Department,<br>IIT Bombay, Powai, Mumbai 400076</span></div>
          <div>{mail}<a href="mailto:{email}">{email}</a></div>
          <div>{phone}<span>{phone_lab} (Lab)<br>{phone_office} (Office)</span></div>
        </div>
      </div>

      <div class="footer__bottom">
        <span>&copy; <span data-year>2026</span> Wadhwani Electronics Laboratory, IIT Bombay. All rights reserved.</span>
        <span><a href="contact.html">Contact</a> &middot; <a href="{old_site}" target="_blank" rel="noopener">Archived website</a></span>
      </div>
    </div>
  </footer>

  <button class="to-top" id="toTop" aria-label="Back to top">{up}</button>
  <script src="assets/js/main.js?v={v}"></script>
{extra_js}""".format(
        v=asset_version(),
        extra_js=extra_js,
        linkedin=SITE["linkedin"], youtube=SITE["youtube"], email=SITE["email"],
        phone_lab=SITE["phone_lab"], phone_office=SITE["phone_office"],
        old_site=SITE["old_site"],
        li=icon("linkedin"), yt=icon("youtube"), mail=icon("mail"),
        pin=icon("pin"), phone=icon("phone"), up=icon("up"),
    )


def page_hero(title, blurb, crumbs, bg="assets/img/site/wel1-lab.jpeg"):
    trail = ['<a href="index.html">Home</a>']
    for label, href in crumbs[:-1]:
        trail.append('<span>/</span><a href="%s">%s</a>' % (href, label))
    trail.append('<span>/</span>%s' % crumbs[-1][0])
    return """  <section class="page-hero">
    <div class="page-hero__bg"><img src="%s" alt="" loading="eager"></div>
    <div class="wrap page-hero__inner">
      <nav class="crumbs" aria-label="Breadcrumb">%s</nav>
      <h1>%s</h1>
      <p>%s</p>
    </div>
  </section>
""" % (bg, "".join(trail), title, blurb)


# ---------------------------------------------------------------------------
# Page shell
# ---------------------------------------------------------------------------
TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0c53a5">
<link rel="icon" href="assets/img/site/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/img/site/favicon-512.png" sizes="512x512" type="image/png">
<link rel="apple-touch-icon" href="assets/img/site/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/site/homepage-hero.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={v}">
<script>document.documentElement.className += " js";</script>
{extra_head}</head>
<body>
{header}
  <main id="main">
{body}  </main>

{footer}</body>
</html>
"""


def render(page):
    body = page.get("hero", "") + page["body"]
    return TEMPLATE.format(
        title=page["title"],
        v=asset_version(),
        desc=html.escape(page["desc"], quote=True),
        extra_head=page.get("extra_head", ""),
        header=header(page.get("nav"), page.get("sub")),
        body=body,
        footer=footer(page.get("extra_js", "")),
    )


def main():
    import pages_main, pages_labs, pages_resources, pages_people, pages_courses, pages_blog
    import pages_workshops

    pages = []
    for mod in (pages_main, pages_labs, pages_resources, pages_people, pages_courses,
                pages_blog, pages_workshops):
        pages.extend(mod.PAGES)

    written = []
    for page in pages:
        out = os.path.join(ROOT, page["file"])
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(render(page))
        written.append((page["file"], os.path.getsize(out)))

    print("Built %d pages into %s\n" % (len(written), ROOT))
    for name, size in sorted(written):
        print("  %-28s %6.1f KB" % (name, size / 1024.0))

    # sanity check: every internal href must resolve to a generated page or a real file
    names = {p["file"] for p in pages}
    missing = set()
    for page in pages:
        html_txt = render(page)
        for href in re.findall(r'href="([^"#?:]+)(?:[#?][^"]*)?"', html_txt):
            if href.startswith(("http", "mailto", "tel", "//")):
                continue
            if href in names:
                continue
            if os.path.exists(os.path.join(ROOT, href.replace("/", os.sep))):
                continue
            missing.add((page["file"], href))
    if missing:
        print("\n!! Unresolved links:")
        for src, href in sorted(missing):
            print("   %s -> %s" % (src, href))
    else:
        print("\nAll internal links resolve.")


if __name__ == "__main__":
    main()
