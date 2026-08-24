# -*- coding: utf-8 -*-
"""Home, About, Programs, Achievements, Blogs, Contact."""
from build import SITE, icon, page_hero

# ===========================================================================
# HOME
# ===========================================================================
HOME_HERO = """  <section class="hero">
    <div class="hero__bg"><img src="assets/img/site/homepage-hero.jpg" alt="" fetchpriority="high"></div>
    <div class="wrap hero__inner">
      <h1>Where electronics <em>lives.</em></h1>
      <p class="hero__sub">The <strong>Wadhwani Electronics Laboratory</strong> is the hub of electronics
        activity in the Department of Electrical Engineering, IIT Bombay &mdash; teaching labs, in-house
        hardware, rapid prototyping and advanced measurement, all under one roof.
        <em>Think it. Make it. Prove it.</em></p>
      <div class="btn-row">
        <a class="btn btn--red" href="resources.html">Explore our resources</a>
        <a class="btn btn--ghost" href="online-request.html">Raise an online request</a>
      </div>
      <div class="hero__meta">
        <div><b><span data-count="1700" data-suffix="+">1,700+</span></b><span>Students / year</span></div>
        <div><b><span data-count="10" data-suffix="+">10+</span></b><span>Lab courses</span></div>
        <div><b><span data-count="5000" data-suffix="+">5,000+</span></b><span>Sq. ft. of lab</span></div>
        <div><b><span data-count="400" data-suffix="+">400+</span></b><span>Colleges reached</span></div>
      </div>
    </div>
  </section>
"""

