from rest_framework import serializers
from apps.sample.api.serializers.detalles_ov_serializer import DetalleOrdenVentaSerializer
from apps.sample.models import DetalleOrdenVenta, OrdenVenta


class OrdenVentaSerializer(serializers.ModelSerializer):
    detalles = DetalleOrdenVentaSerializer(many=True)

    class Meta:
        model = OrdenVenta
        fields = '__all__'

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles', [])
        # Crear la orden de venta primero, con los campos que sí le pertenecen
        orden_venta = OrdenVenta.objects.create(**validated_data)

        # Agregar los detalles
        for detalle_data in detalles_data:
            DetalleOrdenVenta.objects.create(orden_venta=orden_venta, **detalle_data)

        return orden_venta
    