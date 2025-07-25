
from apps.sample.api.serializers.base_auxiliar_serializer import BaseAuxiliarSerializer
from apps.sample.models import Almacen, CondicionPago, CuentaContable, DireccionEnvio, DireccionFacturacion, ListaPrecios, LugarDestino, Moneda, Serie, TipoComprobante, TipoDocumento, TipoEmbalaje, Vendedor


class CondicionPagoSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = CondicionPago


class MonedaSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = Moneda


class LugarDestinoSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = LugarDestino


class DireccionEnvioSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = DireccionEnvio


class DireccionFacturacionSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = DireccionFacturacion


class TipoComprobanteSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = TipoComprobante


class TipoEmbalajeSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = TipoEmbalaje


class AlmacenSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = Almacen


class ListaPreciosSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = ListaPrecios


class VendedorSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = Vendedor


class TipoDocumentoSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = TipoDocumento


class SerieSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = Serie


class CuentaContableSerializer(BaseAuxiliarSerializer):
    class Meta(BaseAuxiliarSerializer.Meta):
        model = CuentaContable
