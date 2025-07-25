// static/js/datatable-docs.js
// -----------------------------------------------------------------------------
//  DataTables – documentos de venta (Facturas, Boletas, NC, ND)
//  Versión DRY que centraliza la lógica de tablas, filtros externos, exportación
// -----------------------------------------------------------------------------

'use strict';
/* global $, $.fn */

/**
 * Inicializa una tabla DataTables para el módulo de documentos de venta.
 * @param {Object} opts
 * @param {string} opts.urlDatos        – Endpoint JSON (Django) que devuelve {data: […]}
 * @param {string} opts.tablaSelector   – Selector CSS de la <table>
 * @param {string} opts.filtrosSelector – Selector CSS del <form> de filtros externos
 * @returns {DataTable|null}
 */
function initDocumentoTable ({ urlDatos, tablaSelector, filtrosSelector }) {
  const $tabla = $(tablaSelector);
  if (!$tabla.length) return null;

  const columnas = [
    { data: null }, // control (responsive)
    { data: null }, // checkbox
    { data: 'numero_ov' },
    { data: 'fecha_creacion' },
    { data: 'hora_creacion' },
    { data: 'ov_vinculado' },
    { data: 'monto_total' },
    { data: 'asesor_comercial' },
    { data: 'destino' },
    { data: 'canal_ventas' },
    { data: 'cantidad_items' },
    { data: 'pickear' },
    { data: 'estado_asignacion_lotes' },
    { data: 'estado_sap' },
    { data: 'respuesta_integrador' },
    { data: null }
  ];

  const dt = $tabla.DataTable({
    ajax: urlDatos,
    columns: columnas,
    columnDefs: getColumnDefs(),
    order: [[2, 'desc']],
    dom: datatableDom(),
    displayLength: 5,
    lengthMenu: [5, 10, 25, 50],
    language: datatableLang(),
    buttons: exportButtons(),
    responsive: responsiveCfg(),
    scrollX: true,
    autoWidth: false,
    initComplete: () => $('.card-header').after('<hr class="my-0">')
  });


/* --- Asignar lotes ---------------------------------------------------------- */
$tabla.on('click', '.btn-lot', function () {
  const id = $(this).data('id');
  $.get(`/orden-venta/${id}/asignar-lotes/`, function(html) {
    $('#asignarLotes .modal-body').html(html);
    $('#asignarLotes').modal('show');
  });
});


/* --- Visualizar ---------------------------------------------------------- */
$tabla.on('click', '.btn-view', function () {
  const id = $(this).data('id');
  $.get(`/orden-venta/${id}/visualizar-ov`, html => {
    $('#visualizarOV .modal-body').html(html);
    $('#visualizarOV').modal('show');
  });
});

/* --- Borrar -------------------------------------------------------------- */
$tabla.on('click', '.btn-delete', function () {
  const id = $(this).data('id');
  if (!confirm('¿Seguro que deseas borrar este documento?')) return;
  $.ajax({
    url: `/documentos/${id}/`,
    type: 'DELETE',
    headers: { 'X-CSRFToken': csrfToken },   // toma tu token de un meta o cookie
    success: () => dt.row($(this).parents('tr')).remove().draw(false),
    error  : () => alert('No se pudo borrar')
  });
});

  // ------------------------------
  // Filtros externos (keyup/change)
  // ------------------------------
  const $f = $(filtrosSelector);
  $f.on('keyup change', '#filtro-numero-ov', function () { dt.column(2).search(this.value).draw(); });
  $f.on('keyup change', '#filtro-fecha-creacion', function () { dt.column(3).search(this.value).draw(); });
  $f.on('keyup change', '#filtro-ov-vinculado', function () { dt.column(5).search(this.value).draw(); });
  $f.on('keyup change', '#filtro-asesor-comercial', function () { dt.column(7).search(this.value).draw(); });
  $('#limpiar-filtros').on('click', () => {
    $f[0].reset(); // vacía inputs
    dt.columns().search('').draw();
  });

  // Borrar registro (demo-only UI)
  $tabla.on('click', '.delete-record', function () {
    dt.row($(this).parents('tr')).remove().draw();
  });

  setTimeout(() => {
    // Insertar botón "Cancelado"
    $('.cancelar-btn-wrapper').prepend(`
      <button id="btn-cancelar" class="btn btn-label-danger waves-effect">
        <i class="ti ti-ban"></i>Cancelar
      </button>
    `);

    // Ajustes de tamaños (quitar "sm")
    $('.dataTables_filter .form-control').removeClass('form-control-sm');
    $('.dataTables_length .form-select').removeClass('form-select-sm');
  }, 300);

  return dt;
}

