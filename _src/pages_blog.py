# -*- coding: utf-8 -*-
"""Blog posts, each hosted here rather than linked out to the archived site.

To add a post: append an entry to POSTS with its own body HTML, and it appears
on blogs.html automatically.

  slug     -> file becomes blog-<slug>.html
  card     -> image used on the blogs listing
  hero     -> image behind the article's page hero
"""
from build import icon, page_hero

# ===========================================================================
# Online lab courses @ WEL - Prof. Siddharth Tallur, 20 May 2021
# ===========================================================================
ONLINE_LABS_BODY = """  <article class="section section--tight">
    <div class="wrap-narrow prose reveal">
      <p class="lead">While lecture courses could be moved to online mode with some effort,
        laboratory courses presented a formidable challenge. Given the duration over which
        laboratories would be inaccessible to students, there was a real danger that many students
        might go through their entire degree course without any hands-on lab experience at all. This
        needed an innovative solution, and in very short time indeed. Fortunately, the seeds for the
        solution were sown almost a decade ago, when WEL had developed dedicated boards for laboratory
        courses which students could take to their hostels and carry out experiments using nothing but
        these boards and their laptops.</p>

      <p>The COVID-19 pandemic continues to disrupt lives well into CY 2021. At the Department of
        Electrical Engineering at IIT Bombay, we recognised the impact of being away from campus on
        the learning experience for students when it comes to practical courses, and we set about
        thinking of ideas to offer students hands-on learning opportunities, despite the challenges.
        An idea for conducting labs in massive open online course (MOOC) mode emerged in October 2020,
        when the country was beginning to emerge from lockdown and companies were slowly resuming
        business.</p>

      <p>At the Wadhwani Electronics Lab, the groundwork for this experiment had been laid out many
        years ago, with in-house made lab kits being used by students to perform laboratory exercises
        in WEL. Three months before the commencement of the Spring 2020&ndash;21 semester, we set an
        ambitious target for ourselves, never attempted before in the history of the institute &mdash;
        <strong>to conduct two laboratory courses, digital systems and microcontrollers, in MOOC mode,
        by shipping the necessary hardware to students at their homes.</strong></p>

      <p>Back in October 2020, this meant that in the next three months WEL would need to get more
        than <strong>250 boards manufactured</strong>, test all hardware, and ship <strong>more than
        500 boards</strong> to students and teaching assistants all over India. The team at WEL
        sourced components from local and online vendors, got PCBs fabricated and explored several
        options for board partners to get the PCBs assembled. This required an immense amount of
        dedication, hard work and precise coordination to ensure that this massive project was
        completed in time.</p>
    </div>

    <div class="wrap">
      <div class="figure-grid reveal">
        <figure>
          <img src="assets/img/blog/kits-digital-systems.png" alt="Hardware kits for the digital systems lab, laid out for packing" loading="lazy">
          <figcaption>Hardware kits for digital systems</figcaption>
        </figure>
        <figure>
          <img src="assets/img/blog/kits-microcontrollers.png" alt="Hardware kits for the microcontrollers lab course" loading="lazy">
          <figcaption>Hardware kits for microcontrollers lab courses</figcaption>
        </figure>
      </div>
    </div>

    <div class="wrap-narrow prose reveal">
      <p>The WEL team rose to the challenge, and got all the hardware ready by December 2020. To avoid
        inconvenience to students who may run into software and PC/OS compatibility issues, the team
        also prepared <strong>bootable USB drives</strong>, sent to each student along with the kits.</p>

      <p>The courses commenced in the Spring 2020&ndash;21 semester and progressed smoothly. Hardware
        kits were sent to students via speed post well before the targeted deadline of 26 January 2021.
        Lab courses were operated on the MS Teams platform, with TAs and staff helping students resolve
        their doubts and queries and debug hardware issues live during the sessions, which would
        sometimes extend beyond the scheduled slot in the timetable. Pre-recorded video lectures and
        tutorials supplemented the content. <strong>Only a handful of boards &mdash; fewer than ten
        &mdash; had to be replaced in the entire semester.</strong></p>
    </div>

    <div class="wrap">
      <div class="figure-grid figure-grid--3 reveal">
        <figure>
          <img src="assets/img/blog/amit-soldering.png" alt="Amit soldering and testing a PCB for the microcontroller lab" loading="lazy">
          <figcaption>Amit soldering and testing a PCB for the microcontroller lab</figcaption>
        </figure>
        <figure>
          <img src="assets/img/blog/bootable-usb-drives.png" alt="Sandesh and Mahesh preparing bootable USB drives" loading="lazy">
          <figcaption>Sandesh (WEL RA) and Mahesh preparing and testing bootable USB drives with preloaded software</figcaption>
        </figure>
        <figure>
          <img src="assets/img/blog/final-checks.png" alt="Sadanand and Maheshwar performing final hardware checks" loading="lazy">
          <figcaption>Sadanand and Maheshwar performing final checks on hardware for the digital systems lab</figcaption>
        </figure>
        <figure>
          <img src="assets/img/blog/kits-ready-to-ship.png" alt="Packed kits stacked and ready for despatch" loading="lazy">
          <figcaption>Kits ready to be shipped</figcaption>
        </figure>
        <figure>
          <img src="assets/img/blog/wel-team.png" alt="The WEL team who prepared and shipped the kits" loading="lazy">
          <figcaption>The WEL team that worked behind the scenes to accomplish this mammoth task</figcaption>
        </figure>
      </div>
    </div>

    <div class="wrap-narrow prose reveal">
      <p>In the digital systems lab, problem statements were posted a few minutes before the
        commencement of the corresponding lab session, and students had to independently work on the
        problem statement during the lab slot, with TAs and staff available to answer questions and
        help with debugging. Two practical exams were also conducted flawlessly. The microcontroller
        lab course had students working on different questions of similar complexity in every lab
        turn. There was also a project component, which the students could work on independently using
        the hardware available with them.</p>

      <blockquote class="pullquote">
        <p>&hellip; in my opinion conducting remote labs using our indigenously designed and fabricated
          cards has been a huge success&hellip; there was a marked difference in student confidence
          about topics related to 8051 as compared to other processors which were not included in the
          lab. In informal discussions, many students appreciated access to the hardware.</p>
        <footer>Prof. Dinesh Sharma<span>Department of Electrical Engineering, IIT Bombay</span></footer>
      </blockquote>

      <p>While formal course feedback is awaited, one student had this to say about the exercise:</p>

      <blockquote class="pullquote">
        <p>The course was amazing. The effort put by the instructor and TA was exceptional. When the lab
          was announced to be held in an online sem I was upset that it wouldn't be fun as an offline
          lab. But it turned totally the other way. This was way beyond expectations of what I could do
          at home in an online lab. Everyone was considerate and helpful. The course didn't feel like a
          burden but was enjoyable. I am really grateful for making the otherwise boring life of only
          studying theory exciting with these really fun labs.</p>
        <footer>A student on the course<span>Spring 2020&ndash;21</span></footer>
      </blockquote>
    </div>

    <div class="wrap">
      <div class="figure-grid reveal">
        <figure>
          <img src="assets/img/blog/students-at-home.png" alt="Students working on lab exercises at home with WEL hardware" loading="lazy">
          <figcaption>Students working on laboratory courses at their homes, using hardware shipped from WEL</figcaption>
        </figure>
        <figure>
          <img src="assets/img/blog/video-demonstration.png" alt="Still from a video demonstrating hardware usage" loading="lazy">
          <figcaption>Video demonstration of the hardware usage</figcaption>
        </figure>
      </div>
    </div>

    <div class="wrap-narrow prose reveal">
      <p>Based on this experience of conducting online laboratory courses, WEL took up another novel
        initiative &mdash; extending this experience to non-IITB students through two summer workshops,
        one for each course, conducted in partnership with <strong>NPTEL</strong> in June&ndash;July
        2021. NPTEL reached out to institutes within the SWAYAM-NPTEL Local Chapter cohort for
        registrations. Through this pilot, we hope to lead by setting an example, and help transform
        the way Electrical Engineering is taught in India, with increased emphasis on hands-on active
        learning.</p>
    </div>

    <div class="wrap">
      <div class="figure-grid reveal">
        <figure>
          <img src="assets/img/blog/iitdh-tas-1.png" alt="IIT Dharwad teaching assistants working on a microcontroller lab kit" loading="lazy">
          <figcaption>IIT Dharwad TAs working on a microcontroller lab kit shipped by WEL</figcaption>
        </figure>
        <figure>
          <img src="assets/img/blog/iitdh-tas-2.png" alt="IIT Dharwad teaching assistants training on WEL hardware" loading="lazy">
          <figcaption>Training on the donated boards at IIT Dharwad</figcaption>
        </figure>
      </div>
    </div>

    <div class="wrap-narrow prose reveal">
      <p>Separately, we received a request from IIT Dharwad, through Prof. Naveen Kadayinti, an IIT
        Bombay alumnus, for establishing a similar mechanism for conducting a microcontrollers lab. WEL
        donated a few boards to enable IIT-DH TAs to get trained on them, and assisted with board
        fabrication and testing. WEL continues to work on developing more hardware and software
        resources to enable other courses to also be conducted in MOOC style, and we hope to soon be
        able to expand the scope of such activities.</p>
    </div>
  </article>

  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="grid g3">
        <a class="lcard reveal" href="made-in-wel.html"><span class="lcard__icon">{i_board}</span>
          <h3>The boards behind this</h3>
          <p>PT-51, Xen-10 and the rest of the hardware designed and manufactured at WEL.</p></a>
        <a class="lcard reveal" href="programs.html#workshops"><span class="lcard__icon">{i_spark}</span>
          <h3>Workshops with NPTEL</h3>
          <p>The outreach programme this pilot grew into, now reaching 400+ colleges.</p></a>
        <a class="lcard reveal" href="blogs.html"><span class="lcard__icon">{i_book}</span>
          <h3>More from the lab</h3>
          <p>Back to all posts.</p></a>
      </div>
    </div>
  </section>
""".format(i_board=icon("board"), i_spark=icon("spark"), i_book=icon("book"))


