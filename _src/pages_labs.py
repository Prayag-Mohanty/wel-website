# -*- coding: utf-8 -*-
"""Teaching labs (overview / autumn / spring) and the online request pages."""
from build import SITE, icon, page_hero, inventory_url, inventory_live

# ===========================================================================
# TEACHING LABS - OVERVIEW
# ===========================================================================
TEACHING_BODY = """  <section class="section">
    <div class="wrap split">
      <div class="split__media reveal"><img src="assets/img/site/lab-sessions.jpg" alt="Students in a WEL teaching lab" loading="lazy"></div>
      <div class="split__body reveal">
        <span class="eyebrow">Teaching labs in WEL</span>
        <h2>Every electronics lab course in the department</h2>
        <p>The Wadhwani Electronics Lab caters to all of the electronics lab courses conducted by the
          Department of Electrical Engineering. Every academic year, about four hundred students use the
          lab facilities for a regular laboratory course.</p>
        <p>Apart from regular courses, the lab also supports project work related to electronics,
          including embedded systems, as part of undergraduate or postgraduate projects.</p>
        <p>As part of the <strong>Electronics Design Lab</strong> course, students take up challenging
          projects and work on them for an entire semester, from design to prototyping. Several
          interesting projects are completed every year, as an academic requirement or as plain
          tinkering.</p>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">By semester</span>
        <h2>Courses running in WEL</h2>
        <p>Lab courses are split across the two semesters. Pick a semester to see the courses it runs.</p>
      </div>
      <div class="grid g2">
        <a class="lcard reveal" href="autumn-semester.html">
          <span class="lcard__icon">{i_book}</span>
          <h3>Autumn semester</h3>
          <p>EE 214 Digital Circuits Lab &middot; EE 236 Electronic Devices Lab &middot;
             EE 340 Communications Lab</p>
        </a>
        <a class="lcard reveal" href="spring-semester.html">
          <span class="lcard__icon">{i_book}</span>
          <h3>Spring semester</h3>
          <p>EE 230 Analog Circuits Lab &middot; EE 344 Electronics Design Lab-I &middot;
             EE 712 Embedded Systems Design Lab &middot; EE 616 Electronics Systems Design &middot;
             EE 337 Microprocessor</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">What a bench looks like</span>
        <h2>Roughly 100 identical setups</h2>
        <p>WEL has more than 5,000 sq. ft. dedicated to laboratory courses. These sections of the lab are
          equipped with about 100 identical setups, plus soldering stations, components and accessories
          for assembling circuit boards.</p>
      </div>
      <div class="grid g4">
        <div class="lcard reveal"><span class="lcard__icon">{i_scope}</span><h3>DSO</h3><p>Digital storage oscilloscope at every bench.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_scope}</span><h3>AFG</h3><p>Arbitrary function generator for stimulus.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_chip}</span><h3>Supply &amp; DMM</h3><p>Programmable power supply and digital multimeter.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_board}</span><h3>Networked PC</h3><p>Lab sheets, datasheets and internet access at the bench.</p></div>
      </div>
      <div class="note mt2 reveal" style="margin-top:2rem">
        <strong>Boards developed in-house.</strong> Alongside the instruments, the lab has several
        development boards designed at WEL for educational use. These boards are now used extensively
        both within IIT Bombay and at other colleges &mdash;
        <a href="made-in-wel.html">see what is made in WEL</a>.
      </div>
    </div>
  </section>
""".format(i_book=icon("book"), i_scope=icon("scope"), i_chip=icon("chip"), i_board=icon("board"))


# ===========================================================================
# SEMESTER PAGES
# ===========================================================================
def _courses(semester):
    """Course rows for a semester, each linking to its own detail page.

    The list comes straight from pages_courses.COURSES so a course only ever
    has to be described in one place.
    """
    from pages_courses import COURSES_BY_SEMESTER
    out = []
    for c in COURSES_BY_SEMESTER[semester]:
        out.append("""        <a class="course reveal" href="course-{slug}.html">
          <span class="course__code">{code}</span>
          <div>
            <h4>{name}</h4>
            <p>{blurb}</p>
            <span class="arrow-link">Course page</span>
          </div>
        </a>""".format(slug=c["slug"], code=c["code"], name=c["title"], blurb=c["blurb"]))
    return "\n".join(out)


