from rest_framework import generics
from apps.sample.api.serializers.orden_venta_serializer import OrdenVentaSerializer
from apps.sample.models import OrdenVenta


class CrearOrdenVentaAPIView(generics.CreateAPIView):
    queryset = OrdenVenta.objects.all()
    serializer_class = OrdenVentaSerializer
