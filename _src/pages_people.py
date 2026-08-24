# -*- coding: utf-8 -*-
"""People (overview / faculty / staff) and the gallery.

Staff and research assistants render as flip cards: the front carries the
photo, name, role and contact details, and the back carries the bio.  Nothing
needed to contact someone is hidden behind the flip.
"""
import json
import os

from build import SITE, icon, page_hero, HERE

# ---------------------------------------------------------------------------
# Faculty.  (name, role, email, phone, photo, ee_profile_url)
# Profile links go to the Department of Electrical Engineering website.
# ---------------------------------------------------------------------------
FACULTY = [
    ("Prof. Rajbabu Velmurugan", "Lab In-charge", "rajbabu@ee.iitb.ac.in",
     "022-2576-7444 (O) / 022-2576-8444 (R)", "assets/img/people/rajbabu-velmurugan.png",
     "https://www.ee.iitb.ac.in/web/people/rajbabu-velmurugan/"),
    ("Prof. Rahul Singh", "Faculty member", "rahuls@ee.iitb.ac.in",
     "022-2576-7417 (O)", "assets/img/people/rahul-singh.jpg",
     "https://www.ee.iitb.ac.in/web/people/rahul-singh/"),
    ("Prof. Dwaipayan Mukherjee", "Faculty member", "dm@ee.iitb.ac.in",
     "022-2576-9426 (O)", "assets/img/people/dwaipayan-mukherjee.png",
     "https://www.ee.iitb.ac.in/web/people/dwaipayan-mukherjee/"),
    ("Prof. Arun S.", "Faculty member", "sarun@ee.iitb.ac.in",
     "022-2576-7413 (O)", "assets/img/people/arun-s.jpg",
     "https://www.ee.iitb.ac.in/web/people/arun-s/"),
    ("Prof. Apurba Laha", "Faculty member", "laha@ee.iitb.ac.in",
     "022-2576-9408 (O)", "assets/img/people/apurba-laha.png",
     "https://www.ee.iitb.ac.in/web/people/apurba-laha/"),
]