def _semester_body(semester, other_label, other_href, note):
    return """  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Courses</span>
        <h2>Lab courses this semester</h2>
        <p>{note}</p>
      </div>
      <div class="grid" style="gap:.9rem">
{rows}
      </div>
      <div class="btn-row mt2" style="margin-top:2rem">
        <a class="btn btn--outline" href="{other_href}">{other_label}</a>
        <a class="btn btn--outline" href="teaching-labs.html">Teaching labs overview</a>
      </div>
    </div>
  </section>

  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="grid g3">
        <a class="lcard reveal" href="made-in-wel.html"><span class="lcard__icon">{i_board}</span>
          <h3>Boards used in these courses</h3><p>PT-51, Xen-10, the IQ Modulator and more, all made in WEL.</p></a>
        <a class="lcard reveal" href="instruments.html"><span class="lcard__icon">{i_scope}</span>
          <h3>Instruments at the bench</h3><p>Generators, oscilloscopes, analyzers and meters available in the lab.</p></a>
        <a class="lcard lcard--red reveal" href="inventory.html"><span class="lcard__icon">{i_box}</span>
          <h3>Need components?</h3><p>Search the stock and raise a request through the WEL Inventory portal.</p></a>
      </div>
    </div>
  </section>
""".format(rows=_courses(semester), other_label=other_label, other_href=other_href, note=note,
           i_board=icon("board"), i_scope=icon("scope"), i_box=icon("box"))


# ===========================================================================
# ONLINE REQUEST
# ===========================================================================

# Requests for boards and equipment are handled by the WEL Inventory app.
if inventory_live():
    _PORTAL_NOTE = """<div class="note">
          <strong>Boards, modules and equipment</strong> are requested through
          <a href="{app}" target="_blank" rel="noopener">WEL Inventory</a>, using the same team
          registration and approval flow as component stock.
        </div>""".format(app=SITE["inventory_app"])
else:
    _PORTAL_NOTE = """<div class="note note--red">
          <strong>The request portal is being moved.</strong> Board, module and equipment requests are
          handled by <a href="inventory.html">WEL Inventory</a>, which is not online yet. Until it is,
          write to <a href="mailto:{email}">{email}</a> and the lab staff will sort it out.
        </div>""".format(email=SITE["email"])


REQUEST_BODY = """  <section class="section">
    <div class="wrap">
      <div class="wrap-narrow reveal" style="width:100%;padding:0;margin:0 0 2.4rem">
        <p class="lead">Three kinds of request are handled online: access to special facilities,
          borrowing development boards and modules, and equipment loans. Requests are tracked, and stock
          is updated when a request is approved.</p>
        {portal_note}
      </div>

      <div class="grid g3">
        <div class="lcard reveal" id="special-facilities">
          <span class="lcard__icon">{i_flask}</span>
          <h3>Special facilities online request</h3>
          <p>Thermal and climate chambers, EMI/EMC test facility, PCB fabrication, 3D printing,
             laser cutting, milling and coil winding. Describe what you need and the expected duration.</p>
          <div class="btn-row" style="margin-top:1.2rem">
            <a class="btn btn--primary btn--sm" href="{facilities_form}" target="_blank" rel="noopener">Open the form {i_ext}</a>
            <a class="btn btn--outline btn--sm" href="advanced-facilities.html">See facilities</a>
          </div>
        </div>

        <div class="lcard reveal" id="dev-boards">
          <span class="lcard__icon">{i_board}</span>
          <h3>Development boards &amp; modules</h3>
          <p>Take development boards from WEL for a specific time period &mdash; PT-51, Xen-10, Krypton,
             the IQ Modulator and the module stock that goes with them.</p>
          <div class="btn-row" style="margin-top:1.2rem">
            <a class="btn btn--primary btn--sm" href="{inv}"{inv_target}>Request a board {i_ext_or_blank}</a>
            <a class="btn btn--outline btn--sm" href="made-in-wel.html">See boards</a>
          </div>
        </div>

        <div class="lcard reveal" id="equipment-loan">
          <span class="lcard__icon">{i_scope}</span>
          <h3>Equipment loan</h3>
          <p>Borrow instruments from WEL for a specific time period &mdash; generators, oscilloscopes,
             analyzers, meters and supplies, subject to availability.</p>
          <div class="btn-row" style="margin-top:1.2rem">
            <a class="btn btn--primary btn--sm" href="{inv}"{inv_target}>Request equipment {i_ext_or_blank}</a>
            <a class="btn btn--outline btn--sm" href="instruments.html">See instruments</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">How it works</span>
        <h2>From request to issue</h2>
      </div>
      <div class="grid g4">
        <div class="lcard reveal"><span class="lcard__icon">{i_people}</span><h3>1. Register</h3>
          <p>Register your project team once, with every member's name and roll number and one IITB email.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_search}</span><h3>2. Pick</h3>
          <p>Browse or search what you need, set the quantity and add it to your request cart.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_clip}</span><h3>3. Submit</h3>
          <p>Add a note describing the project and the period you need it for, then submit the request.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_box}</span><h3>4. Collect</h3>
          <p>Lab staff review it. On approval the stock is decremented and you collect from the lab.</p></div>
      </div>
      <div class="note mt2 reveal" style="margin-top:2rem">
        <strong>Component stock</strong> - resistors, capacitors, discrete devices, ICs, sensors, motors
        and displays - is handled through the <a href="inventory.html">WEL Inventory</a> portal,
        which uses the same team registration and approval flow.
      </div>
    </div>
  </section>
""".format(email=SITE["email"], portal_note=_PORTAL_NOTE, inv=inventory_url(),
           inv_target=(' target="_blank" rel="noopener"' if inventory_live() else ''),
           i_ext_or_blank=(icon("external") if inventory_live() else ''),
           facilities_form=SITE["facilities_form"],
           i_flask=icon("flask"), i_board=icon("board"), i_scope=icon("scope"), i_people=icon("people"),
           i_search=icon("search"), i_clip=icon("clipboard"), i_box=icon("box"), i_ext=icon("external"))


