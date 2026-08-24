# -*- coding: utf-8 -*-
"""Workshops - NPTEL, teacher training and community outreach.

NPTEL workshops run every year and highlights of each one go up on the WEL
YouTube channel, so each edition below carries its own highlights video. To add next year's
edition, put a new entry at the top of NPTEL_EDITIONS with its video IDs.

A video id is the part after watch?v= in the YouTube URL.
"""
from build import SITE, icon, page_hero


def _embed(video_id, title):
    """Responsive YouTube embed, on the no-cookie domain so viewers are not
    tracked unless they actually press play."""
    return """          <figure class="video">
            <div class="video-embed">
              <iframe src="https://www.youtube-nocookie.com/embed/{vid}" title="{title}"
                loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </div>
            <figcaption>{title}</figcaption>
          </figure>""".format(vid=video_id, title=title)


# ---------------------------------------------------------------------------
# NPTEL editions, newest first.
#   videos: (youtube id, title as it appears on the channel)
# ---------------------------------------------------------------------------
NPTEL_EDITIONS = [
    {
        "year": "2026",
        "dates": "",
        "tag": "Latest edition",
        "intro": [
            "The 2026 edition was the widest yet, running four separate courses that between them "
            "cover hardware digital design, device physics, analog design and embedded systems. "
            "Highlights from all four courses are below.",
        ],
        "courses": [
            "Digital Systems using hardware CPLD",
            "Electronic devices simulation using NGSPICE and analysis",
            "Analog circuits design: simulation lab",
            "Microcontroller systems &amp; applications: Pt-51 (8051 architecture)",
        ],
        "videos": [
            ("e0d6UX7uqOw", "NPTEL Workshop 2026 &mdash; Digital Systems Using Hardware CPLD"),
            ("pXf0HyV5XVs", "NPTEL Workshop 2026 &mdash; Electronic Devices Simulation Using NGSPICE and Analysis"),
            ("Vwu8l5C_kn8", "NPTEL Workshop 2026 &mdash; Analog Circuits Design: Simulation Lab"),
            ("Gv5aY6PEQXY", "NPTEL Workshop 2026 &mdash; Microcontroller Systems &amp; Applications: Pt-51"),
        ],
        "image": None,
        "quotes": [],
    },
    {
        "year": "2024",
        "dates": "",
        "tag": "",
        "intro": [
            "The 2024 edition again paired the two flagship hardware courses &mdash; digital design "
            "on the in-house Krypton CPLD board, and the microcontroller lab on the in-house PT-51. "
            "Highlights from both courses are below.",
        ],
        "courses": [
            "Digital system design and verification using the CPLD board (Krypton)",
            "Microcontroller lab on the Pt-51 (8051-based) board",
        ],
        "videos": [
            ("wwesYwzY3Yk", "Digital system design and verification using CPLD board (Krypton)"),
            ("Znody4SyLTM", "Microcontroller Lab on Pt-51 (8051-based) board"),
        ],
        "image": None,
        "quotes": [],
    },
    {
        "year": "2023",
        "dates": "",
        "tag": "",
        "intro": [
            "Two workshops ran in 2023, following the same awareness-plus-hands-on format: sessions "
            "introducing NPTEL and its certification courses, alongside laboratory work on WEL "
            "hardware.",
        ],
        "courses": [],
        "videos": [
            ("mYKpam4EUmw", "NPTEL Workshop 1, 2023"),
            ("5J1i1DoDHR8", "NPTEL Workshop 2, 2023"),
        ],
        "image": None,
        "quotes": [],
    },
    {
        "year": "2022",
        "dates": "4 &ndash; 15 July 2022",
        "tag": "",
        "intro": [
            "A two-week workshop conducted by WEL in association with NPTEL, focussed on skill "
            "development within the lab. <strong>99 students</strong> from local colleges enrolled, "
            "of whom <strong>more than 50 completed</strong> the programme and were certified.",
        ],
        "courses": [
            "Digital system design &amp; verification using CPLD",
            "Microcontroller lab using Pt-51",
        ],
        "videos": [
            ("RCApHkMnua4", "NPTEL Workshop 2022 at WEL"),
        ],
        "image": ("assets/img/workshops/nptel-2022-infographic.jpg",
                  "The 2022 workshop at a glance - operational model, participation and feedback"),
        "quotes": [
            ("I had a great time in the past two weeks; the workshop was paced very well, adequate "
             "content was covered &amp; all the TAs were extremely helpful &amp; patient.",
             "Diya Shetty", "Digital System Design and Verification using CPLD"),
            ("The experience was good; I liked the way lectures &amp; lab-work were going "
             "hand-in-hand. The problems designed in the lab sheets helped us learn the concepts in "
             "a better way.",
             "Suraj Chaudhary", "Microcontroller Lab based on Pt-51"),
            ("The co-ordinators are very supportive &amp; the guides are always ready to explain each "
             "concept from scratch. Overall experience was technically enjoyable.",
             "Himanshu Behera", "Digital System Design and Verification using CPLD"),
        ],
    },
    {
        "year": "2021",
        "dates": "28 June &ndash; 10 July 2021",
        "tag": "The first one",
        "intro": [
            "The pilot. Coming straight out of the online laboratory courses WEL had just run through "
            "the pandemic, this two-week workshop extended that experience to students outside "
            "IIT Bombay for the first time, in association with NPTEL.",
            "Students enrolled through NPTEL, WEL shipped them lab kits, sessions ran online with "
            "both theory and practical components, students demonstrated their experiments for "
            "assessment, and those who completed it were certified.",
        ],
        "courses": [
            "Digital system design &amp; verification using CPLD",
            "Microcontroller lab based on Pt-51",
        ],
        "videos": [],
        "image": ("assets/img/workshops/nptel-2021-infographic.jpg",
                  "The 2021 pilot at a glance - operational model and the kits that were shipped"),
        "quotes": [],
    },
]


