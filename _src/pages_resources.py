# -*- coding: utf-8 -*-
"""Resources hub, advanced facilities, Made in WEL boards, instruments,
components and the IITB WEL Inventory front door."""
from build import SITE, icon, page_hero

# ===========================================================================
# RESOURCES HUB
# ===========================================================================
RESOURCES_BODY = """  <section class="section">
    <div class="wrap">
      <div class="wrap-narrow reveal" style="width:100%;padding:0;margin:0 0 2.6rem">
        <p class="lead">Students and staff at WEL have developed several resources over the years. The
          identity of WEL has evolved from being solely a lab for curricular courses when it started
          operations in 2001, into a hub for electronics activity with state-of-the-art facilities for
          projects and product development over two decades.</p>
      </div>

      <div class="grid g3">
        <a class="lcard reveal" href="advanced-facilities.html"><span class="lcard__icon">{i_tool}</span>
          <h3>Advanced facilities in WEL Lab</h3>
          <p>Thermal and climate chambers, 3D printers and scanner, laser cutter, milling machine,
             lathe, coil winder and ESD workstations.</p></a>

        <a class="lcard reveal" href="made-in-wel.html"><span class="lcard__icon">{i_board}</span>
          <h3>Development boards made in WEL</h3>
          <p>PicoIRIS, PT-51, Xen-10, the IQ Modulator and QMagPi &mdash; designed, built and supported
             in-house.</p></a>

        <a class="lcard reveal" href="instruments.html"><span class="lcard__icon">{i_scope}</span>
          <h3>Instruments</h3>
          <p>Signal generators, oscilloscopes and displays, analyzers, multimeters, power and
             high-voltage equipment.</p></a>

        <a class="lcard reveal" href="components.html"><span class="lcard__icon">{i_chip}</span>
          <h3>Components</h3>
          <p>Passives, discretes, analog and digital ICs, microcontrollers, memory, sensors, motors and
             displays, plus datasheets.</p></a>

        <a class="lcard lcard--red reveal" href="inventory.html"><span class="lcard__icon">{i_box}</span>
          <h3>IITB WEL Inventory</h3>
          <p>The searchable component stock portal: browse, add to a request cart and submit as a
             project team.</p></a>

        <a class="lcard lcard--red reveal" href="online-request.html"><span class="lcard__icon">{i_clip}</span>
          <h3>Online requests</h3>
          <p>Special facilities, development boards and modules, and equipment loans.</p></a>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">The wings of the lab</span>
        <h2>What each part of WEL does</h2>
      </div>
      <div class="grid g2">
        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/madeinwel.png" alt="Boards made in WEL" loading="lazy"></div>
          <div class="card__body">
            <h3>Made in WEL</h3>
            <div class="card__meta">Product developer: Vivekanand Dhakane</div>
            <p>Hardware required for laboratory courses at WEL is primarily designed and manufactured
              in-house. This tradition has been in place for more than 10 years. Notable examples include
              Krypton (Intel MAX V CPLD), Xen-10 (MAX 10 CPLD), PT-51 (Microchip AT89C5131), the IQ
              modulator board and PicoIRIS, an all-in-one lab-on-board under development.</p>
            <a class="arrow-link" href="made-in-wel.html">See the boards</a>
          </div>
        </article>

        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/work-stations.jpeg" alt="Instructional laboratories" loading="lazy"></div>
          <div class="card__body">
            <h3>Instructional laboratories</h3>
            <div class="card__meta">Product developer: Ruchira Nandeshwar</div>
            <p>WEL has more than 5,000 sq. ft. of space dedicated to laboratory courses that form part of
              the curriculum for Electrical Engineering students. These sections are equipped with about
              100 identical setups of arbitrary function generators, digital storage oscilloscopes, power
              supplies, multimeters and desktop computers, plus soldering stations, components and
              accessories for assembling circuit boards.</p>
            <a class="arrow-link" href="teaching-labs.html">Teaching labs</a>
          </div>
        </article>

        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/ell.jpeg" alt="Experiential Learning Laboratory" loading="lazy"></div>
          <div class="card__body">
            <h3>Experiential Learning Laboratory</h3>
            <div class="card__meta">Inaugurated 14 February 2022</div>
            <p>The ELL was inaugurated by Dr. Hemant Kanakia, a Distinguished Alumnus of IIT Bombay. The
              lab has a variety of rapid prototyping equipment to facilitate hands-on learning and
              inculcate a spirit of making among students.</p>
            <a class="arrow-link" href="advanced-facilities.html">Prototyping equipment</a>
          </div>
        </article>

        <article class="card reveal">
          <div class="card__media"><img src="assets/img/facilities/climate-thermal-chamber.jpeg" alt="Advanced measurements lab" loading="lazy"></div>
          <div class="card__body">
            <h3>Advanced measurements lab</h3>
            <div class="card__meta">Set up September 2022</div>
            <p>The advanced measurements wing of WEL houses state-of-the-art facilities such as thermal
              and environmental chambers, EMI/EMC pre-compliance test setups, and facilities for
              biosensing and synthetic biology.</p>
            <a class="arrow-link" href="advanced-facilities.html">See the chambers</a>
          </div>
        </article>

        <article class="card reveal">
          <div class="card__media"><img src="assets/img/site/pcb-blue.png" alt="PCB fabrication" loading="lazy"></div>
          <div class="card__body">
            <h3>PCB fabrication lab</h3>
            <div class="card__meta">Product developer: Ruchira Nandeshwar</div>
            <p>WEL has a printed circuit board manufacturing facility that can produce 2-layer PCBs with
              12 mil resolution for surface mount packages.</p>
            <a class="arrow-link" href="online-request.html#special-facilities">Request PCB fabrication</a>
          </div>
        </article>

        <article class="card reveal">
          <div class="card__media"><img src="assets/img/facilities/esd-workstation.jpeg" alt="EMI/EMC test facility" loading="lazy"></div>
          <div class="card__body">
            <h3>EMI/EMC test facility</h3>
            <div class="card__meta">Advanced measurements wing</div>
            <p>EMI/EMC pre-compliance test setups sit alongside the thermal and environmental chambers in
              the advanced measurements wing, set up in September 2022.</p>
            <a class="arrow-link" href="online-request.html#special-facilities">Request access</a>
          </div>
        </article>
      </div>
    </div>
  </section>
""".format(i_tool=icon("tool"), i_board=icon("board"), i_scope=icon("scope"),
           i_chip=icon("chip"), i_box=icon("box"), i_clip=icon("clipboard"))


