# -*- coding: utf-8 -*-
"""A detail page for each development board made in WEL, and one for the
Experiential Learning Laboratory.

Board feature lists come from the lab's own per-board pages; the PicoIRIS
specification table and the ELL equipment descriptions were transcribed from
the posters those pages carry, so the content is readable text here rather
than words locked inside a JPEG.
"""
from build import icon, page_hero

# ---------------------------------------------------------------------------
# Development boards
#   specs: either a list of bullet strings, or (group title, [(param, value)])
# ---------------------------------------------------------------------------
BOARDS = [
    {
        "slug": "xen10",
        "name": "Xen-10",
        "tagline": "ALTERA MAX 10 FPGA development board for advanced digital design "
                   "experiments and R&amp;D projects",
        "developers": "Vidur Shah, Mahesh B., Maheshwar M., Amit S.",
        "image": "assets/img/boards/xen10-detail.png",
        "card": "assets/img/boards/xen10.png",
        "desc": "Xen-10, the ALTERA MAX 10 FPGA development board designed and built at the "
                "Wadhwani Electronics Laboratory, IIT Bombay.",
        "intro": [
            "Xen-10 is used across the digital design courses at WEL and in R&amp;D projects, and "
            "like the rest of the course hardware it is designed and manufactured in-house.",
        ],
        "features": [
            "FPGA device: Altera MAX 10 (10M25SAE144C8G / 10M08SAE144C8G)",
            "USB connector for programming, JTAG interface for debugging",
            "8 on-board switches and 8 on-board LEDs",
            "4 push-buttons",
            "Header to connect external devices and boards",
            "16-pin connector for an LCD panel, OLED or any I<sup>2</sup>C interface device",
            "On-board 12-bit single-channel MCP4921 DAC",
            "On-board clocks of 1 Hz, 10 MHz and 50 MHz, with provision for an external clock "
            "source through the EXT CLK header",
        ],
        "tables": [],
        "courses": [("EE 214: Digital Circuits Lab", "course-ee214.html")],
    },
    {
        "slug": "pt51",
        "name": "PT-51",
        "tagline": "An 8051-based development board for introducing students to microprocessor "
                   "architecture",
        "developers": "Maheshwar Mangat, Geetanjali Shinde",
        "image": "assets/img/boards/pt-51.png",
        "card": "assets/img/boards/pt-51.png",
        "desc": "PT-51, the 8051-based microcontroller development board designed and built at the "
                "Wadhwani Electronics Laboratory, IIT Bombay.",
        "intro": [
            "PT-51 is built around the Microchip AT89C5131A and is the board students meet in the "
            "microprocessors lab. It is also the board WEL shipped to students' homes when the "
            "course ran online through the pandemic.",
        ],
        "features": [
            "AT89C5131A microcontroller IC with an 8051 core, 6 clocks per instruction",
            "Three 16-bit timer/counters: T0, T1 and T2",
            "256 bytes of scratchpad RAM",
            "16/32 KB on-chip flash EEPROM, in-system programming over USB",
            "Full-duplex enhanced UART (EUART)",
            "Programmable counter array with 16-bit counter, high-speed compare/capture, PWM and "
            "watchdog timer",
            "Keyboard interrupt interface on port P1 (8 bits)",
            "34 I/O pins, TWI (two-wire interface) at 400 kbit/s, SPI interface in master or slave mode",
            "24 MHz clock, power supply 2.7 V to 5.5 V",
            "4 DIP switches and 4 LEDs for simple I/O programs, plus a slot for an LCD",
        ],
        "tables": [],
        "courses": [("EE 337: Microprocessor Lab", "course-ee337.html")],
    },
    {
        "slug": "picoiris",
        "name": "PicoIRIS",
        "tagline": "Lab-in-a-box: oscilloscope, function generator and power supply on one board",
        "developers": "Ankur Agarwal",
        "image": "assets/img/boards/picoiris-board.png",
        "card": "assets/img/boards/picoiris.png",
        "desc": "PicoIRIS, an all-in-one lab-on-board combining oscilloscope, function generator "
                "and power supply, under development at the Wadhwani Electronics Laboratory.",
        "intro": [
            "PicoIRIS combines a function generator, an oscilloscope and a power supply in a "
            "fully-integrated, affordable and portable PCB-based instrument, which lets students "
            "work on electronics projects without having to be physically present in a lab.",
            "It connects to a laptop over USB and Bluetooth. The board is under development at WEL.",
        ],
        "features": [],
        "tables": [
            ("Oscilloscope", [
                ("Input frequency range", "1 Hz &ndash; 200 kHz"),
                ("Input voltage range", "&plusmn;10 V max."),
                ("Input channels", "2 single-ended"),
                ("Input impedance", "1 M&ohm; min."),
            ]),
            ("Function generator", [
                ("Output frequency range", "1 Hz &ndash; 200 kHz"),
                ("Output voltage range", "&plusmn;10 V max."),
                ("Output functions", "Sine, triangle, square"),
                ("Output channels", "2"),
            ]),
            ("Power supply", [
                ("Power source", "5 V USB phone charger"),
                ("Power connector", "Micro USB / USB-C / DC jack"),
                ("Variable DC output", "&minus;10 V to +10 V, programmable"),
                ("Current output", "100 mA max."),
            ]),
            ("Other features", [
                ("Connectivity", "USB and Bluetooth to a PC"),
                ("Digital I/O", "Yes"),
                ("FFT analysis", "Under development"),
            ]),
        ],
        "courses": [],
    },
    {
        "slug": "iq-modulator",
        "name": "IQ Modulator",
        "tagline": "Portable IQ transmitter board, 373 MHz to 1.6 GHz, for teaching communication "
                   "systems",
        "developers": "Manu T. S., Saurabh A., Maheshwar M.",
        "image": "assets/img/boards/iq-modulator.png",
        "card": "assets/img/boards/iq-modulator.png",
        "desc": "The IQ Modulator board designed and built at the Wadhwani Electronics Laboratory "
                "for the communications lab at IIT Bombay.",
        "intro": [
            "The IQ modulator board designed and developed in WEL up-converts a complex baseband "
            "signal to a passband IF or RF signal in the few-GHz range.",
        ],
        "features": [
            "Up-converts a complex baseband signal to a passband IF (intermediate frequency) or RF "
            "(radio frequency) signal in the few-GHz range",
            "An IQ demodulator &mdash; a commercial RTL-SDR dongle &mdash; down-converts the passband "
            "RF or IF signal back to complex baseband. It connects to the USB port of a computer and "
            "is processed with GNU Radio",
            "The open-source GNU Radio environment is used to build the communication blocks for "
            "transmission and reception on the computer",
        ],
        "tables": [],
        "courses": [("EE 340: Communications Lab", "course-ee340.html")],
    },
]