HOME_BODY = """  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">Quick access</span>
        <h2>What do you need today?</h2>
        <p>The lab serves students, research groups and faculty across the institute. Start here.</p>
      </div>
      <div class="grid g3">
        <a class="lcard reveal" href="teaching-labs.html">
          <span class="lcard__icon">{i_book}</span>
          <h3>Teaching Labs</h3>
          <p>Autumn and Spring semester lab courses, schedules and the hardware each course uses.</p>
        </a>
        <a class="lcard reveal" href="advanced-facilities.html">
          <span class="lcard__icon">{i_tool}</span>
          <h3>Advanced Facilities</h3>
          <p>Thermal and climate chambers, 3D printers, laser cutter, milling, coil winding, ESD benches.</p>
        </a>
        <a class="lcard reveal" href="made-in-wel.html">
          <span class="lcard__icon">{i_board}</span>
          <h3>Made in WEL Boards</h3>
          <p>PicoIRIS, PT-51, Xen-10, the IQ Modulator and QMagPi &mdash; designed and built in-house.</p>
        </a>
        <a class="lcard reveal" href="instruments.html">
          <span class="lcard__icon">{i_scope}</span>
          <h3>Instruments</h3>
          <p>Signal generators, oscilloscopes, analyzers, meters and high-voltage equipment.</p>
        </a>
        <a class="lcard lcard--red reveal" href="inventory.html">
          <span class="lcard__icon">{i_box}</span>
          <h3>WEL Inventory</h3>
          <p>Search component stock, add to a cart and raise a request as a project team.</p>
        </a>
        <a class="lcard lcard--red reveal" href="online-request.html">
          <span class="lcard__icon">{i_clip}</span>
          <h3>Online Requests</h3>
          <p>Special facilities, development boards and modules, and equipment loans.</p>
        </a>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap split">
      <div class="split__media reveal">
        <img src="assets/img/site/wel-lab.png" alt="Inside the Wadhwani Electronics Laboratory" loading="lazy">
      </div>
      <div class="split__body reveal">
        <span class="eyebrow">About WEL</span>
        <h2>One roof for the entire electronics activity in EE</h2>
        <p>Wadhwani Electronics Laboratory was inaugurated on <strong>12 February 2001</strong> in the
          Department of Electrical Engineering, IIT Bombay, supported through an endowment from our
          distinguished alumnus <strong>Dr. Romesh Wadhwani (EE 1969)</strong>.</p>
        <p>Many of the activities WEL runs today had not been possible earlier &mdash; at least not at
          the same scale &mdash; because of infrastructural limits, or simply because the various
          electronics activities were physically apart. WEL brought almost the entire electronics
          activity in EE under one umbrella, and the enthusiasm among students followed.</p>
        <p>More than <strong>1,700 students</strong> use WEL every year for laboratory courses and
          projects, on a large variety of microcontroller boards, CPLD/FPGA boards, logic analyzers,
          oscilloscopes, function generators and programmers &mdash; much of it designed in-house.</p>
        <a class="arrow-link" href="about.html">Read more about the lab</a>
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Our resources</span>
        <h2>Facilities built up over two decades</h2>
        <p>WEL has evolved from a lab that only ran curricular courses in 2001 into a hub for
          electronics activity, with state-of-the-art facilities for projects and product development.</p>
      </div>
      <div class="grid g4">
        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/madeinwel.png" alt="Boards designed and manufactured at WEL" loading="lazy"></div>
          <div class="card__body">
            <h3>Made in WEL</h3>
            <p>Course hardware designed and manufactured in-house for more than a decade.</p>
            <a class="arrow-link" href="made-in-wel.html">View boards</a>
          </div>
        </article>
        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/lab-sessions.jpg" alt="Students during a lab session" loading="lazy"></div>
          <div class="card__body">
            <h3>Instructional Labs</h3>
            <p>5,000+ sq. ft. and roughly 100 identical AFG / DSO / supply / DMM setups.</p>
            <a class="arrow-link" href="teaching-labs.html">See teaching labs</a>
          </div>
        </article>
        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/ell.jpeg" alt="Experiential Learning Laboratory" loading="lazy"></div>
          <div class="card__body">
            <h3>Experiential Learning Lab</h3>
            <p>Rapid prototyping equipment for hands-on learning and a spirit of making.</p>
            <a class="arrow-link" href="advanced-facilities.html">Explore the ELL</a>
          </div>
        </article>
        <article class="card reveal">
          <div class="card__media"><img src="assets/img/facilities/climate-thermal-chamber.jpeg" alt="Climate and thermal chambers" loading="lazy"></div>
          <div class="card__body">
            <h3>Advanced Measurements</h3>
            <p>Thermal and environmental chambers, EMI/EMC pre-compliance, biosensing.</p>
            <a class="arrow-link" href="advanced-facilities.html">See facilities</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Made in WEL</span>
        <h2>Hardware designed, built and used here</h2>
        <p>Notable development boards produced in the lab and used across IIT Bombay and beyond.</p>
      </div>
      <div class="slider reveal">
        <div class="slider__track">
          <article class="card">
            <div class="card__media card__media--contain"><img src="assets/img/boards/picoiris.png" alt="PicoIRIS board" loading="lazy"></div>
            <div class="card__body"><span class="card__tag">In development</span>
              <h3>PicoIRIS</h3>
              <p>Lab-in-a-box: oscilloscope, function generator and power supply on a single board, over USB and Bluetooth.</p>
              <a class="arrow-link" href="made-in-wel.html#picoiris">Details</a></div>
          </article>
          <article class="card">
            <div class="card__media card__media--contain"><img src="assets/img/boards/pt-51.png" alt="PT-51 development board" loading="lazy"></div>
            <div class="card__body"><span class="card__tag">Microcontroller</span>
              <h3>PT-51</h3>
              <p>An 8051-based development board that introduces students to microprocessor architecture.</p>
              <a class="arrow-link" href="made-in-wel.html#pt-51">Details</a></div>
          </article>
          <article class="card">
            <div class="card__media card__media--contain"><img src="assets/img/boards/xen10.png" alt="Xen-10 FPGA board" loading="lazy"></div>
            <div class="card__body"><span class="card__tag">FPGA</span>
              <h3>Xen-10</h3>
              <p>An ALTERA MAX 10 FPGA board for advanced digital design experiments and R&amp;D projects.</p>
              <a class="arrow-link" href="made-in-wel.html#xen-10">Details</a></div>
          </article>
          <article class="card">
            <div class="card__media card__media--contain"><img src="assets/img/boards/iq-modulator.png" alt="IQ Modulator board" loading="lazy"></div>
            <div class="card__body"><span class="card__tag">RF</span>
              <h3>IQ Modulator</h3>
              <p>Portable IQ transmitter board (373 MHz &ndash; 1.6 GHz) illustrating communication systems concepts.</p>
              <a class="arrow-link" href="made-in-wel.html#iq-modulator">Details</a></div>
          </article>
          <article class="card">
            <div class="card__media card__media--contain"><img src="assets/img/boards/qmagpi.png" alt="QMagPi magnetometer" loading="lazy"></div>
            <div class="card__body"><span class="card__tag">Research</span>
              <h3>QMagPi</h3>
              <p>A compact, portable magnetometer based on an ensemble of NV centers, built with PQuest lab.</p>
              <a class="arrow-link" href="made-in-wel.html#qmagpi">Details</a></div>
          </article>
        </div>
        <div class="slider__btns">
          <button class="slider__btn slider__btn--prev" aria-label="Previous">{i_prev}</button>
          <button class="slider__btn slider__btn--next" aria-label="Next">{i_next}</button>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Programs</span>
        <h2>More than curricular lab courses</h2>
        <p>Workshops, MOOCs, internships and student projects all run out of WEL.</p>
      </div>
      <div class="grid g3">
        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/workshop-kv-powai.jpg" alt="School workshop conducted by WEL" loading="lazy"></div>
          <div class="card__body">
            <h3>Workshops &amp; outreach</h3>
            <p>The WEL brand has reached 400+ colleges across India, training more than 2,000 teachers
               and students on hardware and lab content developed here.</p>
            <a class="arrow-link" href="workshops.html">See all workshops</a>
          </div>
        </article>
        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/work-stations.jpeg" alt="Lab workstations" loading="lazy"></div>
          <div class="card__body">
            <h3>Lab courses</h3>
            <p>10+ lab courses serving 1,700+ students a year, with tutorials, resources and manuals
               written by WEL staff and research assistants.</p>
            <a class="arrow-link" href="teaching-labs.html">See courses</a>
          </div>
        </article>
        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/outreach-nerul.jpg" alt="WEL staff speaking to a visiting college team" loading="lazy"></div>
          <div class="card__body">
            <h3>Internships &amp; projects</h3>
            <p>Interns contribute to hardware development, research assistance and software modules &mdash;
               and use that training as a launchpad.</p>
            <a class="arrow-link" href="programs.html#internships">Read more</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="stats">
        <div class="stat reveal"><b><span data-count="20" data-suffix="+">20+</span></b><span>Research papers</span></div>
        <div class="stat reveal"><b><span data-count="32" data-suffix="+">32+</span></b><span>Projects</span></div>
        <div class="stat reveal"><b><span data-count="38" data-suffix="+">38+</span></b><span>Workshops</span></div>
        <div class="stat reveal"><b><span data-count="12" data-suffix="+">12+</span></b><span>Courses</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split split--reverse">
      <div class="split__media reveal">
        <img src="assets/img/site/romesh-wadhwani.jpg" alt="Dr. Romesh Wadhwani" loading="lazy">
      </div>
      <div class="split__body reveal">
        <span class="eyebrow">Our founder</span>
        <h2>Dr. Romesh Wadhwani</h2>
        <p>Dr. Romesh Wadhwani (EE 1969) is a proven, successful entrepreneur and CEO. He built
          Symphony Technology Group from a startup to $2.5B revenue and $10B enterprise value, and has
          committed $1B of his own capital to build SymphonyAI.</p>
        <p>He established the Wadhwani Foundation for economic development in emerging economies, with
          an initial focus on India. Its initiatives include the National Entrepreneurship Network,
          which runs growth-centric entrepreneurship programs at over 500 universities and colleges,
          and a research initiative in biosciences and biotechnology to create jobs through innovation.</p>
        <a class="arrow-link" href="https://www.wfglobal.org/who-we-are/#founder" target="_blank" rel="noopener">Read his profile</a>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Our team</span>
        <h2>Academic excellence, hands-on expertise</h2>
        <p>Technical superintendents, system administrators, mechanics and project assistants manage
          everything from embedded systems and PCB design to equipment maintenance and logistics &mdash;
          alongside M.Tech research assistants who bring fresh perspectives across domains.</p>
      </div>
      <div class="grid g4 name-cards">
        <article class="name-card reveal">
          <h4>Prof. Rajbabu Velmurugan</h4><span class="person__role">Lab In-charge</span>
        </article>
        <article class="name-card reveal">
          <h4>Mahesh A. Bhaganagare</h4><span class="person__role">Technical Officer</span>
        </article>
        <article class="name-card reveal">
          <h4>Maheshwar Mangat</h4><span class="person__role">Sr. Technical Superintendent</span>
        </article>
        <article class="name-card reveal">
          <h4>Amit Shetye</h4><span class="person__role">Sr. Technical Superintendent</span>
        </article>
      </div>
      <div class="btn-row mt2 reveal">
        <a class="btn btn--outline" href="people.html">Meet the whole team</a>
        <a class="btn btn--outline" href="faculty.html">Faculty members</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Gallery</span>
        <h2>Life at the lab</h2>
        <p>Lab sessions, EDL projects, NPTEL workshops, guest visits and the facilities themselves.</p>
      </div>
      <div class="grid g4 reveal">
        <img src="assets/img/gallery/thumbs/img_9317.jpg" alt="Students working in the lab" loading="lazy" style="border-radius:14px;aspect-ratio:4/3;object-fit:cover;width:100%">
        <img src="assets/img/gallery/thumbs/img_5690.jpg" alt="NPTEL workshop at WEL" loading="lazy" style="border-radius:14px;aspect-ratio:4/3;object-fit:cover;width:100%">
        <img src="assets/img/gallery/thumbs/img_0326.jpg" alt="Guest visit to WEL" loading="lazy" style="border-radius:14px;aspect-ratio:4/3;object-fit:cover;width:100%">
        <img src="assets/img/gallery/thumbs/img_9611.jpg" alt="Electronics Design Lab project" loading="lazy" style="border-radius:14px;aspect-ratio:4/3;object-fit:cover;width:100%">
      </div>
      <div class="btn-row mt2 reveal"><a class="btn btn--outline" href="gallery.html">Open the full gallery</a></div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="cta-band reveal">
        <span class="eyebrow" style="color:#bcd8f8">Get started</span>
        <h2>Need a board, an instrument or a facility?</h2>
        <p>Requests for development boards, equipment loans and special facilities are handled online.
           Component stock is searchable through the WEL Inventory portal.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="inventory.html">Open WEL Inventory</a>
          <a class="btn btn--ghost" href="online-request.html">Make a request</a>
          <a class="btn btn--ghost" href="contact.html">Contact the lab</a>
        </div>
      </div>
    </div>
  </section>
""".format(
    i_book=icon("book"), i_tool=icon("tool"), i_board=icon("board"), i_scope=icon("scope"),
    i_box=icon("box"), i_clip=icon("clipboard"), i_prev=icon("prev"), i_next=icon("next"),
)

