/* Fills the shared edit dialog from whichever row's pencil was clicked.
 *
 * The listener is on the table container rather than on each button, so it
 * keeps working after live.js replaces the rows with fresh markup.
 */
(function () {
  'use strict';

  var container = document.getElementById('liveInventory');
  var form      = document.getElementById('editForm');
  if (!container || !form) return;

  var FIELDS = ['sr_no', 'component_type', 'model_no',
                'description', 'link', 'location', 'quantity'];

  container.addEventListener('click', function (ev) {
    var btn = ev.target.closest('.js-edit');
    if (!btn) return;

    form.action = '/admin/component/' + btn.dataset.id + '/edit';
    FIELDS.forEach(function (f) {
      var input = form.querySelector('[name="' + f + '"]');
      if (input) input.value = btn.dataset[f] || '';
    });
    bootstrap.Modal.getOrCreateInstance(document.getElementById('editModal')).show();
  });

  /* Offer the types already in use as autocomplete on both dialogs. */
  function refreshTypeList() {
    var list = document.getElementById('typeList');
    if (!list) {
      list = document.createElement('datalist');
      list.id = 'typeList';
      document.body.appendChild(list);
    }
    var seen = {};
    [].forEach.call(container.querySelectorAll('.js-edit'), function (b) {
      var t = b.dataset.component_type;
      if (t) seen[t] = 1;
    });
    list.innerHTML = Object.keys(seen).sort().map(function (t) {
      return '<option value="' + t.replace(/"/g, '&quot;') + '">';
    }).join('');
  }

  refreshTypeList();
  container.addEventListener('live:updated', refreshTypeList);
})();