# ===========================================================================
# ADVANCED FACILITIES
# ===========================================================================
FACILITIES = [
    ("Thermal Chamber", "assets/img/facilities/climate-thermal-chamber.jpeg", "Environmental", [
        ("Temperature range", "&minus;20 &deg;C to 100 &deg;C"),
        ("Temperature resolution", "1 &deg;C"),
        ("Workspace", "550 mm &times; 550 mm &times; 550 mm"),
        ("Manufacturer", "Climate System Engineers, Pune"),
    ]),
    ("Climate Chamber", "assets/img/facilities/autoclave-climate.jpeg", "Environmental", [
        ("Temperature range", "&minus;20 &deg;C to 100 &deg;C"),
        ("Humidity range", "50% RH to 95% RH"),
        ("Temperature resolution", "1 &deg;C"),
        ("Humidity resolution", "1% RH"),
        ("Workspace", "1250 mm &times; 1200 mm &times; 450 mm"),
        ("Manufacturer", "Arcade Scientific Instruments, Delhi"),
    ]),
    ("ESD Work Station", "assets/img/facilities/esd-workstation.jpeg", "Bench", [
        ("Table area", "1800 mm &times; 900 mm"),
        ("Power supply", "Keithley 2231A-30-3"),
        ("DSO", "Tektronix TBS-1072C"),
        ("AFG", "Tektronix AFG1022"),
        ("DMM", "Aplab 1003"),
    ]),
    ("Desktop Lathe Machine", "assets/img/facilities/lathe.png", "Machining", [
        ("Model", "Proxxon PD 400"),
        ("Motor speed", "1400 / 2800 rpm"),
    ]),
    ("3D Scanner", "assets/img/facilities/3d-scanner.png", "Prototyping", [
        ("Model", "Shining 3D EinScan-SE"),
        ("Scan volume", "200 mm &times; 200 mm &times; 200 mm (with turntable)"),
    ]),
    ("Acrylic Laser Cutter", "assets/img/facilities/laser-cutter.jpeg", "Prototyping", [
        ("Model", "SILasers AccuCut 6090"),
        ("Work area", "600 mm &times; 900 mm"),
        ("Laser type", "CO<sub>2</sub> laser"),
        ("Laser power", "100 W"),
        ("Tolerance", "&plusmn;0.3 mm"),
        ("Materials", "Acrylic, plywood, MDF, cardboard"),
    ]),
    ("Desktop Milling Machine", "assets/img/facilities/milling.png", "Machining", [
        ("Model", "Roland SRM-20"),
        ("Table size", "230 mm &times; 156 mm"),
        ("Operating speed", "6 to 1800 mm/min"),
        ("Mechanical resolution", "0.001 mm/step"),
        ("Spindle rotation speed", "3000 to 7000 rpm"),
    ]),
    ("FDM 3D Printer &ndash; Large", "assets/img/facilities/fdm-large.jpg", "Prototyping", [
        ("Model", "Fracktal Works Julia Pro Dual"),
        ("Print volume", "390 &times; 390 &times; 340 mm"),
        ("Extruders", "2"),
        ("Filament diameter", "1.75 mm"),
        ("Extruder diameter", "0.6 mm"),
        ("Layer height", "0.15 &ndash; 0.45 mm"),
        ("Tolerance", "&plusmn;0.3 mm"),
        ("Materials", "PLA, ABS, TPU"),
    ]),
    ("FDM 3D Printer &ndash; Small", "assets/img/facilities/fdm-small.jpg", "Prototyping", [
        ("Model", "Fracktal Works Julia Advance"),
        ("Print volume", "190 &times; 190 &times; 190 mm"),
        ("Filament diameter", "1.75 mm"),
        ("Extruder diameter", "0.4 mm"),
        ("Layer height", "0.1 &ndash; 0.3 mm"),
        ("Tolerance", "&plusmn;0.2 mm"),
        ("Materials", "PLA, ABS, TPU"),
    ]),
    ("SLA 3D Printer &ndash; Large", "assets/img/facilities/sla-large.png", "Prototyping", [
        ("Model", "Elegoo Jupiter 6K"),
        ("Print volume", "278 &times; 156 &times; 300 mm"),
        ("Layer height", "0.01 &ndash; 0.2 mm"),
        ("Materials", "UV (405 nm) liquid resins"),
    ]),
    ("SLA 3D Printer &ndash; Small", "assets/img/facilities/sla-small.jpg", "Prototyping", [
        ("Model", "Original Prusa SL1 Speed + CW1S"),
        ("Print volume", "127 &times; 80 &times; 150 mm"),
        ("Layer height", "0.025 &ndash; 0.1 mm"),
        ("Materials", "UV resin (405 nm)"),
        ("Solvent", "IPA"),
    ]),
    ("Programmable Coil Winding Machine", "assets/img/facilities/coil-winding.jpeg", "Machining", [
        ("Model", "Optima 1250"),
        ("Manufacturer", "Synthesis Winding Technologies, Bengaluru"),
        ("Spindle torque", "15 Nm"),
        ("Spindle speed", "100 &ndash; 6000 rpm"),
        ("Wire diameter", "0.1 &ndash; 1.5 mm"),
        ("Winding width", "250 mm (max)"),
        ("Turns", "100,000 (max)"),
    ]),
]


