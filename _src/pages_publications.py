# -*- coding: utf-8 -*-
"""Publications from WEL.

Every DOI below was resolved through Crossref and checked against the paper
title before being used, so a link goes to the paper it claims to. Three
entries - the WRTLT workshop paper and the two FIRE 2020 working notes - are
not in Crossref; rather than guess at a DOI they carry a title search, marked
as such.

  (authors, title, venue, year, doi, note)
  doi empty  -> a Google Scholar title search is offered instead
"""
from build import icon, page_hero

PUBLICATIONS = [
    # ---- 2022
    ("V. Malviya et al.",
     "Edge-compatible convolutional autoencoder implemented on FPGA for anomaly detection in "
     "vibration condition-based monitoring",
     "IEEE Sensors Letters, vol. 6, no. 4, art. no. 7001104", 2022,
     "10.1109/lsens.2022.3159972", ""),
    ("S. Narang et al.",
     "Field programmable gate array (FPGA) based programmable digital emulator of vibratory "
     "micro-electro-mechanical systems (MEMS) gyroscopes",
     "Review of Scientific Instruments, vol. 93, 035003", 2022,
     "10.1063/5.0065642", ""),
    ("R. Nandeshwar et al.",
     "Molecular imprinting with polyaniline on ENIG finish PCB electrodes for electrochemical "
     "detection of melamine",
     "IEEE Sensors Journal, vol. 22, no. 3, pp. 1898&ndash;1904", 2022,
     "10.1109/jsen.2021.3137515", ""),

    # ---- 2021
    ("S. Narang et al.",
     "A reconfigurable hardware emulator of MEMS gyroscopes with built-in error source models",
     "Joint Conference of the European Frequency &amp; Time Forum and IEEE International Frequency "
     "Control Symposium (EFTF-IFCS), July", 2021,
     "10.1109/eftf/ifcs52194.2021.9604312", ""),
    ("I. Mukherjee et al.",
     "Light-weight CNN enabled edge-based framework for machine health diagnosis",
     "IEEE Access, vol. 9, pp. 84375&ndash;84386", 2021,
     "10.1109/access.2021.3088237", ""),
    ("D. Tamhane et al.",
     "Feature engineering of time-domain signals based on principal component analysis for rebar "
     "corrosion assessment using pulse eddy current",
     "IEEE Sensors Journal, vol. 21, no. 19, pp. 22086&ndash;22093", 2021,
     "10.1109/jsen.2021.3103545", ""),
    ("M. S. Kumar et al.",
     "Electrochemical sensing of SARS-CoV-2 amplicons with PCB electrodes",
     "Sensors and Actuators B: Chemical, vol. 343, 130169", 2021,
     "10.1016/j.snb.2021.130169", ""),

    # ---- 2020
    ("P. Singh et al.",
     "Assisting ensemble of transformers with random transliteration",
     "12th meeting of the Forum for Information Retrieval Evaluation, Hyderabad", 2020,
     "", ""),
    ("P. Singh et al.",
     "Joint multitask learning of multilingual hate speech and offensive content detection system",
     "12th meeting of the Forum for Information Retrieval Evaluation, Hyderabad", 2020,
     "", ""),
    ("V. S. Vineesh et al.",
     "Enhanced design debugging with assistance from guidance-based model checking",
     "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems", 2020,
     "10.1109/tcad.2020.3011039", ""),
    ("R. Shinde et al.",
     "Aquila: A methodology for achieving fine-grained bug localization during design verification",
     "20th Workshop on RTL and High-Level Testing (WRTLT), January", 2020,
     "", ""),
    ("V. S. Vineesh et al.",
     "Analyzing hardware security properties of processors through model checking",
     "33rd International Conference on VLSI Design and 19th International Conference on Embedded "
     "Systems, January", 2020,
     "10.1109/vlsid49098.2020.00036", ""),

    # ---- 2019
    ("K. Mistry et al.",
     "Audio encryption through synchronization of chaotic oscillator circuits: Teaching non-linear "
     "dynamics through simple electrical circuits",
     "American Journal of Physics, vol. 87, no. 12, pp. 1004&ndash;1013", 2019,
     "10.1119/10.0000024", ""),
    ("V. S. Vineesh et al.",
     "Orion: A technique to prune state space search directions for guidance-based formal "
     "verification",
     "IEEE 28th Asian Test Symposium (ATS), pp. 123&ndash;1235, December", 2019,
     "10.1109/ats47505.2019.00023", ""),

    # ---- 2018
    ("J. Joy et al.",
     "Capacitance-voltage profiling of MOS capacitors: A case study of hands-on semiconductor "
     "testing for an undergraduate laboratory",
     "American Journal of Physics, vol. 86, p. 787", 2018,
     "10.1119/1.5052360", "Featured on the journal cover"),

    # ---- 2013
    ("S. Agrawal et al.",
     "An introductory lab course in digital design &mdash; onsite and online laboratory",
     "IEEE Global Engineering Education Conference (EDUCON), Berlin", 2013,
     "10.1109/educon.2013.6530186", ""),
    ("D. Ghosh et al.",
     "A portable solution for microcontroller laboratories",
     "IEEE Global Engineering Education Conference (EDUCON), Berlin", 2013,
     "10.1109/educon.2013.6530179", ""),
    ("J. Jinu et al.",
     "An approach to complement electronics courses using virtual environment",
     "IEEE Global Engineering Education Conference (EDUCON), Berlin", 2013,
     "10.1109/educon.2013.6530185", ""),

    # ---- 2012
    ("S. Shelke et al.",
     "A remote lab for real-time digital signal processing",
     "EDERC 2012, Amsterdam, September", 2012,
     "10.1109/ederc.2012.6532269", ""),
    ("M. P. Date et al.",
     "e-Prayog: A new paradigm in electronics laboratories",
     "IEEE International Conference on Technology-Enhanced Education (ICTEE), Trivandrum", 2012,
     "10.1109/ictee.2012.6208673", ""),
]


