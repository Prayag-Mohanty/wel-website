# -*- coding: utf-8 -*-
"""One detail page per lab course.

Each entry in COURSES becomes a page named course-<slug>.html, linked from the
autumn and spring semester pages.  To edit a course, change its dict below -
the markup is generated from it.

Fields:
  code, title      as printed on the page and in the semester lists
  slug             file becomes course-<slug>.html
  semester         "Autumn" or "Spring" (drives the breadcrumb and the hero)
  term             free text shown under the title, e.g. "Autumn 2026"
  blurb            one line used on the semester page and as the meta description
  intro            list of paragraphs
  bullets          list of short points (may be empty)
  instructors      (name, role, email, phone, photo, profile_url)
  resources        (label, url) - the sidebar links on the current site
  staff            (name, role, photo)
  schedule         (caption, [header row, ...data rows]) or None
  figure           (image, caption) or None
"""
from build import SITE, icon, page_hero

INTERNAL_HOSTS = ("10.107.68.222", "10.107.68.191")


def _is_internal(url):
    return any(h in url for h in INTERNAL_HOSTS)


def _link(url, label):
    """Anchor, tagged when it only resolves inside the institute network."""
    if _is_internal(url):
        return ('<a href="%s" target="_blank" rel="noopener">%s '
                '<span class="tag-internal" title="Only reachable on the IIT Bombay network">'
                'internal</span></a>' % (url, label))
    external = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
    return '<a href="%s"%s>%s</a>' % (url, external, label)