def _facility_cards():
    out = []
    for name, img, cat, specs in FACILITIES:
        rows = "".join("<li><b>%s</b><span>%s</span></li>" % (k, v) for k, v in specs)
        out.append("""        <article class="card reveal" data-cat="{cat}">
          <div class="card__media card__media--contain"><img src="{img}" alt="{plain}" loading="lazy"></div>
          <div class="card__body">
            <span class="card__tag">{cat}</span>
            <h3>{name}</h3>
            <ul class="specs">{rows}</ul>
          </div>
        </article>""".format(cat=cat, img=img, name=name, plain=name.replace("&ndash;", "-"), rows=rows))
    return "\n".join(out)


FACILITIES_BODY = """  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Advanced facilities</span>
        <h2>Equipment available in the lab</h2>
        <p>The advanced measurements wing and the Experiential Learning Laboratory together hold the
          chambers, printers, cutters and machines below. Access is booked through the special facilities
          request form.</p>
      </div>

      <div class="filters reveal" data-filter-group data-filter-target=".card[data-cat]">
        <button class="filter is-active" data-filter="all">All facilities</button>
        <button class="filter" data-filter="Environmental">Environmental</button>
        <button class="filter" data-filter="Prototyping">Prototyping</button>
        <button class="filter" data-filter="Machining">Machining</button>
        <button class="filter" data-filter="Bench">Bench</button>
      </div>

      <div class="grid g3">
{cards}
      </div>
    </div>
  </section>

  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="grid g2">
        <div class="lcard reveal">
          <span class="lcard__icon">{i_flask}</span>
          <h3>PCB fabrication</h3>
          <p>WEL has a printed circuit board manufacturing facility that can produce 2-layer PCBs with
             12 mil resolution for surface mount packages.</p>
        </div>
        <div class="lcard reveal">
          <span class="lcard__icon">{i_scope}</span>
          <h3>EMI/EMC pre-compliance</h3>
          <p>The advanced measurements wing, set up in September 2022, houses EMI/EMC pre-compliance test
             setups alongside facilities for biosensing and synthetic biology.</p>
        </div>
      </div>
      <div class="cta-band reveal" style="margin-top:2.4rem">
        <h2>Book a facility</h2>
        <p>Access to the chambers, printers, cutters, PCB fabrication and EMI/EMC setups is arranged
           through the special facilities online request.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="online-request.html#special-facilities">Request a facility</a>
          <a class="btn btn--ghost" href="contact.html">Ask a question</a>
        </div>
      </div>
    </div>
  </section>
""".format(cards=_facility_cards(), i_flask=icon("flask"), i_scope=icon("scope"))


