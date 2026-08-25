/* Live updates for WEL Inventory.
 *
 * Any element carrying data-live-url refreshes itself when the server says
 * something changed. The poll asks /api/version, which is two cheap queries
 * and about forty bytes; only when the revision number actually moves does it
 * fetch the fragment and swap it in.
 *
 * The markup that comes back is rendered by the same Jinja partial the full
 * page uses, so there is only ever one copy of it.
 */
(function () {
  'use strict';

  var panels = [].slice.call(document.querySelectorAll('[data-live-url]'));
  if (!panels.length) return;

  var IDLE = 5000;         // normal poll
  var SLOW = 30000;        // once the tab has been in the background a while
  var lastRev = null;
  var timer = null;

  /* Never yank the DOM out from under someone who is typing in it, or while a
   * dialog is open on top of it - they would lose what they had entered. */
  function busy(panel) {
    if (document.querySelector('.modal.show')) return true;
    var a = document.activeElement;
    if (!a || a === document.body) return false;
    return panel.contains(a) &&
           /^(INPUT|SELECT|TEXTAREA|BUTTON)$/.test(a.tagName);
  }

  function refresh(panel) {
    if (busy(panel)) return Promise.resolve();
    return fetch(panel.dataset.liveUrl, { headers: { 'X-Live': '1' } })
      .then(function (r) {
        /* A stale session redirects to the login page. Following that and
         * pasting it into the table would replace the inventory with a login
         * form, so treat any redirect as "not logged in any more" and stop. */
        if (!r.ok || r.redirected) { stop(); return null; }
        return r.text();
      })
      .then(function (html) {
        if (html === null || busy(panel)) return;
        panel.innerHTML = html;
        panel.dispatchEvent(new CustomEvent('live:updated', { bubbles: true }));
        flash(panel);
      })
      .catch(function () { /* offline or logged out - try again next tick */ });
  }

  function flash(panel) {
    panel.style.transition = 'none';
    panel.style.opacity = '.45';
    requestAnimationFrame(function () {
      panel.style.transition = 'opacity .35s ease';
      panel.style.opacity = '1';
    });
  }

  function badge(pending) {
    var link = document.querySelector('a[href*="/admin/requests"]');
    if (!link) return;
    var b = link.querySelector('.js-pending-badge');
    if (!pending) { if (b) b.remove(); return; }
    if (!b) {
      b = document.createElement('span');
      b.className = 'badge bg-danger rounded-pill ms-1 js-pending-badge';
      link.appendChild(b);
    }
    b.textContent = pending;
  }

  /* Once the session is gone there is nothing useful left to poll for, and
   * the next thing the user does will send them to the login page anyway. */
  var stopped = false;
  function stop() { stopped = true; clearTimeout(timer); }

  function tick() {
    if (stopped) return;
    fetch('/api/version', { headers: { 'X-Live': '1' } })
      .then(function (r) {
        if (r.redirected || r.status === 401 || r.status === 403) { stop(); return null; }
        return r.ok ? r.json() : null;
      })
      .then(function (d) {
        if (!d) return;
        badge(d.pending);
        if (lastRev === null) { lastRev = d.rev; return; }
        if (d.rev !== lastRev) {
          lastRev = d.rev;
          panels.forEach(refresh);
        }
      })
      .catch(function () {})
      .then(schedule);
  }

  function schedule() {
    if (stopped) return;
    clearTimeout(timer);
    timer = setTimeout(tick, document.hidden ? SLOW : IDLE);
  }

  /* Coming back to the tab should show current data straight away. */
  document.addEventListener('visibilitychange', function () {
    if (!document.hidden && !stopped) { clearTimeout(timer); tick(); }
  });

  tick();
})();
