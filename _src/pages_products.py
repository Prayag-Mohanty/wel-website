# -*- coding: utf-8 -*-
"""A detail page per achievement, reached from the Read more button on each card.

Content comes from the lab's own infographic posters for Nirmiti, WEL PCR and
ACPAD, and from the published paper for QMagPi. Each page links on to the
authoritative source rather than pretending to be it.

To add a product: append to PRODUCTS. `card` is what the achievements page
shows; `body` is the detail page.
"""
from build import icon, page_hero


def _sections(blocks):
    """blocks: list of (heading, [paragraph or <ul>...], ) rendered as prose."""
    out = []
    for heading, paras in blocks:
        out.append("      <h2>%s</h2>" % heading)
        for p in paras:
            out.append("      %s" % p if p.lstrip().startswith("<") else "      <p>%s</p>" % p)
    return "\n".join(out)


def _poster(src, caption):
    return """  <section class="section section--tight">
    <div class="wrap">
      <figure class="course-figure reveal" style="max-width:860px">
        <a href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{cap}" loading="lazy"></a>
        <figcaption>{cap} &mdash; open the full poster</figcaption>
      </figure>
    </div>
  </section>
""".format(src=src, cap=caption)


def _links(items):
    if not items:
        return ""
    lis = "\n".join(
        '            <li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (url, label)
        for label, url in items)
    return """  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Go deeper</span>
        <h2>Sources and further reading</h2>
      </div>
      <div class="reveal">
        <ul class="res-list">
{lis}
        </ul>
      </div>
    </div>
  </section>
""".format(lis=lis)


def _foot():
    return """  <section class="section section--tight">
    <div class="wrap">
      <div class="btn-row reveal">
        <a class="btn btn--outline" href="achievements.html">All achievements</a>
        <a class="btn btn--outline" href="made-in-wel.html">Boards made in WEL</a>
        <a class="btn btn--outline" href="contact.html">Talk to us</a>
      </div>
    </div>
  </section>
"""