# ===========================================================================
# MADE IN WEL
# ===========================================================================
BOARDS = [
    ("picoiris", "PicoIRIS", "assets/img/boards/picoiris.png", "In development",
     "Product developer: Ankur Agarwal",
     "Lab-in-a-box with oscilloscope, function generator and power supply functionality on a single "
     "board, with USB and Bluetooth connectivity for operation from a laptop computer."),
    ("pt-51", "PT-51", "assets/img/boards/pt-51.png", "Microcontroller",
     "Product developers: Maheshwar Mangat, Geetanjali Shinde",
     "PT-51 is an 8051-based development board designed for introducing students to microprocessor "
     "architecture. It is built around the Microchip AT89C5131 and is used in the microprocessors lab "
     "course."),
    ("xen-10", "Xen-10", "assets/img/boards/xen10.png", "FPGA",
     "Product developers: Vidur Shah, Mahesh B., Maheshwar M., Amit S.",
     "Xen-10 is an ALTERA MAX 10 FPGA development board for advanced digital design experiments and "
     "R&amp;D projects."),
    ("iq-modulator", "IQ Modulator", "assets/img/boards/iq-modulator.png", "RF",
     "Product developers: Manu T. S., Saurabh A., Maheshwar M.",
     "A portable IQ transmitter board covering 373 MHz to 1.6 GHz, used to illustrate communication "
     "systems concepts in the communications lab."),
    ("qmagpi", "QMagPi", "assets/img/boards/qmagpi.png", "Research",
     "Developed with PQuest Lab",
     "QMagPi (Quantum Magnetometer with PI control) is a compact and portable magnetometer based on an "
     "ensemble of NV centers, developed at PQuest lab in collaboration with WEL."),
]


def _board_cards():
    out = []
    for anchor, name, img, tag, dev, body in BOARDS:
        out.append("""        <article class="card reveal" id="{a}">
          <div class="card__media card__media--contain"><img src="{img}" alt="{name}" loading="lazy"></div>
          <div class="card__body">
            <span class="card__tag">{tag}</span>
            <h3>{name}</h3>
            <div class="card__meta">{dev}</div>
            <p>{body}</p>
            <a class="arrow-link" href="online-request.html#dev-boards">Request this board</a>
          </div>
        </article>""".format(a=anchor, img=img, name=name, tag=tag, dev=dev, body=body))
    return "\n".join(out)


