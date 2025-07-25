from apps.sample.api.serializers.auxiliares import AlmacenSerializer, CondicionPagoSerializer, CuentaContableSerializer, DireccionEnvioSerializer, DireccionFacturacionSerializer, ListaPreciosSerializer, LugarDestinoSerializer, MonedaSerializer, SerieSerializer, TipoComprobanteSerializer, TipoDocumentoSerializer, TipoEmbalajeSerializer, VendedorSerializer
from apps.sample.models import Almacen, CondicionPago, CuentaContable, DireccionEnvio, DireccionFacturacion, ListaPrecios, LugarDestino, Moneda, Serie, TipoComprobante, TipoDocumento, TipoEmbalaje, Vendedor
from rest_framework import generics

def build_view(model, serializer):
    class _View(generics.ListCreateAPIView):
        queryset = model.objects.all()
        serializer_class = serializer
    _View.__name__ = f"{model.__name__}ListCreateAPIView"
    return _View


CondicionPagoAPIView   = build_view(CondicionPago,   CondicionPagoSerializer)
MonedaAPIView          = build_view(Moneda,          MonedaSerializer)
LugarDestinoAPIView    = build_view(LugarDestino,    LugarDestinoSerializer)
DireccionEnvioAPIView  = build_view(DireccionEnvio,  DireccionEnvioSerializer)
DireccionFactAPIView   = build_view(DireccionFacturacion, DireccionFacturacionSerializer)
TipoComprobanteAPIView = build_view(TipoComprobante, TipoComprobanteSerializer)
TipoEmbalajeAPIView    = build_view(TipoEmbalaje,    TipoEmbalajeSerializer)
AlmacenAPIView         = build_view(Almacen,         AlmacenSerializer)
ListaPreciosAPIView    = build_view(ListaPrecios,    ListaPreciosSerializer)
VendedorAPIView        = build_view(Vendedor,        VendedorSerializer)
TipoDocumentoAPIView   = build_view(TipoDocumento,   TipoDocumentoSerializer)
SerieAPIView           = build_view(Serie,           SerieSerializer)
CuentaContableAPIView  = build_view(CuentaContable,  CuentaContableSerializer)
