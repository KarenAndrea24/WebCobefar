from rest_framework import serializers


class BaseAuxiliarSerializer(serializers.ModelSerializer):
    """Serializador simple para tablas maestras de catálogo."""

    class Meta:
        fields = '__all__'
        read_only_fields = ['id']