BOARDS_BODY = """  <section class="section">
    <div class="wrap">
      <div class="wrap-narrow reveal" style="width:100%;padding:0;margin:0 0 2.6rem">
        <p class="lead">Hardware required for laboratory courses at WEL is primarily designed and
          manufactured in-house. This tradition has been in place for more than ten years, and numerous
          students and staff have participated in developing &mdash; and benefited from using &mdash;
          such hardware for courses and projects.</p>
      </div>
      <div class="grid g3">
{cards}
      </div>
    </div>
  </section>

  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="grid g2">
        <div class="reveal">
          <span class="eyebrow">Also from the bench</span>
          <h2>Krypton</h2>
          <p>Krypton is an Intel MAX V CPLD development board built at WEL for digital design
             experiments, and remains part of the family of in-house boards used across courses at
             IIT Bombay and other colleges.</p>
        </div>
        <div class="reveal">
          <span class="eyebrow">Availability</span>
          <h2>Borrowing a board</h2>
          <p>Boards and the modules that go with them can be taken from WEL for a specific time period
             through the online request portal. Course kits are issued through the teaching lab staff.</p>
          <div class="btn-row">
            <a class="btn btn--primary btn--sm" href="online-request.html#dev-boards">Request a board</a>
            <a class="btn btn--outline btn--sm" href="inventory.html">Component stock</a>
          </div>
        </div>
      </div>
    </div>
  </section>
""".format(cards=_board_cards())


# ===========================================================================
# INSTRUMENTS
# ===========================================================================
SIGNAL_GENERATORS = [
    ("Anritsu MG3601A", "assets/img/instruments/anritsu-mg3601a.png", "Signal generator, 1040 MHz"),
    ("Agilent 33250A", "assets/img/instruments/agilent-33250a.jpeg", "Function / arbitrary waveform generator, 80 MHz"),
    ("Agilent 33220A", "assets/img/instruments/agilent-33220a.jpg", "Function / arbitrary waveform generator, 20 MHz"),
    ("Aplab 2019A", "assets/img/instruments/aplab-2019a.jpg", "20 MHz function / pulse generator"),
    ("Aplab 2011A", "assets/img/instruments/aplab-2011a.jpg", "Function generator / counter"),
]

OTHER_CATEGORIES = [
    ("Oscilloscopes &amp; Displays", "scope",
     "Digital storage oscilloscopes at every teaching bench, plus higher-bandwidth scopes and displays "
     "for advanced courses and sensitive measurements."),
    ("Analyzers", "chip",
     "Logic analyzers and spectrum / network analysis equipment for digital debugging and "
     "high-frequency measurement."),
    ("Multimeters &amp; Meters", "tool",
     "Bench and handheld digital multimeters, LCR meters and dedicated meters used across the "
     "instructional laboratories."),
    ("Power &amp; High-Voltage Equipment", "flask",
     "Programmable bench power supplies and high-voltage sources for device characterisation and "
     "project work."),
    ("Specialized Testers and Other", "board",
     "In-circuit emulators, EPROM programmers, FPGA programmers and dedicated testers built up over "
     "two decades of lab operation."),
]


def _instrument_cards():
    out = []
    for name, img, desc in SIGNAL_GENERATORS:
        out.append("""        <article class="card reveal">
          <div class="card__media card__media--contain"><img src="{img}" alt="{name}" loading="lazy"></div>
          <div class="card__body">
            <span class="card__tag">Signal generator</span>
            <h3>{name}</h3>
            <p>{desc}</p>
          </div>
        </article>""".format(img=img, name=name, desc=desc))
    return "\n".join(out)


def _other_categories():
    out = []
    for name, ico, desc in OTHER_CATEGORIES:
        out.append("""        <div class="lcard reveal"><span class="lcard__icon">{ic}</span>
          <h3>{name}</h3><p>{desc}</p></div>""".format(ic=icon(ico), name=name, desc=desc))
    return "\n".join(out)