PAGES = [
    {
        "file": "teaching-labs.html", "nav": "teaching-labs.html", "sub": "teaching-labs.html",
        "title": "Teaching Labs in WEL | Wadhwani Electronics Laboratory",
        "desc": "WEL caters to all electronics lab courses run by the Department of Electrical "
                "Engineering at IIT Bombay, plus undergraduate and postgraduate project work.",
        "hero": page_hero("Teaching Labs in WEL",
                          "Every electronics lab course conducted by the Department of Electrical "
                          "Engineering runs here, alongside undergraduate and postgraduate project work.",
                          [("Teaching Labs", "teaching-labs.html")],
                          "assets/img/site/work-stations.jpeg"),
        "body": TEACHING_BODY,
    },
    {
        "file": "autumn-semester.html", "nav": "teaching-labs.html", "sub": "autumn-semester.html",
        "title": "Autumn Semester | Wadhwani Electronics Laboratory",
        "desc": "Lab courses running in WEL during the autumn semester - EE 214 Digital Circuits Lab, "
                "EE 236 Electronic Devices Lab and EE 340 Communications Lab.",
        "hero": page_hero("Autumn Semester",
                          "Lab courses conducted in WEL during the autumn semester.",
                          [("Teaching Labs", "teaching-labs.html"), ("Autumn Semester", "autumn-semester.html")],
                          "assets/img/site/lab-sessions.jpg"),
        "body": _semester_body(
            "Autumn", "Spring semester courses", "spring-semester.html",
            "Courses conducted in the Wadhwani Electronics Lab during the autumn semester. "
            "Course content and slot allocation are announced by the department each year."),
    },
    {
        "file": "spring-semester.html", "nav": "teaching-labs.html", "sub": "spring-semester.html",
        "title": "Spring Semester | Wadhwani Electronics Laboratory",
        "desc": "Lab courses running in WEL during the spring semester - EE 230, EE 344, EE 712, "
                "EE 616 and EE 337.",
        "hero": page_hero("Spring Semester",
                          "Lab courses conducted in WEL during the spring semester.",
                          [("Teaching Labs", "teaching-labs.html"), ("Spring Semester", "spring-semester.html")],
                          "assets/img/site/work-stations.jpeg"),
        "body": _semester_body(
            "Spring", "Autumn semester courses", "autumn-semester.html",
            "Courses conducted in the Wadhwani Electronics Lab during the spring semester. "
            "Course content and slot allocation are announced by the department each year."),
    },
    {
        "file": "online-request.html", "nav": "online-request.html",
        "sub": "online-request.html#special-facilities",
        "title": "Online Request | Wadhwani Electronics Laboratory",
        "desc": "Raise an online request for special facilities, development boards and modules, or an "
                "equipment loan from the Wadhwani Electronics Laboratory.",
        "hero": page_hero("Online Request",
                          "Special facilities, development boards and modules, and equipment loans - "
                          "all requested and tracked online.",
                          [("Online Request", "online-request.html")],
                          "assets/img/facilities/esd-workstation.jpeg"),
        "body": REQUEST_BODY,
    },
]
