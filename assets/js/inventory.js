/* WEL Inventory - component browser for the static site.
 *
 * Reads assets/data/inventory.json (produced by _src/inventory_import.py from
 * the same spreadsheet the Flask app imports) and lets anyone search the stock,
 * filter it, and build a request list.
 *
 * The request list lives in localStorage and is handed over as text - by email
 * or clipboard - because a static site has no server to accept it. Approving a
 * request and decrementing stock is the Flask app's job, in inventory-app/.
 */
(function () {
  'use strict';

  var root = document.getElementById('inv');
  if (!root) return;

  var LAB_EMAIL = root.getAttribute('data-email') || 'wel@ee.iitb.ac.in';
  var STORE = 'wel-inventory-request';

  var els = {
    status: document.getElementById('invStatus'),
    search: document.getElementById('invSearch'),
    type: document.getElementById('invType'),
    stock: document.getElementById('invStock'),
    count: document.getElementById('invCount'),
    body: document.getElementById('invBody'),
    empty: document.getElementById('invEmpty'),
    table: document.getElementById('invTable'),
    cart: document.getElementById('invCart'),
    cartList: document.getElementById('invCartList'),
    cartCount: document.getElementById('invCartCount'),
    team: document.getElementById('invTeam'),
    members: document.getElementById('invMembers'),
    note: document.getElementById('invNote'),
    mailBtn: document.getElementById('invMail'),
    copyBtn: document.getElementById('invCopy'),
    clearBtn: document.getElementById('invClear'),
    copied: document.getElementById('invCopied'),
    sample: document.getElementById('invSample'),
    updated: document.getElementById('invUpdated')
  };

  var all = [];
  var picked = load();

  /* ---------------- storage ---------------- */
  function load() {
    try { return JSON.parse(localStorage.getItem(STORE)) || {}; }
    catch (e) { return {}; }
  }
  function save() {
    try { localStorage.setItem(STORE, JSON.stringify(picked)); } catch (e) {}
  }

  /* ---------------- helpers ---------------- */
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
  function stockClass(q) { return q <= 0 ? 'out' : (q <= 2 ? 'low' : 'ok'); }
  function stockLabel(q) { return q <= 0 ? 'Out of stock' : (q <= 2 ? 'Low: ' + q : String(q)); }

  /* ---------------- load data ---------------- */
  fetch('assets/data/inventory.json', { cache: 'no-cache' })
    .then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(function (data) {
      all = (data && data.components) || [];
      if (els.sample && data && data.sample) els.sample.hidden = false;
      if (els.updated && data && data.updated) {
        els.updated.textContent = data.updated;
        els.updated.parentNode.hidden = false;
      }
      if (!all.length) { fail('The component list is empty.'); return; }
      buildTypes();
      if (els.status) els.status.hidden = true;
      if (els.table) els.table.hidden = false;
      render();
      renderCart();
    })
    .catch(function () {
      fail('The component list could not be loaded.');
    });

  function fail(msg) {
    if (!els.status) return;
    els.status.className = 'note note--red';
    els.status.innerHTML = '<strong>' + esc(msg) + '</strong> Ask the lab for the current stock at ' +
      '<a href="mailto:' + esc(LAB_EMAIL) + '">' + esc(LAB_EMAIL) + '</a>.';
  }

  function buildTypes() {
    if (!els.type) return;
    var types = [];
    all.forEach(function (c) { if (c.type && types.indexOf(c.type) === -1) types.push(c.type); });
    types.sort();
    types.forEach(function (t) {
      var o = document.createElement('option');
      o.value = t; o.textContent = t;
      els.type.appendChild(o);
    });
  }

  /* ---------------- filtering ---------------- */
  function visible() {
    var q = (els.search ? els.search.value : '').trim().toLowerCase();
    var type = els.type ? els.type.value : '';
    var stock = els.stock ? els.stock.value : '';
    return all.filter(function (c) {
      if (type && c.type !== type) return false;
      if (stock === 'in' && c.qty <= 0) return false;
      if (stock === 'low' && !(c.qty > 0 && c.qty <= 2)) return false;
      if (!q) return true;
      return (c.model + ' ' + c.description + ' ' + c.type + ' ' + c.location)
        .toLowerCase().indexOf(q) !== -1;
    });
  }

  function render() {
    var rows = visible();
    if (els.count) {
      els.count.textContent = rows.length === all.length
        ? all.length + ' components'
        : rows.length + ' of ' + all.length + ' components';
    }
    if (els.empty) els.empty.hidden = rows.length > 0;

    var html = rows.map(function (c) {
      var id = String(c.sr);
      var inList = picked[id];
      return '<tr>' +
        '<td data-label="Component"><strong>' + esc(c.model || '—') + '</strong>' +
          (c.description ? '<span class="inv-desc">' + esc(c.description) + '</span>' : '') +
          (c.link ? '<a class="inv-link" href="' + esc(c.link) + '" target="_blank" rel="noopener">Datasheet</a>' : '') +
        '</td>' +
        '<td data-label="Type">' + esc(c.type || '—') + '</td>' +
        '<td data-label="Location">' + esc(c.location || '—') + '</td>' +
        '<td data-label="In stock"><span class="inv-stock inv-stock--' + stockClass(c.qty) + '">' +
          esc(stockLabel(c.qty)) + '</span></td>' +
        '<td data-label="Request">' +
          (c.qty <= 0
            ? '<span class="inv-none">—</span>'
            : '<div class="inv-add">' +
                '<input type="number" min="1" max="' + c.qty + '" value="' + (inList || 1) + '" ' +
                  'aria-label="Quantity of ' + esc(c.model) + '" data-qty="' + esc(id) + '">' +
                '<button type="button" class="btn btn--sm ' + (inList ? 'btn--outline' : 'btn--primary') + '" ' +
                  'data-add="' + esc(id) + '">' + (inList ? 'Update' : 'Add') + '</button>' +
              '</div>') +
        '</td></tr>';
    }).join('');

    if (els.body) els.body.innerHTML = html;
  }

  /* ---------------- request list ---------------- */
  function renderCart() {
    var ids = Object.keys(picked);
    if (els.cartCount) els.cartCount.textContent = ids.length;
    if (els.cart) els.cart.hidden = ids.length === 0;
    if (!ids.length) { if (els.cartList) els.cartList.innerHTML = ''; return; }

    if (els.cartList) {
      els.cartList.innerHTML = ids.map(function (id) {
        var c = byId(id);
        if (!c) return '';
        return '<li><span>' + esc(c.model || c.description) + '</span>' +
          '<b>&times;' + picked[id] + '</b>' +
          '<button type="button" class="inv-remove" data-remove="' + esc(id) + '" ' +
          'aria-label="Remove ' + esc(c.model) + '">&times;</button></li>';
      }).join('');
    }
  }

  function byId(id) {
    for (var i = 0; i < all.length; i++) {
      if (String(all[i].sr) === String(id)) return all[i];
    }
    return null;
  }

  function requestText() {
    var lines = ['WEL Inventory - component request', ''];
    lines.push('Team: ' + ((els.team && els.team.value.trim()) || '(not given)'));
    lines.push('Members: ' + ((els.members && els.members.value.trim()) || '(not given)'));
    lines.push('');
    lines.push('Components requested:');
    Object.keys(picked).forEach(function (id) {
      var c = byId(id);
      if (!c) return;
      lines.push('  - ' + (c.model || c.description) + '  x' + picked[id] +
                 (c.location ? '   [' + c.location + ']' : ''));
    });
    var note = els.note && els.note.value.trim();
    if (note) { lines.push(''); lines.push('Notes: ' + note); }
    lines.push('');
    lines.push('Sent from the WEL Inventory page.');
    return lines.join('\n');
  }

  /* ---------------- events ---------------- */
  ['input', 'change'].forEach(function (ev) {
    if (els.search) els.search.addEventListener(ev, render);
    if (els.type) els.type.addEventListener(ev, render);
    if (els.stock) els.stock.addEventListener(ev, render);
  });

  if (els.body) {
    els.body.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-add]');
      if (!btn) return;
      var id = btn.getAttribute('data-add');
      var input = els.body.querySelector('[data-qty="' + id + '"]');
      var c = byId(id);
      var n = Math.max(1, Math.min(parseInt(input && input.value, 10) || 1, c ? c.qty : 1));
      picked[id] = n;
      save();
      render();
      renderCart();
    });
  }

  if (els.cartList) {
    els.cartList.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-remove]');
      if (!btn) return;
      delete picked[btn.getAttribute('data-remove')];
      save();
      render();
      renderCart();
    });
  }

  if (els.clearBtn) {
    els.clearBtn.addEventListener('click', function () {
      picked = {};
      save();
      render();
      renderCart();
    });
  }

  if (els.mailBtn) {
    els.mailBtn.addEventListener('click', function () {
      var subject = 'WEL Inventory request' +
        (els.team && els.team.value.trim() ? ' - ' + els.team.value.trim() : '');
      var href = 'mailto:' + LAB_EMAIL +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(requestText());
      // Very long mailto links get truncated by some mail clients; fall back to
      // the clipboard so the request is never silently cut short.
      if (href.length > 1900) {
        copy(requestText(), 'Too long for an email link - request copied instead. Paste it into a mail to ' + LAB_EMAIL + '.');
        return;
      }
      window.location.href = href;
    });
  }

  if (els.copyBtn) {
    els.copyBtn.addEventListener('click', function () { copy(requestText(), 'Request copied.'); });
  }

  function copy(text, msg) {
    var done = function () {
      if (!els.copied) return;
      els.copied.textContent = msg;
      els.copied.hidden = false;
      setTimeout(function () { els.copied.hidden = true; }, 6000);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { fallbackCopy(text, done); });
    } else {
      fallbackCopy(text, done);
    }
  }

  function fallbackCopy(text, done) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;left:-9999px';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); done(); } catch (e) {}
    document.body.removeChild(ta);
  }
})();