INSTRUMENTS_BODY = """  <section class="section">
    <div class="wrap">
      <div class="wrap-narrow reveal" style="width:100%;padding:0;margin:0 0 2.4rem">
        <p class="lead">The Wadhwani Electronics Lab is equipped with routine low-end instruments and
          also advanced instruments for special purposes. Low-end instruments include oscilloscopes,
          function generators, multimeters and power supplies for use in second-year electronics courses.
          Advanced instruments are available for advanced courses, sensitive measurements and
          high-frequency work. Each set-up has a networked PC that displays lab sheets and datasheets and
          gives access to related information online.</p>
      </div>

      <div class="section-head reveal">
        <span class="eyebrow">Signal generators</span>
        <h2>Generators available in the lab</h2>
      </div>
      <div class="grid g3">
{cards}
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Other categories</span>
        <h2>The rest of the instrument pool</h2>
        <p>Detailed model-by-model listings for these categories are being migrated onto this site. For
          current availability, check the equipment loan portal or ask the lab staff.</p>
      </div>
      <div class="grid g3">
{others}
      </div>
      <div class="cta-band reveal" style="margin-top:2.6rem">
        <h2>Borrow an instrument</h2>
        <p>Instruments can be taken from WEL for a specific time period, subject to availability.
           Requests go through the equipment loan portal.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="online-request.html#equipment-loan">Request equipment</a>
          <a class="btn btn--ghost" href="contact.html">Ask about an instrument</a>
        </div>
      </div>
    </div>
  </section>
""".format(cards=_instrument_cards(), others=_other_categories())


# ===========================================================================
# COMPONENTS
# ===========================================================================
COMPONENTS_BODY = """  <section class="section">
    <div class="wrap split">
      <div class="split__media reveal"><img src="assets/img/site/components.jpg" alt="Component stock at WEL" loading="lazy"></div>
      <div class="split__body reveal">
        <span class="eyebrow">Components</span>
        <h2>Stock kept for courses and projects</h2>
        <p>A stock of components required for the basic electronics lab &mdash; resistors, capacitors and
          discrete devices such as diodes, transistors and LEDs &mdash; along with special-purpose ICs
          (analog and TTL/CMOS digital ICs, microcontrollers, ADC, DAC, RAM, EEPROM, EPROM, regulators)
          is maintained in the Wadhwani lab.</p>
        <p>Some components typically used in projects and competitions, such as stepper motors, are also
          available.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="inventory.html">Search the inventory</a>
          <a class="btn btn--outline" href="online-request.html">Raise a request</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Datasheets</span>
        <h2>Reference material by category</h2>
        <p>Datasheets for the parts held in the lab are grouped into the categories below. Ask the lab
          staff or check the inventory portal for the copy relevant to your part number.</p>
      </div>
      <div class="grid g3">
        <div class="lcard reveal"><span class="lcard__icon">{i_chip}</span><h3>ADC / DAC</h3>
          <p>Data converters held in stock for instrumentation and signal-chain projects.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_chip}</span><h3>Analog ICs</h3>
          <p>Op-amps, comparators, references and analog function blocks.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_chip}</span><h3>Digital ICs</h3>
          <p>TTL and CMOS logic families used across the digital circuits courses.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_board}</span><h3>Microcontrollers &amp; memory</h3>
          <p>Microcontrollers, EPROM, EEPROM and RAM devices.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_tool}</span><h3>Special components</h3>
          <p>Sensors, regulators, crystals, motors, displays and similar parts.</p></div>
        <div class="lcard lcard--red reveal"><span class="lcard__icon">{i_box}</span><h3>List of components available</h3>
          <p>The live list, with quantities and locations, is in the
             <a href="inventory.html">IITB WEL Inventory</a> portal.</p></div>
      </div>
    </div>
  </section>
""".format(i_chip=icon("chip"), i_board=icon("board"), i_tool=icon("tool"), i_box=icon("box"))


