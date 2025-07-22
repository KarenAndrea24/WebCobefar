from rest_framework import serializers
from apps.sample.models import DetalleOrdenVenta


class DetalleOrdenVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrdenVenta
        exclude = ['orden_venta']