# ===========================================================================
# ABOUT
# ===========================================================================
ABOUT_BODY = """  <section class="section">
    <div class="wrap split">
      <div class="split__media reveal"><img src="assets/img/site/wel1-lab.jpeg" alt="The Wadhwani Electronics Laboratory" loading="lazy"></div>
      <div class="split__body reveal">
        <span class="eyebrow">What is WEL?</span>
        <h2>A laboratory built by an alumnus, for students</h2>
        <p>Wadhwani Electronics Laboratory was set up in the Department of Electrical Engineering,
          IIT Bombay with the help of an endowment from <strong>Dr. Romesh Wadhwani</strong>, a member of
          the 1969 EE batch, for teaching and project development in electronics. The laboratory was
          formally inaugurated by Dr. Wadhwani on <strong>12 February 2001</strong>.</p>
        <p>More than 1,700 students use WEL each year for laboratory courses. The lab has developed
          several hardware kits used in those courses, and is equipped with the latest series of
          electronics test instruments &mdash; oscilloscopes, function generators, FPGA programmers,
          digital multimeters and more. Various technical events are hosted every year at WEL, including
          workshops, competitions, training and outreach, and students and staff working here take part
          in numerous translational R&amp;D projects.</p>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="grid g2">
        <div class="reveal">
          <span class="eyebrow">Who are we?</span>
          <h2>One of the largest labs at IIT Bombay</h2>
          <p>WEL is managed by an excellent team of dedicated and highly motivated staff and M.Tech.
            Research Assistants. Apart from housing laboratory courses for undergraduate and postgraduate
            students in the Department of Electrical Engineering, WEL also serves as the hub for various
            student-driven R&amp;D projects.</p>
          <a class="arrow-link" href="people.html">Meet the team</a>
        </div>
        <div class="reveal">
          <span class="eyebrow">What we do</span>
          <h2>Courses, events and R&amp;D</h2>
          <p>On the academic front, WEL caters to more than 10 lab courses with a combined strength of
            more than 1,700 students per year. Various technical events are hosted every year, including
            workshops, competitions and internships. Students, RAs and staff working at WEL are also
            engaged in a range of R&amp;D projects.</p>
          <div class="btn-row">
            <a class="btn btn--outline btn--sm" href="resources.html">Resources</a>
            <a class="btn btn--outline btn--sm" href="programs.html">Programs</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap-narrow prose reveal">
      <span class="eyebrow">History</span>
      <h2>How the lab grew</h2>
      <p>Many of the activities WEL runs had not been possible earlier, at least not on the same scale,
        because of infrastructural limitations &mdash; or sometimes simply because the various electronics
        activities were physically apart. WEL made it possible to bring almost the entire electronics
        activity in EE under one umbrella, which also boosted the enthusiasm among students.</p>
      <p>WEL currently caters to over 700 students every semester. The lab has a large variety of
        microprocessor kits, microcontroller boards, CPLD/FPGA boards developed under e-Prayog (an MHRD
        supported project), cross compilers, assemblers and other utilities for these processors,
        single-board computers, online EPROM programmers, logic analyzers and in-circuit emulators, for
        use in microprocessor and other lab courses. WEL also supports experimental instruction and
        projects in analog and digital circuits and electronics design.</p>

      <h3>Two major activities started in 2002</h3>
      <p><strong>Embedded Systems Lab.</strong> A specialization called Electronic Systems was introduced
        for the M.Tech course in the EE Department. The Embedded Systems Lab was set up within WEL to
        provide laboratory support for this course, and is also made available for other courses in the
        department and for project work.</p>
      <p><strong>Enhancement of the PCB facility.</strong> The PCB making facility in the EE department
        was significantly enhanced in 2002 with the help of a grant from the Department of Science and
        Technology. The WEL fund partially supported the infrastructure development, since the PCB
        facility is used heavily for electronics projects carried out in WEL.</p>

      <h3>New developments from 2010</h3>
      <p>As part of e-Prayog, Virtual Labs, IIT Bombay &mdash; an initiative of the Ministry of Human
        Resource Development under the National Mission on Education through ICT &mdash; the following
        electronics lab courses were developed at WEL:</p>
      <ul>
        <li>Electronic Devices and Circuits</li>
        <li>Network Analysis</li>
        <li>Linear Integrated Circuits</li>
        <li>Signals and Systems</li>
        <li>Digital Signal Processing using DSK6713, DSK5510 and a low-cost board using TMS320VC33</li>
        <li>Modern Digital Design using CPLD and FPGA</li>
        <li>Microcontrollers</li>
        <li>Image Processing</li>
      </ul>
      <p>These are purely simulation-based labs and users are not required to book slots. They are also
        low-cost kit-based labs &mdash; the kits are made available to interested students on request for
        their basic understanding and projects.</p>
    </div>
  </section>

  <section class="section section--dark section--tight">
    <div class="wrap">
      <div class="section-head center reveal">
        <span class="eyebrow">Our reach</span>
        <h2>We are proud of these numbers</h2>
      </div>
      <div class="stats">
        <div class="stat reveal"><b><span data-count="1700" data-suffix="+">1,700+</span></b><span>Students / year</span></div>
        <div class="stat reveal"><b><span data-count="20" data-suffix="+">20+</span></b><span>Research papers</span></div>
        <div class="stat reveal"><b><span data-count="32" data-suffix="+">32+</span></b><span>Projects</span></div>
        <div class="stat reveal"><b><span data-count="38" data-suffix="+">38+</span></b><span>Workshops</span></div>
        <div class="stat reveal"><b><span data-count="12" data-suffix="+">12+</span></b><span>Courses</span></div>
      </div>
    </div>
  </section>
"""