# ===========================================================================
# IITB WEL INVENTORY
# ===========================================================================
INVENTORY_BODY = """  <section class="section">
    <div class="wrap">
      <div class="grid g2" style="align-items:start">
        <div class="reveal">
          <span class="eyebrow">Component stock portal</span>
          <h2>Search stock, build a cart, submit as a team</h2>
          <p>The IITB WEL Inventory is the lab's component stock system. Project teams register once,
            search the component list by type, model number, description or storage location, add what
            they need to a request cart and submit it with a note. Lab staff review the request, and on
            approval the stock is decremented automatically.</p>
          <div class="btn-row">
            <a class="btn btn--red" href="{app}" target="_blank" rel="noopener">Open the inventory portal {i_ext}</a>
            <a class="btn btn--outline" href="components.html">About the components</a>
          </div>
          <div class="note note--red" style="margin-top:1.6rem">
            <strong>Inside the institute network.</strong> The portal runs on the lab server. If the link
            does not open, connect to the IIT Bombay network or VPN, or write to
            <a href="mailto:{email}">{email}</a>.
          </div>
        </div>

        <div class="reveal">
          <div class="table-wrap">
            <table>
              <thead><tr><th>What it holds</th><th>Detail</th></tr></thead>
              <tbody>
                <tr><td>Component type</td><td>Passives, discretes, analog and digital ICs, microcontrollers, memory, sensors, motors, displays</td></tr>
                <tr><td>Model number</td><td>Manufacturer part number as stocked</td></tr>
                <tr><td>Description</td><td>Free-text description of the part</td></tr>
                <tr><td>Location</td><td>Where the part is stored in the lab</td></tr>
                <tr><td>Quantity</td><td>Current stock, decremented on approval</td></tr>
                <tr><td>Reference link</td><td>Datasheet or supplier link where available</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">For project teams</span>
        <h2>How to raise a component request</h2>
      </div>
      <div class="grid g4">
        <div class="lcard reveal"><span class="lcard__icon">{i_people}</span><h3>1. Register your team</h3>
          <p>One registration per team: team name, every member's name and roll number, and one
             <strong>@iitb.ac.in</strong> email with a shared password.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_search}</span><h3>2. Search the stock</h3>
          <p>Filter by component type or search across model number, description and storage location.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_box}</span><h3>3. Add to cart</h3>
          <p>Set a quantity for each part and add it to your request cart. The cart lives with your team.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_clip}</span><h3>4. Submit &amp; collect</h3>
          <p>Add a note describing the project, submit, and track the status under <em>My Requests</em>.
             Collect from the lab once approved.</p></div>
      </div>
      <div class="note mt2 reveal" style="margin-top:2rem">
        <strong>One open request at a time.</strong> A team can have only one pending request; submit the
        next one after the current request has been approved or rejected. Requests are visible to the lab
        staff with the full team roster, so make sure member names and roll numbers are correct at
        registration.
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">For lab staff</span>
        <h2>What the admin side does</h2>
      </div>
      <div class="grid g3">
        <div class="lcard reveal"><span class="lcard__icon">{i_clip}</span><h3>Review requests</h3>
          <p>Pending, approved and rejected requests, each showing the team name and every member with
             their roll number. Approving issues the parts and decrements stock; stock is checked before
             the request goes through.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_box}</span><h3>Manage stock</h3>
          <p>Edit quantities in place, and see a low-stock list of everything at two units or fewer so
             reordering happens before a course needs the part.</p></div>
        <div class="lcard reveal"><span class="lcard__icon">{i_chip}</span><h3>Bulk import</h3>
          <p>Import the component list from an Excel workbook or a Google Sheet link. Columns map to
             type, model number, description, link, location and quantity.</p></div>
      </div>
      <div class="cta-band reveal" style="margin-top:2.6rem">
        <h2>Something missing from the stock?</h2>
        <p>If a part you need is not listed, or the quantity looks wrong, tell the lab staff rather than
           assuming it is unavailable &mdash; stock is updated as parts arrive.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="contact.html">Contact the lab</a>
          <a class="btn btn--ghost" href="online-request.html">Other online requests</a>
        </div>
      </div>
    </div>
  </section>
""".format(app=SITE["inventory_app"], email=SITE["email"], i_ext=icon("external"),
           i_people=icon("people"), i_search=icon("search"), i_box=icon("box"),
           i_clip=icon("clipboard"), i_chip=icon("chip"))