def _edition(e):
    tag = ('<span class="card__tag">%s</span>' % e["tag"]) if e["tag"] else ""
    dates = ('<div class="card__meta">%s</div>' % e["dates"]) if e["dates"] else ""
    intro = "\n".join("        <p>%s</p>" % p for p in e["intro"])

    courses = ""
    if e["courses"]:
        items = "\n".join("            <li>%s</li>" % c for c in e["courses"])
        courses = """        <p style="margin-bottom:.5rem"><strong>Courses offered</strong></p>
        <ul>
%s
        </ul>""" % items

    image = ""
    if e["image"]:
        src, cap = e["image"]
        image = """      <figure class="course-figure reveal" style="max-width:760px">
        <a href="%s" target="_blank" rel="noopener"><img src="%s" alt="%s" loading="lazy"></a>
        <figcaption>%s &mdash; open the full poster</figcaption>
      </figure>""" % (src, src, cap, cap)

    videos = ""
    if e["videos"]:
        vids = "\n".join(_embed(v, t) for v, t in e["videos"])
        videos = """      <div class="video-grid reveal">
%s
      </div>""" % vids

    quotes = ""
    if e["quotes"]:
        qs = []
        for text, who, course in e["quotes"]:
            qs.append("""        <blockquote class="pullquote" style="margin:0">
          <p>%s</p>
          <footer>%s<span>%s</span></footer>
        </blockquote>""" % (text, who, course))
        quotes = """      <div class="grid g3 reveal" style="margin-top:2rem">
%s
      </div>""" % "\n".join(qs)

    return """    <div class="workshop-year reveal" id="nptel-{year}">
      <div class="wrap-narrow prose" style="margin-bottom:1.6rem">
        {tag}
        <h3 style="font-size:clamp(1.5rem,2.6vw,2rem)">NPTEL Workshop {year}</h3>
        {dates}
{intro}
{courses}
      </div>
{image}
{videos}
{quotes}
    </div>
""".format(year=e["year"], tag=tag, dates=dates, intro=intro, courses=courses,
           image=image, videos=videos, quotes=quotes)


def _editions():
    return "\n".join(_edition(e) for e in NPTEL_EDITIONS)


def _year_nav():
    links = " ".join(
        '<a class="filter" href="#nptel-%s">%s</a>' % (e["year"], e["year"])
        for e in NPTEL_EDITIONS
    )
    return '<div class="filters reveal" style="margin-bottom:2.4rem">%s</div>' % links


