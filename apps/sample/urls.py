from django.urls import path
from .views import SampleView, ordenes_venta_json


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

    path('ordenes-ventas/data/', ordenes_venta_json, name='ordenes-ventas_json'),
]
