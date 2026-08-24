# -*- coding: utf-8 -*-
"""People (overview / faculty / staff) and the gallery."""
import json
import os

from build import SITE, icon, page_hero, HERE

# ---------------------------------------------------------------------------
# Data.  Names, roles, emails and phone numbers as published by the lab.
# ---------------------------------------------------------------------------
FACULTY = [
    ("Prof. Rajbabu Velmurugan", "Lab In-charge", "rajbabu@ee.iitb.ac.in",
     "022-2576-7444 (O) / 022-2576-8444 (R)", "assets/img/people/rajbabu-velmurugan.png"),
    ("Prof. Rahul Singh", "Faculty member", "rahuls@ee.iitb.ac.in",
     "022-2576-7417 (O)", "assets/img/people/rahul-singh.jpg"),
    ("Prof. Dwaipayan Mukherjee", "Faculty member", "dm@ee.iitb.ac.in",
     "022-2576-9426 (O)", "assets/img/people/dwaipayan-mukherjee.png"),
    ("Prof. Arun S.", "Faculty member", "sarun.laha@ee.iitb.ac.in",
     "022-2576-7413 (O)", "assets/img/people/arun-s.jpg"),
    ("Prof. Apurba Laha", "Faculty member", "laha@ee.iitb.ac.in",
     "022-2576-9408 (O)", "assets/img/people/apurba-laha.png"),
]

STAFF = [
    ("Mahesh A. Bhaganagare", "Technical Officer", "mab@ee.iitb.ac.in",
     "022-2576-4412 / 4403 (O) &middot; 92264 19459 (M)", "assets/img/people/mahesh-bhaganagare.jpg", "Technical"),
    ("Amit Shetye", "Sr. Technical Superintendent", "amits@ee.iitb.ac.in",
     "022-2576-4484 (O) &middot; 99202 45689 (M)", "assets/img/people/amit-shetye.jpg", "Technical"),
    ("Maheshwar Mangat", "Sr. Technical Superintendent", "maheshgm@ee.iitb.ac.in",
     "022-2576-4412 / 4409 (O) &middot; 96198 27670 (M)", "assets/img/people/maheshwar-mangat.jpg", "Technical"),
    ("Ankur Agarwal", "Jr. Technical Superintendent", "ankur_ee@iitb.ac.in",
     "022-2576-4409 (O) &middot; 99674 43616 (M)", "assets/img/people/ankur-agarwal.jpg", "Technical"),
    ("Nilesh Sawant", "Sr. Technical Superintendent (System Administration)", "nilesh.t.sawant@ee.iitb.ac.in",
     "022-2576-4412 (O) &middot; 95946 20670 (M)", "assets/img/people/nilesh-sawant.jpg", "Technical"),
    ("Anil Gawai", "Project Assistant (Administration)", "anilrg@ee.iitb.ac.in",
     "022-2576-4412 (O) &middot; 09220 087540 (M)", "assets/img/people/anil-gawai.jpg", "Administration"),
    ("Chandrashekhar Shele", "Multi-Skilled Assistant", "shekhars@ee.iitb.ac.in",
     "022-2576-4409 (O) &middot; 92202 12167 (M)", "assets/img/people/chandrashekhar-shele.jpg", "Support"),
    ("Sadanand Sawant", "Sr. Mechanic (Electronics)", "ssawant@ee.iitb.ac.in",
     "022-2576-4412 (O)", "assets/img/people/sadanand-sawant.jpg", "Support"),
    ("Suraj S. Sarfare", "Jr. Mechanic", "sarfaresuraj@ee.iitb.ac.in",
     "022-2576-4412 (O)", "assets/img/people/suraj-sarfare.jpg", "Support"),
    ("V. V. Shahin", "Jr. Mechanic (Electronics)", "vvshahin@ee.iitb.ac.in",
     "022-2576-4412 (O)", "", "Support"),
]


