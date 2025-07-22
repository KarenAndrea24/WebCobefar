from django.urls import path
from apps.sample.api.views.orden_venta_api_view import CrearOrdenVentaAPIView


urlpatterns = [
    path('orden-venta/', CrearOrdenVentaAPIView.as_view(), name='crear_orden_venta'),
]