WORKSHOPS_BODY = """  <section class="section section--tight">
    <div class="wrap">
      <div class="wrap-narrow reveal" style="width:100%;padding:0;margin:0 0 2.4rem">
        <p class="lead">The WEL brand has reached more than 400 colleges across India through
          workshops conducted over the years, training more than 2,000 teachers and students on
          hardware and lab content developed in the lab. Workshops fall into three kinds: the annual
          NPTEL programme, teacher training, and community outreach.</p>
      </div>
      <div class="stats">
        <div class="stat reveal"><b><span data-count="400" data-suffix="+">400+</span></b><span>Colleges reached</span></div>
        <div class="stat reveal"><b><span data-count="30" data-suffix="+">30+</span></b><span>Teacher training workshops</span></div>
        <div class="stat reveal"><b><span data-count="2500" data-suffix="+">2,500+</span></b><span>Teachers trained</span></div>
        <div class="stat reveal"><b><span data-count="5" data-suffix="">5</span></b><span>Years of NPTEL workshops</span></div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">NPTEL workshops</span>
        <h2>Run every year, with highlights from each</h2>
        <p>WEL hosts NPTEL workshops annually and publishes highlights from each one on the
          <a href="{youtube}" target="_blank" rel="noopener">WEL YouTube channel</a>. Every edition is
          below, newest first, with its highlights video.</p>
      </div>

      {year_nav}

      <div class="wrap-narrow prose reveal" style="width:100%;padding:0;margin:0 0 2.4rem">
        <div class="note">
          <strong>What an NPTEL awareness workshop is.</strong> The aim is to create maximum awareness
          among faculty members about NPTEL and its various initiatives. Sessions cover NPTEL and its
          features, NPTEL Online Certification courses, and the concept of the NPTEL Local Chapter.
          NPTEL and the host institute organise the workshop jointly, and the host invites two or
          three faculty members from colleges &mdash; both engineering institutions and arts and
          science colleges &mdash; within a radius of 150 km.
        </div>
      </div>

      <div class="grid g4 reveal" style="margin-bottom:3rem">
        <div class="lcard"><span class="lcard__icon">{i_people}</span><h3>1. Coordination</h3>
          <p>WEL shares the workshop details and brochure with NPTEL Madras through its associate at
             IIT Bombay.</p></div>
        <div class="lcard"><span class="lcard__icon">{i_book}</span><h3>2. Local colleges</h3>
          <p>NPTEL coordinates with associated local colleges, who in turn pass details to their
             students.</p></div>
        <div class="lcard"><span class="lcard__icon">{i_board}</span><h3>3. Hands-on sessions</h3>
          <p>The workshop runs at WEL, IIT Bombay, pairing lectures with lab work on hardware designed
             in the lab.</p></div>
        <div class="lcard"><span class="lcard__icon">{i_spark}</span><h3>4. Certification</h3>
          <p>Participants who complete the assessment are certified.</p></div>
      </div>

{editions}
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="split__media reveal"><img src="assets/img/workshops/teacher-training.jpg" alt="WEL staff speaking to a visiting college team" loading="lazy"></div>
      <div class="split__body reveal">
        <span class="eyebrow">Teacher training</span>
        <h2>2,500+ college teachers, 30+ workshops</h2>
        <p>WEL conducts teacher training workshops for various practical courses. More than 30
          workshops have been conducted for over 2,500 college teachers.</p>
        <p>WEL has also provided mentorship, kits and staff support to new IITs &mdash;
          <strong>IIT Gandhinagar, IIT Indore, IIT Dharwad and IIT Goa</strong> &mdash; for setting up
          electronics lab infrastructure. Kits developed in WEL have been supplied to IIT Hyderabad,
          IIT Delhi, IIIT Bangalore and IIT Guwahati.</p>
        <p>WEL has supported faculty training through the <strong>QIP</strong> and
          <strong>SMDP-IEP</strong> programmes, and enables colleges to establish electronics lab
          courses through support for curriculum and hardware.</p>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap split split--reverse">
      <div class="split__media reveal"><img src="assets/img/workshops/community-outreach.jpg" alt="School students at a WEL outreach workshop" loading="lazy"></div>
      <div class="split__body reveal">
        <span class="eyebrow">Community outreach</span>
        <h2>School students and visiting groups</h2>
        <p>WEL periodically conducts outreach workshops for school students and for students visiting
          IIT Bombay. WEL staff also conduct vocational training for non-teaching lab staff to advance
          their career development.</p>
        <p>Video resources based on experiments and projects designed at WEL are shared widely through
          the WEL <a href="{youtube}" target="_blank" rel="noopener">YouTube</a> and
          <a href="{linkedin}" target="_blank" rel="noopener">LinkedIn</a> pages, freely available to
          aid students and innovators in their projects.</p>
      </div>
    </div>
    <div class="wrap" style="margin-top:2.6rem">
      <div class="video-grid video-grid--one reveal">
{immersionx}
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>Want to attend or host a workshop?</h2>
        <p>Institutions, colleges and student groups interested in NPTEL workshops, teacher training
           or outreach programmes on WEL hardware and lab content are welcome to get in touch.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="contact.html">Talk to the lab</a>
          <a class="btn btn--ghost" href="{youtube}" target="_blank" rel="noopener">Watch on YouTube</a>
        </div>
      </div>
    </div>
  </section>
""".format(youtube=SITE["youtube"], linkedin=SITE["linkedin"], year_nav=_year_nav(),
           editions=_editions(),
           immersionx=_embed("gHk8K9ihgCQ",
                             "ImmersionX: Hands-On Electronics Workshop 2026, Grades 8&ndash;12"),
           i_people=icon("people"), i_book=icon("book"), i_board=icon("board"),
           i_spark=icon("spark"))


PAGES = [{
    "file": "workshops.html", "nav": "programs.html", "sub": "workshops.html",
    "title": "Workshops | Wadhwani Electronics Laboratory",
    "desc": "NPTEL workshops, teacher training and community outreach at the Wadhwani Electronics "
            "Laboratory, IIT Bombay - every edition with highlights from the workshop.",
    "hero": page_hero("Workshops",
                      "NPTEL workshops run every year, teacher training for college faculty, and "
                      "outreach for school students - with highlights from each one.",
                      [("Programs", "programs.html"), ("Workshops", "workshops.html")],
                      "assets/img/site/workshop-kv-powai.jpg"),
    "body": WORKSHOPS_BODY,
}]