# ===========================================================================
# PROGRAMS
# ===========================================================================
PROGRAMS_BODY = """  <section class="section">
    <div class="wrap-narrow reveal">
      <p class="lead">WEL serves as the hub of electronics activity for students at IIT Bombay. Other
        than curricular lab courses, events at WEL include workshops and outreach, MOOCs, and
        co-curricular and extracurricular student projects and internships.</p>
    </div>
  </section>

  <section class="section section--tight" id="workshops">
    <div class="wrap split">
      <div class="split__media reveal"><img src="assets/img/site/workshop-kv-powai.jpg" alt="A school workshop run by WEL" loading="lazy"></div>
      <div class="split__body reveal">
        <span class="eyebrow">Workshops</span>
        <h2>400+ colleges, 2,000+ teachers and students</h2>
        <p>The WEL brand has reached more than 400 colleges across India thanks to workshops conducted
          over the years, with more than 2,000 teachers and students trained on hardware and lab content
          developed in WEL.</p>
        <p>WEL continues this tradition and offers workshops in partnership with <strong>NPTEL</strong>,
          which certifies students on successful completion of summer workshops. Workshops offered
          through other entities at IIT Bombay (QIP, TiH-IoT) also use WEL premises. Recently WEL has
          been part of alumni outreach activities through the EE Alumni and Corporate Engagement (ACE)
          cell.</p>
        <div class="btn-row">
          <a class="btn btn--primary btn--sm" href="workshops.html">All workshops, with highlights</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight" id="lab-courses">
    <div class="wrap split split--reverse">
      <div class="split__media reveal"><img src="assets/img/site/lab-sessions.jpg" alt="Students during a lab course session" loading="lazy"></div>
      <div class="split__body reveal">
        <span class="eyebrow">Lab courses</span>
        <h2>10+ courses, 1,700+ students a year</h2>
        <p>Most of the hardware required for conducting these courses has been designed and manufactured
          at WEL. Tutorials, resources and user manuals made by WEL staff and research assistants are
          used to offer students an engaging learning experience.</p>
        <div class="btn-row">
          <a class="btn btn--outline btn--sm" href="autumn-semester.html">Autumn semester</a>
          <a class="btn btn--outline btn--sm" href="spring-semester.html">Spring semester</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="grid g2">
        <div class="lcard reveal" id="internships">
          <span class="lcard__icon">{i_people}</span>
          <h3>Internships</h3>
          <p>WEL has hosted several students for internships and project positions over the years. Our
            interns have contributed to hardware development, research assistantship, software modules
            and resources, and day-to-day lab activities. WEL has served as a launchpad for young
            graduates who leveraged their training here to obtain prestigious fellowships for higher
            studies and rewarding industry positions.</p>
          <p style="margin-top:.9rem"><a class="arrow-link" href="contact.html">Contact us for details</a></p>
        </div>
        <div class="lcard reveal" id="moocs">
          <span class="lcard__icon">{i_spark}</span>
          <h3>Lab MOOCs</h3>
          <p>Massive open online courses help students access repositories of knowledge not constrained
            by location, at their own pace. MOOC-style courses are typically aimed at theoretical
            concepts, while comparatively little effort has gone into practicum courses. WEL has
            developed expertise in conducting <strong>online lab courses</strong> and offering MOOCs on a
            variety of lab subjects.</p>
          <p style="margin-top:.9rem"><a class="arrow-link" href="blogs.html">Read the online labs report</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>Want to collaborate with WEL?</h2>
        <p>Institutions and student groups interested in workshops, training or outreach programs on
           WEL hardware and lab content are welcome to get in touch.</p>
        <div class="btn-row"><a class="btn btn--red" href="contact.html">Talk to the lab</a></div>
      </div>
    </div>
  </section>
""".format(i_people=icon("people"), i_spark=icon("spark"))

