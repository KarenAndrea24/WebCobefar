'use strict';
$(function () {
  $('#tabla-detalles-lotes').DataTable({
    paging     : true,
    searching  : true,
    info       : true,
    ordering   : true,
    displayLength: 5,
    lengthMenu: [5],
    lengthChange: true,
    scrollX    : true,
    autoWidth  : false,
    language   : datatableLang(),
  });
});

function datatableLang () {
  return {
    paginate: {
      next: '<i class="ti ti-chevron-right ti-sm"></i>',
      previous: '<i class="ti ti-chevron-left ti-sm"></i>'
    }
  };
}