BOARDS_BY_SLUG = {b["slug"]: b for b in BOARDS}


def _features(items):
    if not items:
        return ""
    lis = "\n".join("          <li>%s</li>" % i for i in items)
    return """  <section class="section section--tight">
    <div class="wrap-narrow reveal">
      <h2>Features</h2>
      <ul class="feature-list">
%s
      </ul>
    </div>
  </section>
""" % lis


def _tables(groups):
    if not groups:
        return ""
    blocks = []
    for title, rows in groups:
        lis = "".join("<li><b>%s</b><span>%s</span></li>" % (k, v) for k, v in rows)
        blocks.append("""        <div class="spec-card reveal">
          <h3>%s</h3>
          <ul class="specs">%s</ul>
        </div>""" % (title, lis))
    return """  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Specifications</span>
        <h2>What it does</h2>
      </div>
      <div class="grid g2">
%s
      </div>
    </div>
  </section>
""" % "\n".join(blocks)


def _board_body(b):
    intro = "\n".join("      <p>%s</p>" % p for p in b["intro"])
    dev = ('      <p class="board-dev"><strong>Product developer%s:</strong> %s</p>'
           % ("s" if "," in b["developers"] else "", b["developers"])) if b["developers"] else ""
    course_links = ""
    if b["courses"]:
        links = " &middot; ".join('<a href="%s">%s</a>' % (h, t) for t, h in b["courses"])
        course_links = ('<div class="note" style="margin-top:1.6rem"><strong>Used in:</strong> %s</div>'
                        % links)

    return """  <section class="section section--tight">
    <div class="wrap split">
      <div class="split__media reveal">
        <img src="{img}" alt="{name}" loading="lazy">
      </div>
      <div class="split__body prose reveal">
{intro}
{dev}
{courses}
      </div>
    </div>
  </section>

{features}{tables}  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>Need this board for a project?</h2>
        <p>Development boards and the modules that go with them can be borrowed from WEL for a set
           period. Course kits are issued through the teaching lab staff.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="online-request.html#dev-boards">Request a board</a>
          <a class="btn btn--ghost" href="made-in-wel.html">All boards made in WEL</a>
        </div>
      </div>
    </div>
  </section>
""".format(img=b["image"], name=b["name"], intro=intro, dev=dev, courses=course_links,
           features=_features(b["features"]), tables=_tables(b["tables"]))