# ---------------------------------------------------------------------------
# Staff, grouped as the lab groups them.
# (name, role, email, phone, photo, bio)
# Bios come from the team page; phone numbers from the current staff listing.
# ---------------------------------------------------------------------------
STAFF_GROUPS = [
    ("Technical Team", "Technical", [
        ("Mahesh Ashok Bhaganagare", "Technical Officer", "mab@ee.iitb.ac.in",
         "022-2576-4412 / 4403 (O) &middot; 92264 19459 (M)",
         "assets/img/team/mahesh-bhaganagare.jpg",
         "Mahesh is the Senior Technical Superintendent at WEL. He is responsible for overall lab "
         "administration and procurement, development of new hardware platforms and experiments, "
         "resources and infrastructure planning and execution of lab courses, planning and execution "
         "of outreach programs, assistance in project development activities, guidance to research "
         "and teaching assistants, and assistance in infrastructure planning and setting up of new "
         "teaching and research labs and classrooms in the department. Mahesh is an IIT Bombay "
         "alumnus, having graduated with an M.Tech (Electronic Systems) from IIT Bombay."),
        ("Maheshwar Mangat", "Sr. Technical Superintendent", "maheshgm@ee.iitb.ac.in",
         "022-2576-4412 / 4409 (O) &middot; 96198 27670 (M)",
         "assets/img/team/maheshwar-mangat.jpg",
         "Maheshwar is Technical Superintendent at WEL, where he oversees the overall administration, "
         "development of new experiments and resource/infrastructure management of UG lab courses, "
         "development of portable lab kits, assistance in project development activities, and "
         "conducting workshops. Maheshwar holds a B.Tech (E&amp;TC) from Dr. Babasaheb Ambedkar "
         "Technological University and a PG Diploma in Embedded Systems and Industrial Automation. "
         "His main interest lies in PCB design, embedded systems design, programming, and "
         "industrial IoT."),
        ("Amit Shetye", "Sr. Technical Superintendent", "amits@ee.iitb.ac.in",
         "022-2576-4484 (O) &middot; 99202 45689 (M)",
         "assets/img/team/amit-shetye.jpg",
         "Amit is Technical Superintendent at WEL. He oversees all administration of lab courses. "
         "Additionally, he is involved in activities in the following domains: embedded systems, "
         "hardware description languages, PCB designing, and hardware testing and repairing. He is "
         "an IIT Bombay alumnus, having graduated with an M.Tech in Electronic Systems at IIT Bombay "
         "after acquiring a Bachelor of Engineering in E&amp;TC from Mumbai University."),
        ("Ankur Agarwal", "Jr. Technical Superintendent", "ankur_ee@iitb.ac.in",
         "022-2576-4409 (O) &middot; 99674 43616 (M)",
         "assets/img/team/ankur-agarwal.jpg",
         "Ankur is Technical Superintendent at WEL. He is involved in electronic product design, "
         "embedded system design, PCB design and assembly, 3D modelling, and fabrication. He has "
         "completed his M.Des. in Electronic Systems from the Indian Institute of Information "
         "Technology Design and Manufacturing, Kancheepuram. He is working on two research projects, "
         "codenamed PicoIRIS and iPEC."),
        ("Yadnyik Pandurang Sonalkar", "Technical Superintendent", "yadnyik.sonalkar@iitb.ac.in",
         "022-2576-4412 (O)",
         "assets/img/team/yadnyik-sonalkar.jpg",
         "Yadnyik is a Technical Superintendent. He is involved in embedded software development and "
         "PCB fabrication."),
    ]),
    ("Research &amp; Development Team", "Research", [
        ("Sadanand Sahadev Sawant", "Sr. Mechanic (Electronics)", "ssawant@iitb.ac.in",
         "022-2576-4412 (O)",
         "assets/img/team/sadanand-sawant.jpg",
         "Sadanand handles day-to-day teaching lab activities of UG and PG students. His expertise is "
         "in soldering, testing, and repair and maintenance of measurement equipment, development "
         "boards, and modules. He has received a Diploma in Electronics from the Maharashtra State "
         "Board of Technical Education, Mumbai."),
        ("Suraj Suresh Sarfare", "Jr. Mechanic", "sarfaresuraj@ee.iitb.ac.in",
         "022-2576-4412 (O)",
         "assets/img/team/suraj-sarfare.jpg",
         "Suraj oversees the handling of the UG and PG teaching labs, operating and fault finding and "
         "repair and maintenance of electronic measuring instruments and development boards, "
         "maintaining the lab records, and keeping track of the lab equipment and boards. He has "
         "received a Diploma in Electronics from the Maharashtra State Board of Technical Education, "
         "Mumbai."),
    ]),
    ("System Administration", "Systems", [
        ("Nilesh Tukaram Sawant", "Sr. Technical Superintendent (Sysad)", "nilesh.t.sawant@ee.iitb.ac.in",
         "022-2576-4412 (O) &middot; 95946 20670 (M)",
         "assets/img/team/nilesh-sawant.jpg",
         "Nilesh is Technical Superintendent. He oversees all the system administration work at WEL. "
         "He is responsible for development of Linux drivers for WEL lab boards and development of "
         "barcode-based online verification of WEL lab electronics equipment stock. Nilesh has a "
         "Master's degree in Computer Application."),
    ]),
    ("Administration / Accounts Team", "Administration", [
        ("Varsha Suresh Ingle", "Sr. Project Assistant", "varshaingle@iitb.ac.in",
         "022-2576-4412 (O)",
         "assets/img/team/varsha-ingle.jpg",
         "Varsha is a Senior Project Assistant. She looks after office administration, preparing and "
         "processing purchase bills, procurement, the GeM process and day-to-day activity related to "
         "projects. Additionally, she is involved in stock data entry work. She completed a Bachelor "
         "of Arts in Economics."),
        ("Anil Ramrao Gawai", "Project Assistant (Administration)", "anilrg@ee.iitb.ac.in",
         "022-2576-4412 (O) &middot; 09220 087540 (M)",
         "assets/img/team/anil-gawai.jpg",
         "Anil is responsible for the day-to-day administration and accounting work, photography, and "
         "video shooting for lab sessions, workshops, and other events conducted in WEL and the EE "
         "department. Additionally, he assists in preparing financial statements for annual reports "
         "and handling general expenditures. Anil received a Bachelor of Commerce degree from Mumbai "
         "University."),
    ]),
    ("Supporting Staff", "Support", [
        ("Mangesh U. Ingle", "Project Assistant", "mangesh@ee.iitb.ac.in",
         "022-2576-4412 (O)",
         "assets/img/team/mangesh-ingle.jpg",
         "Mangesh is a Project Assistant. He is involved in testing teaching lab boards, modules, ICs, "
         "electronic components, accessories, and equipment; through-hole soldering, lab equipment "
         "testing, and PCB drilling. He has completed a Bachelor of Arts from YCMOU."),
        ("Sunil Sheshrao Raut", "Project Attendant", "sunilraut26@gmail.com",
         "022-2576-4412 (O)",
         "assets/img/team/sunil-raut.jpg",
         "Sunil is involved in testing activities such as teaching lab boards, modules, electronic ICs "
         "and components; through-hole soldering, lab equipment testing, board accessories testing, "
         "and dispatch-related work and follow-up. Sunil is SSC passed from the Maharashtra State "
         "Board."),
        ("Sandhya Samadhan Birare", "Lab Attendant", "sandhyabirare1980@gmail.com",
         "022-2576-4412 (O)",
         "assets/img/team/sandhya-birare.jpg",
         "Sandhya is a Lab Attendant. She is involved in electronic component and IC testing and "
         "sorting, equipment probes and accessories testing, inward and outward entries, dispatch "
         "work and follow-up with other sections. Sandhya is HSC passed in Arts from the Maharashtra "
         "State Board."),
        ("Vijay Vilas Patil", "Project Assistant", "vijaypatil4045@gmail.com",
         "022-2576-4412 (O)",
         "assets/img/team/vijay-patil.jpg",
         "Vijay is a Project Assistant. He is involved in testing and checking of the Krypton board, "
         "digital multimeter, arbitrary function generator, and power supply. He has completed his "
         "Bachelor of Arts."),
    ]),
]