# ===========================================================================
# ACHIEVEMENTS
# ===========================================================================
ACH = [
    ("hardware-kits", "assets/img/site/madeinwel.png", "Course hardware",
     "Hardware kits for lab courses", "Product developer: Vivekanand Dhakane",
     "Hardware required for laboratory courses at WEL is primarily designed and manufactured in-house. "
     "This tradition has been in place for more than 10 years, and numerous students and staff have "
     "participated in developing and benefiting from such hardware for courses and projects. Notable "
     "examples include Krypton (Intel MAX V CPLD), Xen-10 (MAX 10 CPLD), PT-51 (Microchip AT89C5131), "
     "the IQ modulator board and PicoIRIS, an all-in-one lab-on-board under development.",
     "made-in-wel.html", "View the boards"),
    ("inspec", "assets/img/site/inspec-cs100.jpg", "Translational R&amp;D",
     "inSPEC CS100", "Handheld rebar inspection device",
     "The inSPEC CS100 is a handheld device designed for on-demand inspection and measurement of rebar "
     "diameter and cover thickness in reinforced concrete structures. It is particularly useful for "
     "structural analysis applications including repairs, renovations, inspections and quality control "
     "of RCC structures. The device is being commercialised by Nirixense Technologies Pvt. Ltd., a "
     "startup incubated at SINE, IIT Bombay.", "", ""),
    ("qmagpi", "assets/img/site/qmagpi.jpg", "Research instrument",
     "QMagPi", "Quantum Magnetometer with PI control",
     "QMagPi is a compact and portable magnetometer based on an ensemble of NV centers. It was "
     "developed at the PQuest lab in collaboration with WEL.", "made-in-wel.html#qmagpi", "Board details"),
    ("nirmiti", "assets/img/site/nirmiti.jpg", "Outreach",
     "Nirmiti", "Product developer: Vivekanand Dhakane",
     "Nirmiti is an initiative started by Vivekanand Dhakane during the COVID-19 lockdown at his village "
     "Shevgaon, to make electronics learning affordable, simple and language-independent for everyone "
     "from schoolchildren to engineers and hobbyists.", "", ""),
    ("welpcr", "assets/img/site/welpcr.png", "Open source",
     "WEL PCR", "Low-cost DNA thermal cycler",
     "WELPCR is a low-cost polymerase chain reaction thermal cycler for DNA amplification developed at "
     "WEL. Inspired by the OpenPCR design, it is a standalone device that needs no computer or mobile "
     "device to configure and operate. The bill of materials for one unit is under Rs. 10,000 "
     "(about USD 120), which makes it a strong resource for educational and research use in "
     "laboratories with limited resources. The design is open-source and available to developers who "
     "want to assemble their own units.", "", ""),
    ("acpad", "assets/img/site/micron.png", "Alumni product",
     "ACPAD", "Product developer: Amaldev V",
     "ACPAD is the world's first wireless MIDI controller for acoustic guitar. With ACPAD you have "
     "access to hundreds of instruments, sound effects and loops &mdash; right where you want them, on "
     "your guitar.", "", ""),
]