PAGES = [
    {
        "file": "resources.html", "nav": "resources.html", "sub": "resources.html",
        "title": "Resources | Wadhwani Electronics Laboratory",
        "desc": "Facilities, in-house development boards, instruments and components available at the "
                "Wadhwani Electronics Laboratory, IIT Bombay.",
        "hero": page_hero("Resources",
                          "Facilities, hardware and stock built up over two decades - and how to get "
                          "hold of any of it.",
                          [("Resources", "resources.html")],
                          "assets/img/site/madeinwel.png"),
        "body": RESOURCES_BODY,
    },
    {
        "file": "advanced-facilities.html", "nav": "resources.html", "sub": "advanced-facilities.html",
        "title": "Advanced Facilities in WEL Lab | Wadhwani Electronics Laboratory",
        "desc": "Thermal and climate chambers, 3D printers and scanner, laser cutter, milling machine, "
                "lathe, coil winding machine and ESD workstations at WEL, IIT Bombay.",
        "hero": page_hero("Advanced Facilities in WEL Lab",
                          "Chambers, printers, cutters and machines in the advanced measurements wing "
                          "and the Experiential Learning Laboratory.",
                          [("Resources", "resources.html"), ("Advanced Facilities", "advanced-facilities.html")],
                          "assets/img/facilities/climate-thermal-chamber.jpeg"),
        "body": FACILITIES_BODY,
    },
    {
        "file": "made-in-wel.html", "nav": "resources.html", "sub": "made-in-wel.html",
        "title": "Development Boards Made in WEL | Wadhwani Electronics Laboratory",
        "desc": "PicoIRIS, PT-51, Xen-10, the IQ Modulator, QMagPi and Krypton - development boards "
                "designed and manufactured in-house at WEL, IIT Bombay.",
        "hero": page_hero("Development Boards Made in WEL",
                          "Course hardware designed, built and supported in-house for more than a decade.",
                          [("Resources", "resources.html"), ("Made in WEL", "made-in-wel.html")],
                          "assets/img/site/madeinwel.png"),
        "body": BOARDS_BODY,
    },
    {
        "file": "instruments.html", "nav": "resources.html", "sub": "instruments.html",
        "title": "Instruments | Wadhwani Electronics Laboratory",
        "desc": "Signal generators, oscilloscopes, analyzers, multimeters and power equipment available "
                "at the Wadhwani Electronics Laboratory, IIT Bombay.",
        "hero": page_hero("Instruments",
                          "Routine bench instruments for teaching labs, and advanced instruments for "
                          "sensitive and high-frequency measurement.",
                          [("Resources", "resources.html"), ("Instruments", "instruments.html")],
                          "assets/img/instruments/signal-generators.jpeg"),
        "body": INSTRUMENTS_BODY,
    },
    {
        "file": "components.html", "nav": "resources.html", "sub": "components.html",
        "title": "Components | Wadhwani Electronics Laboratory",
        "desc": "Component stock at WEL - passives, discretes, analog and digital ICs, microcontrollers, "
                "memory, sensors, motors and displays, with datasheets.",
        "hero": page_hero("Components",
                          "Stock kept for the basic electronics lab, special-purpose ICs and the parts "
                          "projects and competitions ask for.",
                          [("Resources", "resources.html"), ("Components", "components.html")],
                          "assets/img/site/components.jpg"),
        "body": COMPONENTS_BODY,
    },
    {
        "file": "inventory.html", "nav": "resources.html", "sub": "inventory.html",
        "title": "IITB WEL Inventory | Wadhwani Electronics Laboratory",
        "desc": "Search the WEL component stock, build a request cart and submit it as a project team. "
                "The IITB WEL Inventory portal for students and lab staff.",
        "hero": page_hero("IITB WEL Inventory",
                          "The component stock portal: search what the lab holds, build a cart and "
                          "submit a request as a project team.",
                          [("Resources", "resources.html"), ("IITB WEL Inventory", "inventory.html")],
                          "assets/img/site/components.jpg"),
        "body": INVENTORY_BODY,
    },
]