STAFF_FLAT = [m for _title, _cat, members in STAFF_GROUPS for m in members]

# ---------------------------------------------------------------------------
# LinkedIn profiles, keyed by the exact name used above.
#
# Neither the old team page nor the current site publishes these - the old
# site's "View Profile" buttons all pointed at an empty "http://" - so this
# starts empty on purpose rather than with guessed URLs. Add a line and the
# LinkedIn link appears on the back of that person's card; leave someone out
# and their card simply omits it.
#
#   "Amit Shetye": "https://www.linkedin.com/in/amit-shetye-xxxx/",
# ---------------------------------------------------------------------------
LINKEDIN = {
    "Prayag Mohanty": "https://www.linkedin.com/in/prayag-mohanty/",
    "Anubhav Bhura": "https://www.linkedin.com/in/anubhavbhura13",
    "Sachin Soneria": "https://www.linkedin.com/in/sachin-soneria",
    "Aatmaj Barbhaiya": "https://www.linkedin.com/in/aatmajb/",
    "Shanthan Rao Pinninti": "https://www.linkedin.com/in/shanthan-rao-a7a4601a8/",
    "Adisha P V": "https://www.linkedin.com/in/adisha-p-v-6b42091ab",
    "Nikita Rajpurohit": "https://www.linkedin.com/in/nikita-rajpurohit-7291131a6",
    "Utkarsh Shukla": "https://www.linkedin.com/in/usin",
    "Vevinya A": "https://www.linkedin.com/in/vevinya-a-0002641aa/",
    "Navaneeth C": "https://www.linkedin.com/in/nvneethc",
}