# ---------------------------------------------------------------------------
# Experiential Learning Laboratory
# ---------------------------------------------------------------------------
ELL_KIT = [
    ("Lathe machine", "assets/img/facilities/lathe.png",
     "A machining tool for shaping materials such as metal, wood and acrylic. It works on the "
     "principle of a rotating workpiece: the cutting tool feeds into the workpiece, which rotates "
     "and takes the required shape and size, removing unwanted material and leaving a cleanly "
     "shaped part."),
    ("Laser engraving and cutting", "assets/img/facilities/laser-cutter.jpeg",
     "An automatic laser machine that engraves and cuts material to the desired shape, with high "
     "precision and rapid cutting speeds. It cuts plywood, acrylic, paper, thermocol, MDF board and "
     "cardboard, and engraves acrylic, glass, leather, MDF board and marble."),
    ("3D printers", "assets/img/facilities/fdm-large.jpg",
     "In FFF 3D printers the filament is fed through a moving, heated extruder head and deposited "
     "on the growing work. The Julia Advance prints in a single material and the Julia Pro in two. "
     "Materials used are plastic filaments such as PLA, ABS and EVA."),
    ("Milling machine", "assets/img/facilities/milling.png",
     "The desktop milling machine uses rotary cutting tools driven by computer numerical control "
     "(CNC) to remove unwanted material and produce the desired workpiece."),
    ("FormBox vacuum former", "",
     "The FormBox is a desktop vacuum former that makes moulds and packaging trays from casting "
     "sheets, and can produce a shape within a minute."),
    ("3D scanner", "assets/img/facilities/3d-scanner.png",
     "The desktop 3D scanner creates a digital 3D model of an object within minutes. It uses the "
     "white-light method, which makes capturing objects from small to large easier and faster, and "
     "gives a high-resolution model in one click."),
]


def _ell_cards():
    out = []
    for name, img, text in ELL_KIT:
        media = ('<div class="card__media card__media--contain">'
                 '<img src="%s" alt="%s" loading="lazy"></div>' % (img, name)) if img else ""
        out.append("""        <article class="card reveal">
          {media}
          <div class="card__body">
            <h3>{name}</h3>
            <p>{text}</p>
          </div>
        </article>""".format(media=media, name=name, text=text))
    return "\n".join(out)