def _initials(name):
    parts = [p for p in name.replace("Prof.", "").replace("Dr.", "").split() if p and p[0].isalpha()]
    if not parts:
        return "WEL"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def _photo(name, src):
    if src:
        return '<img src="%s" alt="%s" loading="lazy">' % (src, name)
    return '<div class="person__initials">%s</div>' % _initials(name)


def _person(name, role, email, phone, src, cat=None):
    data = ' data-cat="%s"' % cat if cat else ""
    return """        <article class="person reveal"{data}>
          <div class="person__photo">{photo}</div>
          <div class="person__body">
            <h4>{name}</h4>
            <span class="person__role">{role}</span>
            <div class="person__contact">
              <div>{i_mail}<a href="mailto:{email}">{email}</a></div>
              <div>{i_phone}<span>{phone}</span></div>
            </div>
          </div>
        </article>""".format(data=data, photo=_photo(name, src), name=name, role=role,
                             email=email, phone=phone, i_mail=icon("mail"), i_phone=icon("phone"))


def _people_grid(rows, with_cat=False):
    return "\n".join(_person(*(r if with_cat else r[:5])) for r in rows)


# M.Tech research assistants currently working at WEL.
RESEARCH_ASSISTANTS = [
    ("Prayag Mohanty", "M.Tech EE6 (2027)", "24m1177@iitb.ac.in",
     "assets/img/people/prayag-mohanty.jpg",
     "Prayag completed his Bachelors in Electrical &amp; Electronics Engineering from BITS Pilani. "
     "His research interests include computer systems architecture, AI/ML inference accelerators, "
     "ML-assisted system design and reconfigurable computing."),
    ("Anubhav Bhura", "M.Tech EE7 (2027)", "24m1219@iitb.ac.in",
     "assets/img/people/anubhav-bhura.jpg",
     "Anubhav completed his B.Tech in Electrical Engineering from Shri Govindram Seksaria Institute "
     "of Technology and Science. His research interests lie in digital VLSI design and computer "
     "architecture."),
    ("Sachin Soneria", "M.Tech EE6 (2027)", "24m1178@iitb.ac.in",
     "assets/img/people/sachin-soneria.jpg",
     "Sachin completed his B.Tech in Electronics Engineering from K. J. Somaiya College of "
     "Engineering, Mumbai. He is interested in digital VLSI and embedded design."),
    ("Aatmaj Barbhaiya", "M.Tech EE2 (2027)", "aatmaj017@gmail.com",
     "assets/img/people/aatmaj-barbhaiya.jpg",
     "Aatmaj completed his B.E. in Electronics and Communication Engineering from L.D. College of "
     "Engineering. His research interests encompass accelerator architecture."),
]


def _ra_cards():
    out = []
    for name, batch, email, src, bio in RESEARCH_ASSISTANTS:
        out.append("""        <article class="person reveal">
          <div class="person__photo">{photo}</div>
          <div class="person__body">
            <h4>{name}</h4>
            <span class="person__role">{batch}</span>
            <p>{bio}</p>
            <div class="person__contact">
              <div>{i_mail}<a href="mailto:{email}">{email}</a></div>
            </div>
          </div>
        </article>""".format(photo=_photo(name, src), name=name, batch=batch, bio=bio,
                             email=email, i_mail=icon("mail")))
    return "\n".join(out)