# ===========================================================================
PRODUCTS = [
    # ---------------------------------------------------------------- Nirmiti
    {
        "slug": "nirmiti",
        "name": "Nirmiti",
        "tagline": "Making a difference",
        "blurb": "Making electronics affordable, simple and language-independent &mdash; from "
                 "schoolchildren to engineers and hobbyists.",
        "tag": "Outreach",
        "meta": "Product developer: Vivekanand Dhakane",
        "card": "assets/img/site/nirmiti.jpg",
        "hero": "assets/img/site/nirmiti.jpg",
        "desc": "Nirmiti - an affordable, language-independent electronics learning platform started "
                "at WEL, IIT Bombay, funded by SINE under the DST Nidhi Prayas programme.",
        "blocks": [
            ("Where the idea came from", [
                "Vivekanand Dhakane, an M.Tech student at IIT Bombay, came up with the idea for "
                "Nirmiti during the first wave of the COVID-19 pandemic in 2020, at his hometown "
                "Shevgaon.",
                "He was looking for an affordable microcontroller to replace the high-cost Arduino he "
                "had used in earlier projects, and came across the <strong>STM8S003F3P6</strong>, a "
                "controller worth about &#8377;19. He started writing libraries for it, and that grew "
                "into the Nirmiti project.",
            ]),
            ("What Nirmiti is", [
                "An initiative to make electronics easy to learn, user-friendly, affordable and "
                "accessible for every student <strong>independent of their language</strong> &mdash; "
                "from school level to degree level, and for hobbyists too.",
                "<div class=\"note\"><strong>Funded by SINE, IIT Bombay</strong> under the Nidhi "
                "Prayas programme offered by the Department of Science and Technology, Government of "
                "India.</div>",
            ]),
            ("Hardware and software", [
                "<ul>"
                "<li><strong>Nirmiti Board V1.3</strong> &mdash; the core microcontroller board</li>"
                "<li><strong>Nirmiti Base Shield V1.3</strong> &mdash; the expansion board that "
                "carries sensors, motor drivers and displays</li>"
                "<li><strong>Nirmiti Blocks</strong> &mdash; a drag-and-drop graphical interface for "
                "building a program</li>"
                "<li><strong>Nirmiti IDE</strong> &mdash; a text editor in which the code is "
                "auto-generated from those blocks</li>"
                "</ul>",
                "A worked example is the <strong>Nirmiti remote-controlled car</strong>, driven from "
                "the Nirmiti Android app.",
            ]),
            ("Challenges and goals", [
                "The project ran into the global chip shortage and the rise in chip pricing, along "
                "with delays in the delivery of parts.",
                "<ul>"
                "<li>Commercialise the Nirmiti products</li>"
                "<li>Add more regional languages to the software</li>"
                "<li>Write a user manual for the software and hardware</li>"
                "<li>Promote Nirmiti through social media and workshops</li>"
                "</ul>",
            ]),
        ],
        "poster": ("assets/img/achievements/nirmiti-infographic.jpg",
                   "Nirmiti: origin, products, challenges and goals"),
        "links": [],
    },

    # ------------------------------------------------------------------ ACPAD
    {
        "slug": "acpad",
        "name": "ACPAD",
        "tagline": "The world's first electronic orchestra for acoustic guitar",
        "blurb": "A mountable, wireless, ultra-thin MIDI controller that puts hundreds of "
                 "instruments, effects and loops on the guitar itself.",
        "tag": "Alumni product",
        "meta": "Product developer: Amaldev V",
        "card": "assets/img/site/acpad.jpg",
        "hero": "assets/img/site/acpad.jpg",
        "desc": "ACPAD - the world's first wireless MIDI controller for acoustic guitar, developed "
                "with IIT Bombay graduates and funded on Kickstarter.",
        "blocks": [
            ("Where the idea came from", [
                "The idea for ACPAD was born in 2009, when <strong>Robin Sukroso</strong>, a Berlin "
                "musician, started experimenting by building his own devices and created a prototype "
                "that would let him perform the music he had envisioned.",
                "In 2013, when Robin visited India for one of his concerts, his guitar and prototype "
                "were accidentally damaged &mdash; and three graduate students from IIT Bombay, "
                "<strong>Amaldev V, Deepak Malani and Avinash Iyer</strong>, came to his rescue.",
                "What began as a repair mission led to the development of a mountable, wireless and "
                "very thin MIDI controller for the guitar.",
            ]),
            ("What it does", [
                "An easily attachable controller giving access to hundreds of instruments, sound "
                "effects and loops on the guitar itself, designed for everyone from hobbyists to "
                "performing artists.",
                "<ul>"
                "<li>Custom sound samples can be triggered</li>"
                "<li>Easy connectivity over a USB dongle and mini cable</li>"
                "<li>Sleek enough that it does not damp the acoustic guitar's sound</li>"
                "<li>Compatible with all digital audio workstations</li>"
                "</ul>",
            ]),
            ("Specifications", [
                "<ul class=\"specs\">"
                "<li><b>Adhesive</b><span>Sticky polymer mat</span></li>"
                "<li><b>Dimensions</b><span>300 mm &times; 365 mm</span></li>"
                "<li><b>Thickness</b><span>3.5 mm for the pad, 9 mm for the battery</span></li>"
                "<li><b>Battery life</b><span>4&ndash;5 hours, rechargeable over USB</span></li>"
                "</ul>",
            ]),
            ("ACPAD Online", [
                "The companion web interface offers <strong>25 presets and 200 sounds</strong>, "
                "keyboard instructions for a quick preview, and a tutorial series on YouTube.",
                "The project was <strong>successfully funded on Kickstarter</strong>.",
            ]),
        ],
        "poster": ("assets/img/achievements/acpad-infographic.jpg",
                   "ACPAD: origin, innovation, specifications and controls"),
        "links": [("ACPAD website", "https://acpad.com/")],
    },

    # ---------------------------------------------------------------- WEL PCR
    {
        "slug": "welpcr",
        "name": "WEL PCR",
        "tagline": "Low-cost molecular sensing for affordable diagnostics",
        "blurb": "A standalone PCR thermal cycler for DNA amplification, built for under "
                 "&#8377;10,000 and released as an open design.",
        "tag": "Open source",
        "meta": "Low-cost DNA thermal cycler",
        "card": "assets/img/site/welpcr.png",
        "hero": "assets/img/site/welpcr.png",
        "desc": "WEL PCR - a low-cost polymerase chain reaction thermal cycler for DNA amplification "
                "developed at the Wadhwani Electronics Laboratory, IIT Bombay.",
        "blocks": [
            ("Why it was built", [
                "The idea was born during the COVID pandemic, in an attempt to overcome the challenge "
                "of limited access to the reagents and chemicals needed for conventional RT-PCR "
                "testing.",
                "That situation prompted the team to think about how a basic molecular sensing tool "
                "like PCR remains out of reach for many students and researchers in India. Alongside "
                "several low-cost assays and sensors for DNA sensing, the lab developed "
                "<strong>WEL PCR</strong>, a convenient and inexpensive option for students and "
                "researchers.",
            ]),
            ("What makes it different", [
                "<ul>"
                "<li><strong>In-house design</strong> &mdash; the laser cutter and hand-held power "
                "tools in the lab are used for the mechanical assembly</li>"
                "<li><strong>Touchscreen display</strong> for real-time readout of live process "
                "parameters, so it does not need to be connected to a computer or mobile device to be "
                "configured and operated, unlike other PCRs</li>"
                "<li><strong>Thermal ramp rate comparable</strong> to commercially available PCRs</li>"
                "<li><strong>Bill of materials under &#8377;10,000</strong>, about USD 120 &mdash; far "
                "below conventional PCR machines</li>"
                "</ul>",
                "The design is inspired by OpenPCR, is open-source, and is made available to "
                "developers who want to assemble their own units.",
            ]),
            ("Where it fits", [
                "The workflow runs from sample collection &mdash; environmental samples, saliva, blood "
                "and plasma &mdash; through nucleic acid extraction and cDNA synthesis where RNA is "
                "the genomic material, then PCR amplification with electrochemical and optical "
                "sensing, to the result.",
                "Potential users include diagnostic labs, water testing labs, hospitals and research "
                "institutes.",
            ]),
            ("Goals", [
                "<ul>"
                "<li>Outreach to colleges and labs through WEL PCR</li>"
                "<li>Testing and validation of low-cost assays and DNA sensors</li>"
                "<li>Clinical validation of the technology with diagnostic laboratories</li>"
                "<li>Scaling up the team for wider impact</li>"
                "</ul>",
            ]),
        ],
        "poster": ("assets/img/achievements/welpcr-infographic.jpg",
                   "WEL PCR: overview, innovation, applications and goals"),
        "links": [],
    },

    # ----------------------------------------------------------------- QMagPi
    {
        "slug": "qmagpi",
        "name": "QMagPi",
        "tagline": "Quantum Magnetometer with Proportional-Integral control",
        "blurb": "A compact, portable magnetometer built on an ensemble of nitrogen-vacancy centres "
                 "in diamond, developed with the PQuest lab.",
        "tag": "Research instrument",
        "meta": "Developed with PQuest Lab, IIT Bombay",
        "card": "assets/img/site/qmagpi.jpg",
        "hero": "assets/img/site/qmagpi.jpg",
        "desc": "QMagPi - a compact, portable NV-centre magnetometer with closed-loop control, "
                "developed at PQuest lab in collaboration with WEL, IIT Bombay.",
        "blocks": [
            ("What it is", [
                "QMagPi &mdash; <strong>Quantum Magnetometer with Proportional-Integral control</strong> "
                "&mdash; is a compact and portable magnetometer based on an ensemble of "
                "nitrogen-vacancy (NV) centres in diamond. It was developed at the PQuest lab in "
                "collaboration with WEL.",
                "NV centres in diamond have been explored for a wide range of sensing applications "
                "over the last decade because of their unusual quantum properties. The work here is "
                "in making that capability small, portable and usable outside a specialised optics "
                "bench.",
            ]),
            ("Performance", [
                "<ul class=\"specs\">"
                "<li><b>Sensitivity</b><span>~10 nT/&radic;Hz, bandwidth normalised</span></li>"
                "<li><b>Linear dynamic range</b><span>200 &micro;T, a 20&times; improvement over the "
                "intrinsic range, without losing sensitivity</span></li>"
                "<li><b>Sensor head and electronics</b><span>fits in a 10 &times; 10 &times; 7 cm "
                "box</span></li>"
                "<li><b>Control electronics</b><span>30 &times; 25 &times; 5 cm</span></li>"
                "</ul>",
                "The dynamic range comes from closed-loop feedback that locks to the resonance "
                "frequency. The published work reports a detailed performance analysis through noise "
                "spectra, Allan deviation, and tracking of nanotesla-level magnetic fields in real "
                "time.",
            ]),
            ("Shown working", [
                "The team demonstrated the magnetometer by tracking, in real time, the movement of a "
                "lift car and the opening of its doors &mdash; measuring the projection of the "
                "magnetic field along one of the NV axes, at ambient temperature and humidity.",
            ]),
        ],
        "poster": None,
        "links": [
            ("Paper: High dynamic-range and portable magnetometer using ensemble nitrogen-vacancy "
             "centers in diamond (arXiv)", "https://arxiv.org/abs/2402.15748"),
        ],
    },

    # ----------------------------------------------------------------- inSPEC
    {
        "slug": "inspec",
        "name": "inSPEC CS100",
        "tagline": "Handheld rebar inspection for reinforced concrete",
        "blurb": "On-demand measurement of rebar diameter and cover thickness in reinforced concrete "
                 "structures, being commercialised through a SINE-incubated startup.",
        "tag": "Translational R&amp;D",
        "meta": "Commercialised by Nirixense Technologies Pvt. Ltd.",
        "card": "assets/img/site/inspec-cs100.jpg",
        "hero": "assets/img/site/inspec-cs100.jpg",
        "desc": "inSPEC CS100 - a handheld device for on-demand inspection and measurement of rebar "
                "diameter and cover thickness in reinforced concrete structures.",
        "blocks": [
            ("What it does", [
                "The inSPEC CS100 is a handheld device designed for on-demand inspection and "
                "measurement of <strong>rebar diameter and cover thickness</strong> in reinforced "
                "concrete structures.",
                "It is aimed at structural analysis work: repairs, renovations, inspections, and "
                "quality control of RCC structures &mdash; situations where you need to know what is "
                "inside the concrete without breaking into it.",
            ]),
            ("Where it is going", [
                "The device is being commercialised by <strong>Nirixense Technologies Pvt. Ltd.</strong>, "
                "a startup incubated at SINE, IIT Bombay.",
            ]),
        ],
        "poster": None,
        "links": [("inSPEC project page", "https://www.ee.iitb.ac.in/~stallur/inspec/")],
    },
]

PRODUCTS_BY_SLUG = {p["slug"]: p for p in PRODUCTS}


def _body(p):
    return """  <section class="section section--tight">
    <div class="wrap-narrow prose reveal">
{blocks}
    </div>
  </section>

{poster}{links}{foot}""".format(
        blocks=_sections(p["blocks"]),
        poster=_poster(*p["poster"]) if p["poster"] else "",
        links=_links(p["links"]),
        foot=_foot(),
    )


PAGES = []
for _p in PRODUCTS:
    PAGES.append({
        "file": "product-%s.html" % _p["slug"],
        "nav": "about.html", "sub": "achievements.html",
        "title": "%s | Wadhwani Electronics Laboratory" % _p["name"],
        "desc": _p["desc"],
        "hero": page_hero(_p["name"], _p["tagline"],
                          [("About", "about.html"), ("Achievements", "achievements.html"),
                           (_p["name"], "product-%s.html" % _p["slug"])],
                          _p["hero"]),
        "body": _body(_p),
    })