ELL_BODY = """  <section class="section section--tight">
    <div class="wrap split">
      <div class="split__media reveal">
        <img src="assets/img/site/ell.jpeg" alt="Inside the Experiential Learning Laboratory" loading="lazy">
      </div>
      <div class="split__body prose reveal">
        <p>The Experiential Learning Laboratory was inaugurated on <strong>14 February 2022</strong>
          by <strong>Dr. Hemant Kanakia</strong>, a Distinguished Alumnus of IIT Bombay. It holds a
          range of rapid prototyping equipment, put there to support hands-on learning and to
          encourage a spirit of making among students.</p>
        <p>Before the ELL, student projects were largely limited to basic printed circuit boards and
          rudimentary packaging. With a lathe, laser cutter, CNC mill, 3D printers, a 3D scanner and a
          vacuum former in the same room, a project can now go from an idea to a housed, finished
          prototype without leaving the lab &mdash; which is what lifted the technology readiness
          level of <a href="course-ee344.html">Electronics Design Lab</a> projects.</p>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">The equipment</span>
        <h2>What is in the room</h2>
        <p>Detailed models, work volumes and tolerances for each machine are on the
          <a href="advanced-facilities.html">advanced facilities</a> page.</p>
      </div>
      <div class="grid g3">
{cards}
      </div>
    </div>
  </section>

  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="wrap-narrow reveal" style="width:100%;padding:0;margin:0">
        <span class="eyebrow">Behind it</span>
        <h2>Dr. Hemant Kanakia and the Maker Bhavan Foundation</h2>
        <p>Dr. Hemant Kanakia, an alumnus of IIT Bombay Electrical Engineering from the batch of 1975,
          is the founder of the <strong>Maker Bhavan Foundation</strong>. The idea of setting up a
          collaborative classroom and an experiential learning laboratory &mdash; to move electrical
          engineering education towards outcome-based learning &mdash; came from him.</p>
        <p>The laboratory gives students access to world-class equipment, resources and knowledge, so
          that new practice can be folded into the existing engineering curriculum. It is the best
          platform in the department for developing the skills involved in actually creating a
          prototype.</p>
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="cta-band reveal">
        <h2>We are contributing towards developing a nation of innovators</h2>
        <p>Access to the prototyping equipment is arranged through the special facilities request.
           Students on project courses are inducted by the lab staff.</p>
        <div class="btn-row">
          <a class="btn btn--red" href="online-request.html#special-facilities">Request a facility</a>
          <a class="btn btn--ghost" href="advanced-facilities.html">Full equipment list</a>
        </div>
      </div>
    </div>
  </section>
""".format(cards=_ell_cards())


PAGES = [{
    "file": "facility-ell.html", "nav": "resources.html", "sub": "resources.html",
    "title": "Experiential Learning Laboratory | Wadhwani Electronics Laboratory",
    "desc": "The Experiential Learning Laboratory at WEL, IIT Bombay - lathe, laser cutter, CNC "
            "mill, 3D printers, 3D scanner and vacuum former for rapid prototyping.",
    "hero": page_hero("Experiential Learning Laboratory",
                      "Rapid prototyping equipment for hands-on learning, and a spirit of making.",
                      [("Resources", "resources.html"),
                       ("Experiential Learning Laboratory", "facility-ell.html")],
                      "assets/img/site/ell.jpeg"),
    "body": ELL_BODY,
}]

for _b in BOARDS:
    PAGES.append({
        "file": "board-%s.html" % _b["slug"],
        "nav": "resources.html", "sub": "made-in-wel.html",
        "title": "%s | Wadhwani Electronics Laboratory" % _b["name"],
        "desc": _b["desc"],
        "hero": page_hero(_b["name"], _b["tagline"],
                          [("Resources", "resources.html"),
                           ("Made in WEL", "made-in-wel.html"),
                           (_b["name"], "board-%s.html" % _b["slug"])],
                          "assets/img/site/madeinwel.png"),
        "body": _board_body(_b),
    })