# ===========================================================================
# PEOPLE - OVERVIEW
# ===========================================================================
PEOPLE_BODY = """  <section class="section">
    <div class="wrap">
      <div class="wrap-narrow reveal" style="width:100%;padding:0;margin:0 0 2.6rem">
        <p class="lead">WEL is a diverse and highly skilled team that blends academic excellence with
          hands-on technical expertise. The lab runs on a foundation of technical superintendents, system
          administrators, mechanics and project assistants who manage everything from embedded systems
          development and PCB design to equipment maintenance and logistics &mdash; alongside M.Tech
          research assistants who bring deep domain knowledge across different areas.</p>
      </div>

      <div class="section-head reveal">
        <span class="eyebrow">Faculty</span>
        <h2>Faculty associated with WEL</h2>
      </div>
      <div class="grid g4">
{faculty}
      </div>
      <div class="btn-row mt2" style="margin-top:1.8rem">
        <a class="btn btn--outline btn--sm" href="faculty.html">Faculty page</a>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Staff</span>
        <h2>The team that runs the lab</h2>
        <p>Technical, administrative and support staff across lab administration, procurement, hardware
          development, system administration and day-to-day teaching lab operations.</p>
      </div>
      <div class="grid g4">
{staff}
      </div>
      <div class="btn-row mt2" style="margin-top:1.8rem">
        <a class="btn btn--outline btn--sm" href="staff.html">Staff page with roles</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Research assistants</span>
        <h2>M.Tech research assistants</h2>
        <p>Research assistants work at WEL across digital design, computer architecture, embedded
          systems and accelerator design. They contribute to hardware development, course support and
          the lab's R&amp;D projects, and in turn get the run of a very well-equipped bench.</p>
      </div>
      <div class="grid g4">
{ras}
      </div>
      <div class="note mt2 reveal" style="margin-top:2.2rem">
        <strong>Interested in an RA or intern position at WEL?</strong>
        <a href="contact.html">Write to the lab</a>, or see the
        <a href="programs.html#internships">internships section</a>.
      </div>
    </div>
  </section>
""".format(faculty=_people_grid(FACULTY), staff=_people_grid(STAFF[:4]), ras=_ra_cards())


# ===========================================================================
# FACULTY
# ===========================================================================
FACULTY_BODY = """  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Faculty members</span>
        <h2>Faculty associated with the lab</h2>
        <p>Faculty who oversee the Wadhwani Electronics Laboratory and the courses conducted in it.</p>
      </div>
      <div class="grid g4">
{faculty}
      </div>
      <div class="note mt2 reveal" style="margin-top:2.2rem">
        The wider set of faculty who use WEL for courses and projects is listed with the
        <a href="https://www.ee.iitb.ac.in/web/people/faculty/" target="_blank" rel="noopener">Department of
        Electrical Engineering</a>.
      </div>
    </div>
  </section>
""".format(faculty=_people_grid(FACULTY))


# ===========================================================================
# STAFF
# ===========================================================================
STAFF_BODY = """  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Staff members</span>
        <h2>Technical, administrative and support staff</h2>
        <p>The team responsible for lab administration and procurement, development of new hardware
          platforms and experiments, planning and execution of lab courses, outreach programs, systems
          and network, and day-to-day operations.</p>
      </div>

      <div class="filters reveal" data-filter-group data-filter-target=".person[data-cat]">
        <button class="filter is-active" data-filter="all">Everyone</button>
        <button class="filter" data-filter="Technical">Technical</button>
        <button class="filter" data-filter="Administration">Administration</button>
        <button class="filter" data-filter="Support">Support</button>
      </div>

      <div class="grid g4">
{staff}
      </div>
    </div>
  </section>

  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="table-wrap reveal">
        <table>
          <thead><tr><th>Name</th><th>Position</th><th>Email</th><th>Contact</th></tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
    </div>
  </section>
"""


def _staff_rows():
    out = []
    for name, role, email, phone, _src, _cat in STAFF:
        out.append('            <tr><td>%s</td><td>%s</td><td><a href="mailto:%s">%s</a></td><td>%s</td></tr>'
                   % (name, role, email, email, phone))
    return "\n".join(out)


STAFF_BODY = STAFF_BODY.format(staff=_people_grid(STAFF, with_cat=True), rows=_staff_rows())


# ===========================================================================
# GALLERY
# ===========================================================================
CAT_LABELS = {
    "EDL project": "EDL Projects",
    "NPTEL": "NPTEL Workshops",
    "guest visit": "Guest Visits",
    "WEL Facilities": "Facilities",
    "School Workshop": "School Workshops",
    "Research product": "Research Products",
}
CAT_ORDER = ["EDL project", "NPTEL", "guest visit", "WEL Facilities", "School Workshop", "Research product"]