def _scholar(title):
    import urllib.parse
    plain = title.replace("&ndash;", "-").replace("&mdash;", "-").replace("&amp;", "and")
    return "https://scholar.google.com/scholar?q=" + urllib.parse.quote('"%s"' % plain)


def _entries():
    out = []
    current_year = None
    for authors, title, venue, year, doi, note in PUBLICATIONS:
        if year != current_year:
            current_year = year
            out.append('      <h3 class="pub-year" id="y%d">%d</h3>' % (year, year))
        if doi:
            link = ('<a class="pub-link" href="https://doi.org/%s" target="_blank" rel="noopener">'
                    'DOI %s</a>' % (doi, doi))
        else:
            link = ('<a class="pub-link pub-link--search" href="%s" target="_blank" rel="noopener">'
                    'Search for this paper</a>' % _scholar(title))
        badge = '<span class="pub-note">%s</span>' % note if note else ""
        out.append("""      <article class="pub reveal">
        <p class="pub-title">{title}{badge}</p>
        <p class="pub-meta">{authors} &middot; {venue}, {year}</p>
        {link}
      </article>""".format(title=title, badge=badge, authors=authors,
                           venue=venue, year=year, link=link))
    return "\n".join(out)


_with_doi = sum(1 for p in PUBLICATIONS if p[4])

PUBLICATIONS_BODY = """  <section class="section section--tight">
    <div class="wrap-narrow reveal">
      <p class="lead">Publications based on the pedagogical activities at WEL, and on the work of the
        students and staff who work here &mdash; from the e-Prayog remote laboratories of 2012 through
        to FPGA-based condition monitoring and electrochemical sensing.</p>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap-narrow">
      <div class="pub-list">
{entries}
      </div>

      <div class="note mt2 reveal" style="margin-top:2.4rem">
        <strong>About the links.</strong> {with_doi} of these {total} papers link straight to the
        publisher through their DOI. The remaining {without} &mdash; a workshop paper and two Forum
        for Information Retrieval Evaluation working notes &mdash; are not registered with a DOI, so
        they carry a title search instead of a link that might land on the wrong paper.
      </div>

      <div class="note reveal" style="margin-top:1.2rem">
        <strong>Published something at WEL?</strong> Send the reference to
        <a href="mailto:wel@ee.iitb.ac.in">wel@ee.iitb.ac.in</a> and it will be added here.
      </div>
    </div>
  </section>
""".format(entries=_entries(), with_doi=_with_doi, total=len(PUBLICATIONS),
           without=len(PUBLICATIONS) - _with_doi)


PAGES = [{
    "file": "publications.html", "nav": "about.html", "sub": "achievements.html",
    "title": "Publications from WEL | Wadhwani Electronics Laboratory",
    "desc": "Publications based on pedagogical activities at the Wadhwani Electronics Laboratory, "
            "IIT Bombay, and on the work of the students and staff who work here.",
    "hero": page_hero("Publications from WEL",
                      "Papers from the lab's teaching work and from the research of the students and "
                      "staff who work here.",
                      [("About", "about.html"), ("Achievements", "achievements.html"),
                       ("Publications", "publications.html")],
                      "assets/img/site/wel1-lab.jpeg"),
    "body": PUBLICATIONS_BODY,
}]