POSTS = [
    {
        "slug": "online-lab-courses",
        "title": "Online lab courses @ WEL",
        "date": "20 May 2021",
        "author": "Prof. Siddharth Tallur",
        "author_note": "then Faculty-in-charge, WEL",
        "summary": "A report on the first-of-their-kind online laboratory courses conducted in the "
                   "Spring 2020&ndash;21 semester, when WEL manufactured and shipped more than 500 "
                   "boards to students across India.",
        "card": "assets/img/blog/hero.png",
        "hero": "assets/img/blog/hero.png",
        "body": ONLINE_LABS_BODY,
    },
]


def _cards():
    out = []
    for p in POSTS:
        out.append("""        <article class="card reveal">
          <div class="card__media"><img src="{card}" alt="{title}" loading="lazy"></div>
          <div class="card__body">
            <div class="card__meta">{date} &middot; {author}</div>
            <h3>{title}</h3>
            <p>{summary}</p>
            <a class="arrow-link" href="blog-{slug}.html">Read the post</a>
          </div>
        </article>""".format(**p))
    return "\n".join(out)


BLOGS_BODY = """  <section class="section">
    <div class="wrap">
      <div class="grid g3">
{cards}
      </div>

      <div class="note mt2 reveal" style="margin-top:2.4rem">
        <strong>Writing for the lab?</strong> Reports, project write-ups and course retrospectives
        from students, research assistants and staff are welcome here. Send a draft to
        <a href="mailto:wel@ee.iitb.ac.in">wel@ee.iitb.ac.in</a> and it will be published on this page.
      </div>
    </div>
  </section>
""".format(cards=_cards())


PAGES = [{
    "file": "blogs.html", "nav": "about.html", "sub": "blogs.html",
    "title": "Blogs | Wadhwani Electronics Laboratory",
    "desc": "Reports and writing from the Wadhwani Electronics Laboratory, IIT Bombay.",
    "hero": page_hero("Blogs",
                      "Reports, retrospectives and writing from the lab.",
                      [("About", "about.html"), ("Blogs", "blogs.html")],
                      "assets/img/site/work-stations.jpeg"),
    "body": BLOGS_BODY,
}]

for _p in POSTS:
    PAGES.append({
        "file": "blog-%s.html" % _p["slug"],
        "nav": "about.html", "sub": "blogs.html",
        "title": "%s | Wadhwani Electronics Laboratory" % _p["title"],
        "desc": _p["summary"].replace("&ndash;", "-"),
        "hero": page_hero(
            _p["title"],
            "%s &middot; %s, %s" % (_p["date"], _p["author"], _p["author_note"]),
            [("About", "about.html"), ("Blogs", "blogs.html"),
             (_p["title"], "blog-%s.html" % _p["slug"])],
            _p["hero"]),
        "body": _p["body"],
    })
