/* Wadhwani Electronics Laboratory - site behaviour
   Vanilla JS, no dependencies. */
(function () {
  'use strict';

  var on = function (el, ev, fn) { if (el) el.addEventListener(ev, fn); };
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------------- mobile navigation ---------------- */
  var nav = $('#nav');
  var toggle = $('#navToggle');
  var scrim = $('#navScrim');

  function closeNav() {
    if (!nav) return;
    nav.classList.remove('is-open');
    if (toggle) { toggle.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); }
    if (scrim) scrim.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  on(toggle, 'click', function () {
    var open = nav.classList.toggle('is-open');
    toggle.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (scrim) scrim.classList.toggle('is-open', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  on(scrim, 'click', closeNav);
  on(document, 'keydown', function (e) { if (e.key === 'Escape') closeNav(); });

  /* submenu toggles - only act as toggles on small screens */
  $$('.nav__item--has-children > .nav__link').forEach(function (link) {
    on(link, 'click', function (e) {
      if (window.matchMedia('(min-width:961px)').matches) return; // desktop: follow the link
      e.preventDefault();
      var item = link.parentElement;
      var wasOpen = item.classList.contains('is-open');
      $$('.nav__item--has-children').forEach(function (i) { i.classList.remove('is-open'); });
      item.classList.toggle('is-open', !wasOpen);
    });
  });

  window.addEventListener('resize', function () {
    if (window.matchMedia('(min-width:961px)').matches) closeNav();
  });

  /* ---------------- sticky header shadow + back to top ---------------- */
  var header = $('#siteHeader');
  var toTop = $('#toTop');
  function onScroll() {
    var y = window.pageYOffset || document.documentElement.scrollTop;
    if (header) header.classList.toggle('is-stuck', y > 8);
    if (toTop) toTop.classList.toggle('is-visible', y > 600);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  on(toTop, 'click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  /* ---------------- reveal on scroll ---------------- */
  var revealables = $$('.reveal');
  if (revealables.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -60px 0px', threshold: 0.08 });
      revealables.forEach(function (el) { io.observe(el); });
    } else {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    }
  }

  /* ---------------- animated counters ---------------- */
  var counters = $$('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        cio.unobserve(el);
        var target = parseFloat(el.getAttribute('data-count'));
        var suffix = el.getAttribute('data-suffix') || '';
        var start = null, dur = 1400;
        function step(ts) {
          if (start === null) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased).toLocaleString('en-IN') + suffix;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------------- accordions ---------------- */
  $$('.acc__head').forEach(function (head) {
    on(head, 'click', function () {
      var acc = head.parentElement;
      var open = acc.classList.toggle('is-open');
      head.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ---------------- horizontal sliders ---------------- */
  $$('.slider').forEach(function (slider) {
    var track = $('.slider__track', slider);
    var prev = $('.slider__btn--prev', slider);
    var next = $('.slider__btn--next', slider);
    if (!track) return;
    function amount() {
      var first = track.firstElementChild;
      return first ? first.getBoundingClientRect().width + 22 : 340;
    }
    on(prev, 'click', function () { track.scrollBy({ left: -amount(), behavior: 'smooth' }); });
    on(next, 'click', function () { track.scrollBy({ left: amount(), behavior: 'smooth' }); });
  });

  /* ---------------- filter chips (gallery, instruments, boards...) ---------------- */
  $$('[data-filter-group]').forEach(function (group) {
    var targetSel = group.getAttribute('data-filter-target');
    var items = $$(targetSel);
    $$('.filter', group).forEach(function (btn) {
      on(btn, 'click', function () {
        var val = btn.getAttribute('data-filter');
        $$('.filter', group).forEach(function (b) { b.classList.remove('is-active'); });
        btn.classList.add('is-active');
        items.forEach(function (item) {
          var cats = (item.getAttribute('data-cat') || '').toLowerCase();
          var show = val === 'all' || cats.indexOf(val.toLowerCase()) !== -1;
          item.classList.toggle('is-hidden', !show);
        });
      });
    });
  });

  /* ---------------- live text search over a list ---------------- */
  $$('[data-search-target]').forEach(function (input) {
    var items = $$(input.getAttribute('data-search-target'));
    var empty = $(input.getAttribute('data-search-empty') || '#noResults');
    on(input, 'input', function () {
      var q = input.value.trim().toLowerCase();
      var visible = 0;
      items.forEach(function (item) {
        var hit = q === '' || item.textContent.toLowerCase().indexOf(q) !== -1;
        item.style.display = hit ? '' : 'none';
        if (hit) visible++;
      });
      if (empty) empty.classList.toggle('is-shown', visible === 0);
    });
  });

  /* ---------------- lightbox ---------------- */
  var lb = $('#lightbox');
  if (lb) {
    var lbImg = $('#lightboxImg');
    var lbCap = $('#lightboxCap');
    var figures = [];
    var index = 0;

    function visibleFigures() {
      return $$('.gallery figure').filter(function (f) { return !f.classList.contains('is-hidden'); });
    }
    function show(i) {
      figures = visibleFigures();
      if (!figures.length) return;
      index = (i + figures.length) % figures.length;
      var fig = figures[index];
      var full = fig.getAttribute('data-full') || $('img', fig).src;
      lbImg.src = full;
      lbImg.alt = $('img', fig).alt || '';
      if (lbCap) lbCap.textContent = (fig.getAttribute('data-cat') || '') + '  ·  ' + (index + 1) + ' / ' + figures.length;
      lb.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    }
    function hide() { lb.classList.remove('is-open'); lbImg.removeAttribute('src'); document.body.style.overflow = ''; }

    $$('.gallery figure').forEach(function (fig) {
      on(fig, 'click', function () { show(visibleFigures().indexOf(fig)); });
    });
    on($('#lightboxClose'), 'click', hide);
    on($('#lightboxPrev'), 'click', function (e) { e.stopPropagation(); show(index - 1); });
    on($('#lightboxNext'), 'click', function (e) { e.stopPropagation(); show(index + 1); });
    on(lb, 'click', function (e) { if (e.target === lb) hide(); });
    on(document, 'keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') hide();
      if (e.key === 'ArrowLeft') show(index - 1);
      if (e.key === 'ArrowRight') show(index + 1);
    });
  }

  /* ---------------- home hero slideshow ---------------- */
  var show = $('#heroShow');
  if (show) {
    var slides = $$('img', show);
    var i = 0;
    if (slides.length > 1) {
      slides.forEach(function (s, n) { s.style.transition = 'opacity 1.2s ease'; s.style.opacity = n === 0 ? '1' : '0'; s.style.position = 'absolute'; s.style.inset = '0'; });
      setInterval(function () {
        slides[i].style.opacity = '0';
        i = (i + 1) % slides.length;
        slides[i].style.opacity = '1';
      }, 6000);
    }
  }

  /* ---------------- current year ---------------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