// -----------------------------------------------------------------------------
// Funciones auxiliares separadas para mantener legibilidad
// -----------------------------------------------------------------------------
function getColumnDefs () {
  return [
    {
      targets: 0,
      className: 'control',
      orderable: false,
      searchable: false,
      responsivePriority: 2,
      render: () => ''
    },
    {
      targets: 1,
      orderable: false,
      searchable: false,
      responsivePriority: 3,
      checkboxes: true,
      render: () => '<input type="checkbox" class="dt-checkboxes form-check-input">',
      checkboxes: { selectAllRender: '<input type="checkbox" class="form-check-input">' }
    },
    {
      targets: 4,
      responsivePriority: 1
    },
    {
      // Badge demo (puedes personalizar según tu status real)
      targets: -2,
      render: (data, type, full) => {
        const status = {
          1: { t: 'Current', c: 'bg-label-primary' },
          2: { t: 'Professional', c: 'bg-label-success' },
          3: { t: 'Rejected', c: 'bg-label-danger' },
          4: { t: 'Resigned', c: 'bg-label-warning' },
          5: { t: 'Applied', c: 'bg-label-info' }
        }[full.status];
        return status ? `<span class="badge ${status.c}">${status.t}</span>` : data;
      }
    },
    {
      // Acciones – placeholder (puedes enlazar a vistas/URLs reales)
      targets: -1,
      title: 'Acciones',
      orderable: false,
      searchable: false,
      responsivePriority: 1,
      render: (data, type, full) =>
        `
        <div class="btn-group" role="group">
          <button class="btn btn-sm btn-primary btn-icon btn-lot  me-2" data-id="${full.id}" title="Asignar lotes">
            <i class="ti ti-arrows-right-left"></i>
          </button>
          <button class="btn btn-sm btn-secondary btn-icon btn-view  me-2" data-id="${full.id}" title="Visualizar">
            <i class="ti ti-eye"></i>
          </button>
          <button class="btn btn-sm btn-danger  btn-icon btn-delete" data-id="${full.id}" title="Borrar">
            <i class="ti ti-trash"></i>
          </button>
        </div>
        `
    }
  ];
}

// function datatableDom () {
//   return '<"card-header flex-column flex-md-row"<"head-label text-center"><"dt-action-buttons text-end pt-6 pt-md-0"B>><"row"<"col-sm-12 col-md-6"l><"col-sm-12 col-md-6 d-flex justify-content-center justify-content-md-end mt-n6 mt-md-0"f>>t<"row"<"col-sm-12 col-md-6"i><"col-sm-12 col-md-6"p>>';
// }

function datatableDom () {
  return `
    <"card-header flex-column flex-md-row justify-content-between align-items-center"
      <"head-label text-center mb-2 mb-md-0">
    >
    <"row"
      <"col-sm-12 col-md-6"l>
      <"col-sm-12 col-md-6 d-flex justify-content-center justify-content-md-end align-items-center gap-2"
        f
        <"cancelar-btn-wrapper">
        B
      >
    >
    t
    <"row"
      <"col-sm-12 col-md-6"i>
      <"col-sm-12 col-md-6"p>
    >
  `;
}

function datatableLang () {
  return {
    paginate: {
      next: '<i class="ti ti-chevron-right ti-sm"></i>',
      previous: '<i class="ti ti-chevron-left ti-sm"></i>'
    }
  };
}

function exportButtons () {
  const commonExport = {
    columns: [3, 4, 5, 6, 7],
    format: { body: stripHtmlForExport }
  };

  return [
    {
      extend: 'collection',
      className: 'btn btn-label-primary dropdown-toggle me-4 waves-effect waves-light border-none',
      text: '<i class="ti ti-file-export ti-xs me-sm-1"></i> <span class="d-none d-sm-inline-block">Export</span>',
      buttons: [
        { extend: 'print',  text: '<i class="ti ti-printer me-1"></i>Print',  className: 'dropdown-item', exportOptions: commonExport },
        { extend: 'csv',    text: '<i class="ti ti-file-text me-1"></i>Csv',   className: 'dropdown-item', exportOptions: commonExport },
        { extend: 'excel',  text: '<i class="ti ti-file-spreadsheet me-1"></i>Excel', className: 'dropdown-item', exportOptions: commonExport },
        { extend: 'pdf',    text: '<i class="ti ti-file-description me-1"></i>Pdf',  className: 'dropdown-item', exportOptions: commonExport },
        { extend: 'copy',   text: '<i class="ti ti-copy me-1"></i>Copy',  className: 'dropdown-item', exportOptions: commonExport }
      ]
    }
  ];
}

function stripHtmlForExport (inner) {
  if (!inner) return inner;
  const el = $.parseHTML(inner);
  return el.map(e => e.innerText ?? e.textContent).join('');
}

function responsiveCfg () {
  return {
    details: {
      display: $.fn.dataTable.Responsive.display.modal({
        header: row => `Details of ${row.data().razon_social || row.data().id}`
      }),
      type: 'column',
      renderer: (api, rowIdx, columns) => {
        const data = columns.map(col => col.title ? `<tr data-dt-row="${col.rowIndex}" data-dt-column="${col.columnIndex}"><td>${col.title}:</td><td>${col.data}</td></tr>` : '').join('');
        return data ? $('<table class="table"/>').append('<tbody/>').find('tbody').append(data).end() : false;
      }
    }
  };
}
