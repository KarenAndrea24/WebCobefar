from django.urls import path
from .views import SampleView, asignar_lotes, ordenes_venta_json, visualizar_orden_venta


urlpatterns = [
    path(
        "",
        SampleView.as_view(template_name="index.html"),
        name="index",
    ),
    path(
        "ordenes-ventas/",
        SampleView.as_view(template_name="ordenes_ventas/ordenes_ventas.html"),
        name="ordenes-ventas",
    ),
    path(
        "ordenes-ventas-seleccionadas/",
        SampleView.as_view(template_name="ordenes_ventas_seleccionadas/ordenes_ventas_seleccionadas.html"),
        name="ordenes-ventas-seleccionadas",
    ),

    # Mostrar tabla ordenes de ventas
    path('ordenes-ventas/data/', ordenes_venta_json, name='ordenes-ventas_json'),

    # Modals asignar lotes
    path('orden-venta/<int:orden_id>/asignar-lotes/', asignar_lotes, name='asignar-lotes'),

    # Modals visualizar ordenes de ventas
    path('orden-venta/<int:orden_id>/visualizar-ov/', visualizar_orden_venta, name='visualizar-orden-venta'),

]