# ---------------------------------------------------------------------------
# M.Tech research assistants.  (name, batch, email, photo, bio)
# ---------------------------------------------------------------------------
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
    ("Shanthan Rao Pinninti", "M.Tech EE7 (2027)", "shanthanrao078@gmail.com",
     "assets/img/team/shantan-pinninti.png",
     "Shanthan completed his B.Tech from CVR College of Engineering. His research interests lie at "
     "the intersection of semiconductor devices and circuit design, with a focus on CMOS technology, "
     "low-power VLSI circuits, and device-circuit co-design."),
    ("Adisha P V", "M.Tech EE7 (2027)", "24m1221@iitb.ac.in",
     "assets/img/team/adisha-pv.jpg",
     "Adisha completed her B.Tech in Electronics and Communication Engineering from Government "
     "Engineering College Wayanad. Her research interests are semiconductor devices and digital "
     "VLSI design."),
    ("Nikita Rajpurohit", "M.Tech EE7 (2027)", "24m1203@iitb.ac.in",
     "assets/img/team/nikita-rajpurohit.jpg",
     "Nikita completed her B.Tech in Electrical Engineering from Engineering College Bikaner. Her "
     "research interests are analog circuits and devices."),
    ("Utkarsh Shukla", "M.Tech EE6 (2027)", "24m1171@iitb.ac.in",
     "assets/img/team/utkarsh-shukla.jpg",
     "Utkarsh completed his B.Tech in Electrical Engineering from MMMUT Gorakhpur. His research "
     "interests are analog and mixed-signal design."),
    ("Vevinya A", "M.Tech EE6 (2027)", "vevinyagifty@gmail.com",
     "assets/img/team/vevinya-a.jpg",
     "Vevinya completed her B.Tech in Electronics and Communication Engineering from MEPCO Schlenk "
     "Engineering College. Her research interests are processor design, digital circuit design and "
     "VLSI design."),
    ("Navaneeth C", "M.Tech EE1 (2027)", "nvneethc@gmail.com",
     "assets/img/team/navaneeth-c.jpg",
     "Navaneeth completed his B.Tech at TKM College of Engineering. His research interests are "
     "wireless communication and the capacity of wireless channels."),
]


# ===========================================================================
# Card builders
# ===========================================================================
def _initials(name):
    parts = [p for p in name.replace("Prof.", "").replace("Dr.", "").split() if p and p[0].isalpha()]
    if not parts:
        return "WEL"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def _photo(name, src, cls="person__photo"):
    inner = ('<img src="%s" alt="%s" loading="lazy">' % (src, name) if src
             else '<div class="person__initials">%s</div>' % _initials(name))
    return '<div class="%s">%s</div>' % (cls, inner)


def _faculty_card(name, role, email, phone, src, profile):
    """Faculty card - the whole card links to their EE department profile."""
    return """        <a class="person reveal" href="{profile}" target="_blank" rel="noopener">
          {photo}
          <div class="person__body">
            <h4>{name}</h4>
            <span class="person__role">{role}</span>
            <div class="person__contact">
              <div>{i_mail}<span>{email}</span></div>
              <div>{i_phone}<span>{phone}</span></div>
              <div style="margin-top:.45rem"><span class="arrow-link" style="font-size:.76rem">EE profile</span></div>
            </div>
          </div>
        </a>""".format(profile=profile, photo=_photo(name, src), name=name, role=role,
                       email=email, phone=phone, i_mail=icon("mail"), i_phone=icon("phone"))


def _flip_card(name, role, email, phone, src, bio, cat=None, team=""):
    """Flip card: photo, name and role on the front; bio and contact on the back.

    `team` puts a badge on the photo, which lets every staff member sit in one
    continuous grid instead of a separate headed section per team - small teams
    no longer leave most of a row empty.
    """
    data = ' data-cat="%s"' % cat if cat else ""
    badge = '<span class="flipcard__team">%s</span>' % team if team else ""
    back_team = '<span class="flipcard__team-back">%s</span>' % team if team else ""

    lines = ['<div>%s<a href="mailto:%s">%s</a></div>' % (icon("mail"), email, email)]
    if phone:
        lines.append('<div>%s<span>%s</span></div>' % (icon("phone"), phone))
    if LINKEDIN.get(name):
        lines.append(
            '<div class="flipcard__social">'
            '<a class="social-icon" href="%s" target="_blank" rel="noopener" '
            'aria-label="%s on LinkedIn" title="%s on LinkedIn">%s</a>'
            '</div>' % (LINKEDIN[name], name, name, icon("linkedin")))

    return """        <div class="flipcard reveal" tabindex="0" role="button" aria-label="{name}, {role}. Activate to read their biography and contact details."{data}>
          <div class="flipcard__inner">
            <div class="flipcard__face flipcard__front">
              {photo}
              {badge}
              <span class="flipcard__hint" aria-hidden="true">i</span>
              <div class="flipcard__id">
                <h4>{name}</h4>
                <span class="person__role">{role}</span>
              </div>
            </div>
            <div class="flipcard__face flipcard__back">
              <h4>{name}</h4>
              <span class="person__role">{role}</span>
              {back_team}
              <p>{bio}</p>
              <div class="flipcard__contact">
                {contact}
              </div>
            </div>
          </div>
        </div>""".format(name=name, role=role, data=data, badge=badge, back_team=back_team,
                         photo=_photo(name, src, "flipcard__photo"),
                         contact="\n                ".join(lines), bio=bio)