def _ach_cards():
    out = []
    for anchor, img, tag, title, sub, body, link, link_label in ACH:
        cta = '<a class="arrow-link" href="%s">%s</a>' % (link, link_label) if link else ""
        out.append("""        <article class="card reveal" id="{a}">
          <div class="card__media card__media--contain"><img src="{img}" alt="{title}" loading="lazy"></div>
          <div class="card__body">
            <span class="card__tag">{tag}</span>
            <h3>{title}</h3>
            <div class="card__meta">{sub}</div>
            <p>{body}</p>
            {cta}
          </div>
        </article>""".format(a=anchor, img=img, tag=tag, title=title, sub=sub, body=body, cta=cta))
    return "\n".join(out)


ACHIEVEMENTS_BODY = """  <section class="section">
    <div class="wrap">
      <div class="wrap-narrow reveal" style="width:100%;padding:0;margin:0 0 2.6rem">
        <p class="lead">WEL cultivates a vibrant community of highly capable and passionate engineers and
          research assistants who continually demonstrate excellence through developmental activities.
          Students and staff working at WEL have made numerous contributions through innovative projects,
          academic and industry recognition, and translational impact.</p>
      </div>
      <div class="grid g3">
{cards}
      </div>
    </div>
  </section>

  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>WEL Publications</h2>
        <p>The complete list of publications based on pedagogical activities at WEL, along with the
           R&amp;D done by students, research assistants and staff working at the lab.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="contact.html">Request the publication list</a>
          <a class="btn btn--ghost" href="https://www.ee.iitb.ac.in/~wel_iitb/achievements/index.html" target="_blank" rel="noopener">Archived list</a>
        </div>
      </div>
    </div>
  </section>
""".format(cards=_ach_cards())