def _gallery():
    path = os.path.join(HERE, "gallery_manifest.json")
    with open(path, encoding="utf-8") as fh:
        items = json.load(fh)

    figs = []
    for it in items:
        cat = it["cat"]
        label = CAT_LABELS.get(cat, cat)
        figs.append(
            '        <figure data-cat="{label}" data-full="assets/img/gallery/{f}">'
            '<img src="assets/img/gallery/thumbs/{f}" alt="{label} at WEL" loading="lazy"></figure>'
            .format(label=label, f=it["file"])
        )

    present = [c for c in CAT_ORDER if any(i["cat"] == c for i in items)]
    chips = ['<button class="filter is-active" data-filter="all">All photos</button>']
    for c in present:
        chips.append('<button class="filter" data-filter="%s">%s</button>'
                     % (CAT_LABELS.get(c, c), CAT_LABELS.get(c, c)))
    return "\n".join(figs), "\n        ".join(chips), len(items)


_figs, _chips, _count = _gallery()

GALLERY_BODY = """  <section class="section">
    <div class="wrap">
      <div class="filters reveal" data-filter-group data-filter-target=".gallery figure">
        {chips}
      </div>

      <div class="gallery reveal">
{figs}
      </div>
    </div>
  </section>

  <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photograph viewer">
    <button class="lightbox__close" id="lightboxClose" aria-label="Close">&times;</button>
    <button class="lightbox__nav lightbox__nav--prev" id="lightboxPrev" aria-label="Previous photograph">{prev}</button>
    <img id="lightboxImg" alt="">
    <button class="lightbox__nav lightbox__nav--next" id="lightboxNext" aria-label="Next photograph">{next}</button>
    <div class="lightbox__caption" id="lightboxCap"></div>
  </div>
""".format(chips=_chips, figs=_figs, prev=icon("prev"), next=icon("next"))


PAGES = [
    {
        "file": "people.html", "nav": "people.html", "sub": "people.html",
        "title": "People | Wadhwani Electronics Laboratory",
        "desc": "Faculty, technical staff, administration and research assistants at the Wadhwani "
                "Electronics Laboratory, IIT Bombay.",
        "hero": page_hero("People",
                          "A diverse and highly skilled team blending academic excellence with hands-on "
                          "technical expertise.",
                          [("People", "people.html")],
                          "assets/img/site/wel1-lab.jpeg"),
        "body": PEOPLE_BODY,
    },
    {
        "file": "faculty.html", "nav": "people.html", "sub": "faculty.html",
        "title": "Faculty Members | Wadhwani Electronics Laboratory",
        "desc": "Faculty members associated with the Wadhwani Electronics Laboratory, Department of "
                "Electrical Engineering, IIT Bombay.",
        "hero": page_hero("Faculty Members",
                          "Faculty who oversee the lab and the courses conducted in it.",
                          [("People", "people.html"), ("Faculty Members", "faculty.html")],
                          "assets/img/site/wel-lab.png"),
        "body": FACULTY_BODY,
    },
    {
        "file": "staff.html", "nav": "people.html", "sub": "staff.html",
        "title": "Staff Members | Wadhwani Electronics Laboratory",
        "desc": "Technical, administrative and support staff at the Wadhwani Electronics Laboratory, "
                "IIT Bombay, with roles and contact details.",
        "hero": page_hero("Staff Members",
                          "The technical, administrative and support team that keeps the lab running.",
                          [("People", "people.html"), ("Staff Members", "staff.html")],
                          "assets/img/site/work-stations.jpeg"),
        "body": STAFF_BODY,
    },
    {
        "file": "gallery.html", "nav": "gallery.html", "sub": None,
        "title": "WEL Gallery | Wadhwani Electronics Laboratory",
        "desc": "Photographs from the Wadhwani Electronics Laboratory - EDL projects, NPTEL workshops, "
                "guest visits, school outreach and lab facilities.",
        "hero": page_hero("WEL Gallery",
                          "Lab sessions, projects, workshops, visits and the facilities themselves.",
                          [("WEL Gallery", "gallery.html")],
                          "assets/img/site/lab-sessions.jpg"),
        "body": GALLERY_BODY,
    },
]