# ===========================================================================
# Course data
# ===========================================================================
COURSES = [
    {
        "code": "EE 214", "title": "Digital Circuits Lab", "slug": "ee214",
        "semester": "Autumn", "term": "Autumn 2026",
        "blurb": "Combinational and sequential logic, flip-flops, counters, multiplexers and "
                 "microcontroller-based systems.",
        "intro": [
            "The Digital Circuits Laboratory (EE 214) is a hands-on lab course designed for "
            "undergraduate students in Electrical Engineering. It focuses on practical applications "
            "of digital logic design, covering topics such as combinational and sequential circuits, "
            "flip-flops, counters, multiplexers, and microcontroller-based systems.",
        ],
        "bullets": [],
        "instructors": [
            ("Prof. Saurabh Lodha", "Course Instructor", "slodha@ee.iitb.ac.in",
             "022-2576-7460 (O)", "assets/img/courses/saurabh-lodha.png",
             "https://www.ee.iitb.ac.in/web/people/saurabh-lodha/"),
        ],
        "resources": [
            ("Course Outline", "http://10.107.68.222/teaching_labs/WEL%20Site/EE214/OverviewCmos.pdf"),
            ("Lab Manual", "http://10.107.68.222/teaching_labs/WEL%20Site/EE214/Labsheets-2019/LabManual.pdf"),
            ("AFG Manual", "http://10.107.68.222/teaching_labs/WEL%20Site/EE214/Labsheets-2019/AFG.pdf"),
            ("DSO Manual", "http://10.107.68.222/teaching_labs/WEL%20Site/EE214/Labsheets-2019/Lab%20exercise_DSO_AFG.pdf"),
        ],
        "resource_note": "TA allotment for EE 214 is announced by the course staff each semester.",
        "staff": [
            ("Mahesh Ashok Bhaganagare", "Technical Officer", "assets/img/team/mahesh-bhaganagare.jpg"),
            ("Amit Shetye", "Sr. Technical Superintendent", "assets/img/team/amit-shetye.jpg"),
            ("Sadanand Sahadev Sawant", "Sr. Mechanic", "assets/img/team/sadanand-sawant.jpg"),
            ("Mangesh U. Ingle", "Sr. Project Assistant", "assets/img/team/mangesh-ingle.jpg"),
            ("Sandhya Samadhan Birare", "Lab Attendant", "assets/img/team/sandhya-birare.jpg"),
        ],
        "schedule": ("Practical lab experiments schedule, Autumn 2026", [
            ["Lab No.", "Experiment", "Week", "Material"],
            ["&mdash;", "Course Outline", "27 July &ndash; 2 August",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee230/Labsheets-2019/EE%20230-course%20outline_2019%20.pdf", "Course Outline")],
            ["Lab 1", "LAB-1 Material", "3 August &ndash; 9 August", ""],
            ["Lab 2", "LAB-2 Material", "10 August &ndash; 16 August", ""],
            ["Lab 3", "LAB-3 Material", "17 August &ndash; 23 August", ""],
            ["Lab 4", "LAB-4 Material", "24 August &ndash; 30 August", ""],
            ["Lab 5", "LAB-5 Material", "", ""],
            ["Lab 6", "LAB-6 Material", "", ""],
            ["Lab 7", "LAB-7 Material", "", ""],
        ]),
        "figure": None,
    },
    {
        "code": "EE 236", "title": "Electronic Devices Lab", "slug": "ee236",
        "semester": "Autumn", "term": "Autumn 2026",
        "blurb": "PN junctions, MOSFETs, BJTs and optoelectronic devices - characterisation, "
                 "circuit implementation and applications.",
        "intro": [
            "The Electronic Devices Laboratory (EE 236) is a course designed to help students "
            "understand the fundamentals of semiconductor devices and their applications. It covers "
            "key concepts such as PN junctions, MOSFETs, BJTs, and optoelectronic devices, with "
            "experiments focusing on device characterization, circuit implementation, and real-world "
            "applications.",
            "Students work with oscilloscopes, signal generators, and specialized testing equipment "
            "to analyze device behaviour under different conditions.",
        ],
        "bullets": [],
        "instructors": [
            ("Prof. Apurba Laha", "Course Instructor", "laha@ee.iitb.ac.in",
             "022-2576-9408 (O)", "assets/img/people/apurba-laha.png",
             "https://www.ee.iitb.ac.in/web/people/apurba-laha/"),
            ("Prof. Pradeep R. Nair", "Course Instructor", "prnair@ee.iitb.ac.in",
             "022-2576-9447 (O)", "assets/img/courses/pradeep-nair.png",
             "https://www.ee.iitb.ac.in/web/people/pradeep-r-nair/"),
        ],
        "resources": [],
        "resource_note": "Every handout, pre-lab exercise and slide deck for this course is linked "
                         "from the schedule below.",
        "staff": [],
        "schedule": ("Practical lab experiments schedule, Autumn 2026", [
            ["Lab No.", "Experiment", "Week", "Material"],
            ["Lab 0",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Course%20Introduction.pptx", "Course introduction slide")
             + " &middot; " +
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Course%20Outline.pptx", "Course outline slide"),
             "28 July &ndash; 3 August",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Lab0_Handout.zip", "Lab 0 handout")],
            ["Lab 1",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Introduction%20to%20solid%20state%20lighting.pptx", "Introduction to solid state lighting"),
             "4 &ndash; 10 August",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/prelab1.zip", "Pre-lab 1 exercise")
             + " &middot; " +
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Lab1.zip", "Lab 1 material")],
            ["Lab 2",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Introduction%20to%20PIN%20diode%20and%20its%20application%20%5bPDF%5d.pdf", "Introduction to PIN diode and its application"),
             "11 &ndash; 17 August",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Exp2_PIN_diode.pdf", "Lab 2 handout")],
            ["Lab 3",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Introduction%20to%20photodiodes%20and%20its%20application.pptx", "Introduction to photodiodes and applications"),
             "18 &ndash; 24 August",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Lab%203_handout.pdf", "Lab 3 handout")],
            ["Lab 4",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Introduction%20to%20schottky%20diode.pptx", "Introduction to Schottky diode"),
             "25 &ndash; 31 August",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Lab4_handout.pdf", "Lab 4 handout")],
            ["Lab 5",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Introduction%20to%20solar%20cell.pptx", "Introduction to solar cell"),
             "1 &ndash; 7 September",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Prelab_simulation.zip", "Pre-lab simulation")
             + " &middot; " +
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/solarcell_Experiments.zip", "Lab 5 handout")],
            ["Lab 6", "Lab 6 submission", "8 &ndash; 14 September", ""],
            ["&mdash;", "Mid-semester", "15 &ndash; 21 September", ""],
            ["Lab 7",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Introduction%20to%20BJT%20and%20HBT.pptx", "Introduction to BJT and HBT"),
             "22 &ndash; 28 September",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/BJT_handout.pdf", "Lab 7 handout")],
            ["Lab 8",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/Introduction%20to%20NMOS,%20PMOS,%20CMOS%20and%20MOSCAP.pdf", "Introduction to NMOS, PMOS, CMOS and MOSCAP"),
             "29 September &ndash; 5 October",
             _link("http://10.107.68.222/teaching_labs/WEL%20Site/ee236/ee236_2025/devices/NMOS_Handouts.zip", "Lab 8 handout")],
        ]),
        "figure": None,
    },
    {
        "code": "EE 340", "title": "Communications Lab", "slug": "ee340",
        "semester": "Autumn", "term": "Autumn 2026",
        "blurb": "Modulation, error correction, digital signal processing and wireless protocols, "
                 "with SDR and the in-house IQ Modulator board.",
        "intro": [
            "The Communications Laboratory (EE 340) is a hands-on course designed to provide students "
            "with practical experience in communication systems and signal processing. It covers key "
            "topics such as modulation techniques, error correction, digital signal processing, and "
            "wireless communication protocols.",
        ],
        "bullets": [
            "Experiments on AM/FM modulation, phase shift keying (PSK) and frequency shift keying (FSK).",
            "Practical implementation of communication networks and RF electronics.",
            "Use of software-defined radio (SDR) and MATLAB simulations for signal analysis.",
        ],
        "instructors": [
            ("Prof. Rajbabu Velmurugan", "Lab In-charge", "rajbabu@ee.iitb.ac.in",
             "022-2576-7444 (O) &middot; 022-2576-8444 (R)", "assets/img/courses/rajbabu-velmurugan.png",
             "https://www.ee.iitb.ac.in/web/people/rajbabu-velmurugan/"),
        ],
        "resources": [
            ("Course details and labsheets", "http://10.107.68.222/teaching_labs/"),
            ("GNU Radio - what is it?", "https://wiki.gnuradio.org/index.php/What_is_GNU_Radio%3F"),
            ("RTL-SDR dongle quick start guide", "http://www.rtl-sdr.com/rtl-sdr-quick-start-guide/"),
            ("IQ Modulator board details", "made-in-wel.html#iq-modulator"),
        ],
        "resource_note": "",
        "staff": [
            ("Maheshwar Mangat", "Sr. Technical Superintendent", "assets/img/team/maheshwar-mangat.jpg"),
            ("Suraj Suresh Sarfare", "Junior Mechanic", "assets/img/team/suraj-sarfare.jpg"),
            ("Sunil Sheshrao Raut", "Project Attendant", "assets/img/team/sunil-raut.jpg"),
            ("Vijay Vilas Patil", "Project Assistant", "assets/img/team/vijay-patil.jpg"),
        ],
        "schedule": None,
        "figure": ("assets/img/courses/iq-modulator-board.jpg",
                   "The IQ Modulator board, designed and built at WEL, is used throughout this course."),
    },
    {
        "code": "EE 230", "title": "Analog Circuits Lab", "slug": "ee230",
        "semester": "Spring", "term": "Spring 2026",
        "blurb": "Operational amplifiers, BJTs and FETs, and feedback systems, measured on the "
                 "standard WEL bench.",
        "intro": [
            "The Analog Circuits Laboratory (EE 230) is a core lab course designed for undergraduate "
            "students in Electrical Engineering. It focuses on hands-on experiments with analog "
            "circuit components, including operational amplifiers (op-amps), transistors (BJTs and "
            "FETs), and feedback systems.",
        ],
        "bullets": [],
        "instructors": [
            ("Prof. Sandip Mondal", "Course Instructor", "sandip@ee.iitb.ac.in",
             "+91-22-2576-9427 (O)", "assets/img/courses/sandip-mondal.png",
             "https://www.ee.iitb.ac.in/web/people/sandip-mondal/"),
        ],
        "resources": [
            ("Course Outline", "http://10.107.68.222/teaching_labs/WEL%20Site/ee230/Labsheets-2019/EE%20230-course%20outline_2019%20.pdf"),
            ("LaTeX and Xcircuit help", "http://10.107.68.222/teaching_labs/WEL%20Site/ee230/Labsheets-2019/Latex%20and%20Xcircuit%20Help.zip"),
        ],
        "resource_note": "Monday and Tuesday batch lists, TA allotment and TA contact details are "
                         "published by the course staff each semester.",
        "staff": [
            ("Mahesh Ashok Bhaganagare", "Technical Officer", "assets/img/team/mahesh-bhaganagare.jpg"),
            ("Ankur Agarwal", "Jr. Technical Superintendent", "assets/img/team/ankur-agarwal.jpg"),
            ("Sadanand Sahadev Sawant", "Sr. Mechanic", "assets/img/team/sadanand-sawant.jpg"),
            ("Mangesh U. Ingle", "Sr. Project Assistant", "assets/img/team/mangesh-ingle.jpg"),
            ("Sandhya Samadhan Birare", "Lab Attendant", "assets/img/team/sandhya-birare.jpg"),
        ],
        "schedule": None,
        "figure": None,
    },
    {
        "code": "EE 344", "title": "Electronics Design Lab-I", "slug": "ee344",
        "semester": "Spring", "term": "Spring 2026",
        "blurb": "The capstone design course: take an electronic product from concept to working "
                 "prototype over a semester.",
        "intro": [
            "The <strong>Electronics Design Lab (EDL)</strong> course, a capstone design course at the "
            "Department of Electrical Engineering, IIT Bombay, empowers students to develop electronic "
            "products from concept to prototype. The introduction of the Experiential Learning Lab "
            "(ELL) significantly enhanced the curriculum and the technology readiness level (TRL) of "
            "student project prototypes. ELL has facilities for 3D printing, 3D scanning, desktop CNC "
            "milling, lathe, laser cutting and vacuum forming.",
            "Previously limited to basic printed circuit boards (PCBs) and rudimentary packaging, EDL "
            "now fosters innovation through access to advanced PCB fabrication and rapid prototyping "
            "tools. The upgraded facilities enable students to create more impactful prototypes, "
            "bridging theory with hands-on application-driven problem solving, and training them to "
            "become innovators.",
        ],
        "bullets": [
            "EDL has an enrollment of more than 200 students in each batch and runs for around 15 weeks.",
            "Students are expected to form their own groups of four or five students.",
            "Each student group is expected to spend approximately 30 person-hours per week on the project.",
        ],
        "instructors": [
            ("Prof. Siddharth Tallur", "Course Instructor", "stallur@ee.iitb.ac.in",
             "022-2576-9422 (O)", "assets/img/courses/siddharth-tallur.png",
             "https://www.ee.iitb.ac.in/web/people/siddharth-tallur/"),
            ("Prof. Satish Mulleti", "Course Instructor", "satishmulleti@ee.iitb.ac.in",
             "", "assets/img/courses/satish-mulleti.jpg",
             "https://www.ee.iitb.ac.in/web/people/satish-mulleti/"),
            ("Prof. P. C. Pandey", "Course Instructor", "pcpandey@ee.iitb.ac.in",
             "022-2572-3707 (O)", "assets/img/courses/pc-pandey.jpg",
             "https://www.ee.iitb.ac.in/~pcpandey/"),
            ("Prof. Apurba Bhattacharya", "Course Instructor", "apurbabhattacharya@ee.iitb.ac.in",
             "022-2576-7417 (O)", "assets/img/courses/apurba-bhattacharya.jpg",
             "https://www.ee.iitb.ac.in/web/people/apurba-narayan-bhattacharya/"),
            ("Prof. Apurba Laha", "Course Instructor", "laha@ee.iitb.ac.in",
             "022-2576-9408 (O)", "assets/img/people/apurba-laha.png",
             "https://www.ee.iitb.ac.in/web/people/apurba-laha/"),
            ("Prof. Debanjan Bhowmik", "Course Instructor", "debanjan@ee.iitb.ac.in",
             "022-2576-9429 (O)", "assets/img/courses/debanjan-bhowmik.jpg",
             "https://www.ee.iitb.ac.in/web/people/debanjan-bhowmik/"),
            ("Prof. Jayanta Mukherjee", "Course Instructor", "jayanta@ee.iitb.ac.in",
             "022-2576-7479 (O)", "assets/img/courses/jayanta-mukherjee.jpg",
             "https://www.ee.iitb.ac.in/web/people/jayanta-mukherjee/"),
            ("Prof. Anil Kottantharayil", "Course Instructor", "anilkg@ee.iitb.ac.in",
             "022-2576-7438 (O)", "assets/img/courses/anil-kottantharayil.png",
             "https://www.ee.iitb.ac.in/web/people/anil-kottantharayil/"),
            ("Prof. Himanshu Bahirat", "Course Instructor", "hjbahirat@ee.iitb.ac.in",
             "022-2576-9415 (O)", "assets/img/courses/himanshu-bahirat.jpg",
             "https://www.ee.iitb.ac.in/web/people/himanshu-j-bahirat/"),
        ],
        "resources": [
            ("Labsheets", "http://10.107.68.222/teaching_labs/EDL/Labsheets/"),
            ("Resources for TIVA-C", "http://10.107.68.222/teaching_labs/EDL/Tiva_c"),
            ("Resources for Aurum", "http://10.107.68.222/teaching_labs/EDL/Aurum"),
            ("Resources for PCB design", "http://10.107.68.222/teaching_labs/EDL/PCB_Design"),
            ("Project ideas", "http://10.107.68.222/teaching_labs/EDL/project_ideas"),
            ("Template for project proposal", "http://10.107.68.222/teaching_labs/EDL/project_template"),
            ("Component purchase approval form", "http://10.107.68.222/teaching_labs/EDL/Approval_Form.doc"),
        ],
        "resource_note": "Group allotment, the course timeline and the archive of past project "
                         "reports are published by the course staff each semester.",
        "staff": [
            ("Maheshwar Mangat", "Sr. Technical Superintendent", "assets/img/team/maheshwar-mangat.jpg"),
            ("Ankur Agarwal", "Jr. Technical Superintendent", "assets/img/team/ankur-agarwal.jpg"),
            ("Suraj Suresh Sarfare", "Junior Mechanic", "assets/img/team/suraj-sarfare.jpg"),
            ("Mangesh U. Ingle", "Sr. Project Assistant", "assets/img/team/mangesh-ingle.jpg"),
            ("Sunil Sheshrao Raut", "Project Attendant", "assets/img/team/sunil-raut.jpg"),
            ("Vijay Vilas Patil", "Project Assistant", "assets/img/team/vijay-patil.jpg"),
        ],
        "schedule": None,
        "figure": None,
    },
    {
        "code": "EE 616", "title": "Electronics Systems Design", "slug": "ee616",
        "semester": "Spring", "term": "Spring 2026",
        "blurb": "Analog and digital circuit design, signal conditioning, instrumentation and "
                 "PCB layout.",
        "intro": [
            "The Electronics Systems Design (EE 616) course focuses on the design and implementation "
            "of electronic systems, covering both analog and digital circuit design, signal "
            "conditioning, instrumentation, and PCB layout.",
        ],
        "bullets": [],
        "instructors": [
            ("Prof. Laxmeesha Somappa", "Course Instructor", "laxmeesha@ee.iitb.ac.in",
             "022-2576-7490 (O)", "assets/img/courses/laxmeesha-somappa.png",
             "https://www.ee.iitb.ac.in/web/people/laxmeesha-somappa/"),
        ],
        "resources": [],
        "resource_note": "Course material for EE 616 is distributed by the course instructor.",
        "staff": [],
        "schedule": None,
        "figure": None,
    },
    {
        "code": "EE 712", "title": "Embedded Systems Design Lab", "slug": "ee712",
        "semester": "Spring", "term": "Spring 2026 &middot; PG course",
        "blurb": "ARM Cortex architecture, ADC/DAC interfacing, serial protocols, RTOS and SoC "
                 "design on TIVA-C and Zynq-7000.",
        "intro": [
            "The Embedded Systems Design (EE 712) course focuses on the architecture, programming, "
            "and interfacing of embedded systems. It covers topics such as ARM Cortex-A8/A9 "
            "architecture, ADC/DAC interfacing, serial communication protocols (SPI, I2C, UART, CAN, "
            "USB), embedded software development, and SoC design.",
        ],
        "bullets": [
            "Hands-on labs with TIVA-C and Zynq-7000 SoC for hardware accelerators.",
            "Study of real-time operating systems (RTOS), device drivers and memory subsystems.",
            "Practical implementation of multi-standard I/Os, high-speed transceivers and embedded networking.",
            "Faculty-led research in low-power embedded systems and FPGA-based designs.",
        ],
        "instructors": [
            ("Prof. P. C. Pandey", "Course Instructor", "pcpandey@ee.iitb.ac.in",
             "022-2576-7445 (O)", "assets/img/courses/pc-pandey-712.jpg", ""),
            ("Prof. Dinesh K. Sharma", "Course Instructor", "dinesh@ee.iitb.ac.in",
             "022-2576-7432 (O)", "assets/img/courses/dinesh-sharma.jpg", ""),
        ],
        "resources": [
            ("Installation of Code Composer Studio", "http://10.107.68.222/teaching_labs/ee712/CCS_Installation/CCS_TivaWare.pdf"),
            ("Download Code Composer Studio", "http://10.107.68.222/teaching_labs/ee712/CCS.zip"),
            ("TIVA-C user manual", "http://10.107.68.222/teaching_labs/ee712/UserManualTiva.pdf"),
            ("TIVA-C supporting documents", "http://10.107.68.222/teaching_labs/ee712/supporting%20documents"),
        ],
        "resource_note": "The lab schedule is announced by the course staff each semester.",
        "staff": [],
        "schedule": None,
        "figure": None,
    },
    {
        "code": "EE 337", "title": "Microprocessor Lab", "slug": "ee337",
        "semester": "Spring", "term": "Spring 2026",
        "blurb": "Microprocessor architecture, assembly programming and peripheral interfacing on "
                 "the in-house PT-51 board.",
        "intro": [
            "The Microprocessor Laboratory (EE 337) is a hands-on course designed to teach students "
            "microprocessor architecture, assembly programming, and peripheral interfacing. It covers "
            "both software and hardware experiments.",
            "This lab provides a practical foundation for embedded systems and digital hardware design.",
        ],
        "bullets": [
            "8085 microprocessor kit for learning instruction sets.",
            "8051 microcontroller development board for assembly programming.",
            "Peripheral interfacing with devices such as LCD displays, keyboards, stepper motors and ADC chips.",
            "USART (8251) communication experiments.",
            "PIC microcontroller-based projects.",
        ],
        "instructors": [
            ("Prof. Sachin Patkar", "Course Instructor", "patkar@ee.iitb.ac.in",
             "+91-22-2576-7490 (O)", "assets/img/courses/sachin-patkar.png",
             "https://www.ee.iitb.ac.in/web/people/sachin-patkar/"),
        ],
        "resources": [
            ("PT-51 board details", "made-in-wel.html#pt-51"),
        ],
        "resource_note": "The practical lab experiments schedule for Spring 2026 is published by the "
                         "course staff each semester.",
        "staff": [
            ("Mahesh Ashok Bhaganagare", "Technical Officer", "assets/img/team/mahesh-bhaganagare.jpg"),
            ("Amit Shetye", "Sr. Technical Superintendent", "assets/img/team/amit-shetye.jpg"),
            ("Sadanand Sahadev Sawant", "Sr. Mechanic", "assets/img/team/sadanand-sawant.jpg"),
            ("Mangesh U. Ingle", "Sr. Project Assistant", "assets/img/team/mangesh-ingle.jpg"),
            ("Sandhya Samadhan Birare", "Lab Attendant", "assets/img/team/sandhya-birare.jpg"),
        ],
        "schedule": None,
        "figure": None,
    },
]

COURSES_BY_SEMESTER = {
    "Autumn": [c for c in COURSES if c["semester"] == "Autumn"],
    "Spring": [c for c in COURSES if c["semester"] == "Spring"],
}


# ===========================================================================
# Rendering
# ===========================================================================
def _instructors(rows):
    out = []
    for name, role, email, phone, photo, profile in rows:
        heading = ('<a href="%s" target="_blank" rel="noopener">%s</a>' % (profile, name)) if profile else name
        phone_line = '<div>%s<span>%s</span></div>' % (icon("phone"), phone) if phone else ""
        out.append("""        <article class="person reveal">
          <div class="person__photo"><img src="{photo}" alt="{name}" loading="lazy"></div>
          <div class="person__body">
            <h4>{heading}</h4>
            <span class="person__role">{role}</span>
            <div class="person__contact">
              <div>{i_mail}<a href="mailto:{email}">{email}</a></div>
              {phone_line}
            </div>
          </div>
        </article>""".format(photo=photo, name=name, heading=heading, role=role,
                             email=email, phone_line=phone_line, i_mail=icon("mail")))
    return "\n".join(out)


def _staff(rows):
    out = []
    for name, role, photo in rows:
        out.append("""        <article class="person reveal">
          <div class="person__photo"><img src="{photo}" alt="{name}" loading="lazy"></div>
          <div class="person__body">
            <h4>{name}</h4>
            <span class="person__role">{role}</span>
          </div>
        </article>""".format(photo=photo, name=name, role=role))
    return "\n".join(out)


def _schedule(sched):
    if not sched:
        return ""
    caption, rows = sched
    head = "".join("<th>%s</th>" % c for c in rows[0])
    body = []
    for r in rows[1:]:
        body.append("<tr>%s</tr>" % "".join("<td>%s</td>" % (c or "&mdash;") for c in r))
    return """  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Schedule</span>
        <h2>{caption}</h2>
      </div>
      <div class="table-wrap reveal">
        <table>
          <thead><tr>{head}</tr></thead>
          <tbody>
            {body}
          </tbody>
        </table>
      </div>
    </div>
  </section>
""".format(caption=caption, head=head, body="\n            ".join(body))


def _resources(course):
    items = course["resources"]
    note = course.get("resource_note", "")
    if not items and not note:
        return ""
    links = "\n".join(
        '            <li>%s</li>' % _link(url, label) for label, url in items
    )
    list_html = '<ul class="res-list">\n%s\n          </ul>' % links if items else ""
    note_html = '<div class="note" style="margin-top:%s">%s</div>' % (
        "1.4rem" if items else "0", note) if note else ""
    internal = any(_is_internal(u) for _, u in items)
    internal_note = ("""          <p style="font-size:.88rem;color:var(--muted);margin-top:1rem">
            Links marked <span class="tag-internal">internal</span> are hosted on the lab server and
            open only from the IIT Bombay network.</p>""" if internal else "")
    return """  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Course resources</span>
        <h2>Material and links</h2>
      </div>
      <div class="reveal">
          {list_html}
{internal_note}
          {note_html}
      </div>
    </div>
  </section>
""".format(list_html=list_html, note_html=note_html, internal_note=internal_note)


def _figure(fig):
    if not fig:
        return ""
    src, caption = fig
    return """      <figure class="course-figure reveal">
        <img src="%s" alt="%s" loading="lazy">
        <figcaption>%s</figcaption>
      </figure>
""" % (src, caption, caption)


def _body(course):
    intro = "\n".join("        <p>%s</p>" % p for p in course["intro"])
    bullets = ""
    if course["bullets"]:
        bullets = "        <ul>\n%s\n        </ul>" % "\n".join(
            "          <li>%s</li>" % b for b in course["bullets"])

    instructors = ""
    if course["instructors"]:
        instructors = """  <section class="section section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Teaching</span>
        <h2>Course instructor%s</h2>
      </div>
      <div class="grid g4">
%s
      </div>
    </div>
  </section>
""" % ("s" if len(course["instructors"]) > 1 else "", _instructors(course["instructors"]))

    staff = ""
    if course["staff"]:
        staff = """  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Lab support</span>
        <h2>Supporting staff</h2>
        <p>WEL staff who run this lab day to day.</p>
      </div>
      <div class="grid g4">
%s
      </div>
    </div>
  </section>
""" % (_staff(course["staff"]))

    sem_href = "%s-semester.html" % course["semester"].lower()
    return """  <section class="section section--tight">
    <div class="wrap-narrow prose reveal">
{intro}
{bullets}
    </div>
{figure}  </section>

{instructors}{schedule}{resources}{staff}  <section class="section section--tight">
    <div class="wrap">
      <div class="btn-row reveal">
        <a class="btn btn--outline" href="{sem_href}">All {sem} semester courses</a>
        <a class="btn btn--outline" href="teaching-labs.html">Teaching labs</a>
        <a class="btn btn--outline" href="contact.html">Ask the lab</a>
      </div>
    </div>
  </section>
""".format(intro=intro, bullets=bullets, figure=_figure(course["figure"]),
           instructors=instructors, schedule=_schedule(course["schedule"]),
           resources=_resources(course), staff=staff,
           sem_href=sem_href, sem=course["semester"].lower())


PAGES = []
for _c in COURSES:
    _sem_href = "%s-semester.html" % _c["semester"].lower()
    PAGES.append({
        "file": "course-%s.html" % _c["slug"],
        "nav": "teaching-labs.html", "sub": _sem_href,
        "title": "%s: %s | Wadhwani Electronics Laboratory" % (_c["code"], _c["title"]),
        "desc": "%s %s at the Wadhwani Electronics Laboratory, IIT Bombay. %s"
                % (_c["code"], _c["title"], _c["blurb"]),
        "hero": page_hero(
            "%s: %s" % (_c["code"], _c["title"]),
            _c["blurb"],
            [("Teaching Labs", "teaching-labs.html"),
             ("%s Semester" % _c["semester"], _sem_href),
             ("%s" % _c["code"], "course-%s.html" % _c["slug"])],
            "assets/img/site/lab-sessions.jpg"),
        "body": _body(_c),
    })