# ===========================================================================
# CONTACT
# ===========================================================================
CONTACT_BODY = """  <section class="section">
    <div class="wrap">
      <div class="grid g2" style="align-items:start">
        <div class="reveal">
          <span class="eyebrow">Reach the lab</span>
          <h2>Wadhwani Electronics Laboratory</h2>
          <p>Department of Electrical Engineering,<br>
             Indian Institute of Technology Bombay,<br>
             Powai, Mumbai 400076, India</p>

          <div class="table-wrap mt2" style="margin-top:1.6rem">
            <table>
              <thead><tr><th>Channel</th><th>Details</th></tr></thead>
              <tbody>
                <tr><td>Lab email</td><td><a href="mailto:{email}">{email}</a></td></tr>
                <tr><td>Lab phone</td><td>{phone_lab}</td></tr>
                <tr><td>Office phone</td><td>{phone_office}</td></tr>
                <tr><td>Location</td><td>3rd Floor, Electrical Engineering Department</td></tr>
              </tbody>
            </table>
          </div>

          <div class="note mt2" style="margin-top:1.6rem">
            <strong>Requests for equipment, boards or facilities</strong> should go through the
            <a href="online-request.html">online request pages</a> rather than email &mdash; that way the
            request is tracked and stock is updated automatically.
          </div>
        </div>

        <div class="reveal">
          <h3>Who to write to</h3>
          <div class="grid" style="gap:1rem">
            <div class="lcard">
              <h3 style="font-size:1.02rem">Prof. Rajbabu Velmurugan</h3>
              <p>Lab In-charge &mdash; <a href="mailto:rajbabu@ee.iitb.ac.in">rajbabu@ee.iitb.ac.in</a><br>
                 022-2576-7444 (O) / 022-2576-8444 (R)</p>
            </div>
            <div class="lcard">
              <h3 style="font-size:1.02rem">Mahesh A. Bhaganagare</h3>
              <p>Technical Officer &mdash; <a href="mailto:mab@ee.iitb.ac.in">mab@ee.iitb.ac.in</a><br>
                 022-2576-4412 / 4403 (O)</p>
            </div>
            <div class="lcard">
              <h3 style="font-size:1.02rem">Ankur Agarwal</h3>
              <p>Jr. Technical Superintendent &mdash; <a href="mailto:ankur_ee@iitb.ac.in">ankur_ee@iitb.ac.in</a><br>
                 022-2576-4409 (O)</p>
            </div>
          </div>
          <div class="btn-row mt2" style="margin-top:1.4rem">
            <a class="btn btn--outline btn--sm" href="staff.html">All staff members</a>
            <a class="btn btn--outline btn--sm" href="faculty.html">All faculty members</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight section--alt">
    <div class="wrap">
      <div class="section-head reveal"><span class="eyebrow">Find us</span><h2>3rd floor, EE Department, IIT Bombay</h2></div>
      <div class="reveal" style="border-radius:22px;overflow:hidden;border:1px solid var(--line)">
        <iframe title="Map to IIT Bombay Electrical Engineering Department"
          src="https://www.openstreetmap.org/export/embed.html?bbox=72.9080%2C19.1290%2C72.9250%2C19.1370&amp;layer=mapnik&amp;marker=19.1334%2C72.9163"
          style="width:100%;height:420px;border:0;display:block" loading="lazy"></iframe>
      </div>
      <p style="margin-top:.9rem;font-size:.9rem;color:var(--muted)">
        <a href="https://www.openstreetmap.org/?mlat=19.1334&amp;mlon=72.9163#map=16/19.1334/72.9163" target="_blank" rel="noopener">Open larger map</a>
      </p>
    </div>
  </section>
""".format(email=SITE["email"], phone_lab=SITE["phone_lab"], phone_office=SITE["phone_office"])