def _faculty_grid():
    return "\n".join(_faculty_card(*f) for f in FACULTY)


def _staff_grid():
    """Every staff member in one grid, ordered by team, each card badged with
    its team. Keeps the grouping visible without a headed section per team."""
    cards = []
    for _title, cat, members in STAFF_GROUPS:
        for n, r, e, p, s, b in members:
            cards.append(_flip_card(n, r, e, p, s, b, cat=cat, team=cat))
    return "\n".join(cards)


def _staff_filters():
    chips = ['<button class="filter is-active" data-filter="all">Everyone</button>']
    for _title, cat, members in STAFF_GROUPS:
        chips.append('<button class="filter" data-filter="%s">%s <em>%d</em></button>'
                     % (cat, cat, len(members)))
    return ('      <div class="filters reveal" data-filter-group data-filter-target=".flipcard[data-cat]">\n'
            '        %s\n      </div>' % "\n        ".join(chips))


def _ra_cards():
    return "\n".join(_flip_card(n, b_, e, "", s, bio) for n, b_, e, s, bio in RESEARCH_ASSISTANTS)


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
        <p>Each card opens that faculty member's profile on the Department of Electrical Engineering
          website.</p>
      </div>
      <div class="grid g4">
{faculty}
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Staff</span>
        <h2>The team that runs the lab</h2>
        <p>Lab administration and procurement, development of new hardware platforms and experiments,
          planning and execution of lab courses, outreach programs, systems and network, and
          day-to-day operations. Hover over a card &mdash; or tap it &mdash; to read what each person
          does and how to reach them.</p>
      </div>

{staff_filters}
      <div class="grid g4">
{staff_grid}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Research assistants</span>
        <h2>M.Tech research assistants</h2>
        <p>Research assistants work at WEL across digital design, computer architecture, embedded
          systems, semiconductor devices and accelerator design. Hover over a card &mdash; or tap it
          &mdash; to read more.</p>
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
""".format(faculty=_faculty_grid(), staff_filters=_staff_filters(),
           staff_grid=_staff_grid(), ras=_ra_cards())


# ===========================================================================
# FACULTY
# ===========================================================================
FACULTY_BODY = """  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Faculty members</span>
        <h2>Faculty associated with the lab</h2>
        <p>Faculty who oversee the Wadhwani Electronics Laboratory and the courses conducted in it.
          Each card opens that faculty member's profile on the Department of Electrical Engineering
          website.</p>
      </div>
      <div class="grid g4">
{faculty}
      </div>
      <div class="note mt2 reveal" style="margin-top:2.2rem">
        The wider set of faculty who use WEL for courses and projects is listed with the
        <a href="https://www.ee.iitb.ac.in/web/people/" target="_blank" rel="noopener">Department of
        Electrical Engineering</a>. Faculty teaching individual lab courses are listed on each
        <a href="teaching-labs.html">course page</a>.
      </div>
    </div>
  </section>
""".format(faculty=_faculty_grid())


# ===========================================================================
# STAFF
# ===========================================================================
STAFF_BODY = """  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Staff members</span>
        <h2>The team that runs the lab</h2>
        <p>Lab administration and procurement, development of new hardware platforms and experiments,
          planning and execution of lab courses, outreach programs, systems and network, and
          day-to-day operations. Hover over a card &mdash; or tap it &mdash; to read what each person
          does.</p>
      </div>

{staff_filters}
      <div class="grid g4">
{staff_grid}
      </div>
    </div>
  </section>
"""

STAFF_BODY = STAFF_BODY.format(staff_filters=_staff_filters(), staff_grid=_staff_grid())


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
        label = CAT_LABELS.get(it["cat"], it["cat"])
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
        "desc": "Technical, research, systems, administration and support staff at the Wadhwani "
                "Electronics Laboratory, IIT Bombay, with roles, biographies and contact details.",
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