PAGES = [
    {
        "file": "index.html", "nav": "index.html", "sub": None,
        "title": "Wadhwani Electronics Laboratory | IIT Bombay",
        "desc": "The Wadhwani Electronics Laboratory at IIT Bombay - teaching labs, in-house hardware, "
                "rapid prototyping and advanced measurement for over 1,700 students a year.",
        "hero": HOME_HERO, "body": HOME_BODY,
    },
    {
        "file": "about.html", "nav": "about.html", "sub": "about.html",
        "title": "About WEL | Wadhwani Electronics Laboratory",
        "desc": "WEL was inaugurated on 12 February 2001 in the Department of Electrical Engineering, "
                "IIT Bombay, through an endowment from Dr. Romesh Wadhwani (EE 1969).",
        "hero": page_hero("About WEL",
                          "What the lab is, who runs it and what happens here - from the 2001 "
                          "inauguration to the facilities of today.",
                          [("About WEL", "about.html")],
                          "assets/img/site/wel-lab.png"),
        "body": ABOUT_BODY,
    },
    {
        "file": "programs.html", "nav": "programs.html", "sub": None,
        "title": "Programs | Wadhwani Electronics Laboratory",
        "desc": "Workshops, lab courses, internships and lab MOOCs run out of the Wadhwani Electronics "
                "Laboratory at IIT Bombay.",
        "hero": page_hero("Programs",
                          "Workshops and outreach, curricular lab courses, internships and lab MOOCs.",
                          [("Programs", "programs.html")],
                          "assets/img/site/workshop-kv-powai.jpg"),
        "body": PROGRAMS_BODY,
    },
    {
        "file": "achievements.html", "nav": "about.html", "sub": "achievements.html",
        "title": "Achievements | Wadhwani Electronics Laboratory",
        "desc": "Products, instruments and publications from the Wadhwani Electronics Laboratory - "
                "inSPEC CS100, QMagPi, WEL PCR, Nirmiti, ACPAD and course hardware.",
        "hero": page_hero("Achievements",
                          "Innovative projects, academic and industry recognition, and translational "
                          "impact from students and staff at WEL.",
                          [("About", "about.html"), ("Achievements", "achievements.html")],
                          "assets/img/site/madeinwel.png"),
        "body": ACHIEVEMENTS_BODY,
    },
    {
        "file": "contact.html", "nav": "contact.html", "sub": None,
        "title": "Contact Us | Wadhwani Electronics Laboratory",
        "desc": "Contact the Wadhwani Electronics Laboratory, Department of Electrical Engineering, "
                "IIT Bombay, Powai, Mumbai 400076.",
        "hero": page_hero("Contact Us",
                          "Wadhwani Electronics Lab, Department of Electrical Engineering, "
                          "IIT Bombay, Powai, Mumbai 400076.",
                          [("Contact Us", "contact.html")],
                          "assets/img/site/wel1-lab.jpeg"),
        "body": CONTACT_BODY,
    },
]
