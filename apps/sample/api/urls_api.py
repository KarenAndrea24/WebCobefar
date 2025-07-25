from django.urls import path
from apps.sample.api.views.auxiliares import AlmacenAPIView, CondicionPagoAPIView, CuentaContableAPIView, DireccionEnvioAPIView, DireccionFactAPIView, ListaPreciosAPIView, LugarDestinoAPIView, MonedaAPIView, SerieAPIView, TipoComprobanteAPIView, TipoDocumentoAPIView, TipoEmbalajeAPIView, VendedorAPIView
from apps.sample.api.views.orden_venta_api_view import CrearOrdenVentaAPIView


urlpatterns = [
    path('orden-venta/', CrearOrdenVentaAPIView.as_view(), name='api_crear_orden_venta'),

    # auxiliares
    path('condiciones-pago/',  CondicionPagoAPIView.as_view(),   name='api_condiciones_pago'),
    path('monedas/',           MonedaAPIView.as_view(),          name='api_monedas'),
    path('lugares-destino/',   LugarDestinoAPIView.as_view(),    name='api_lugares_destino'),
    path('direcciones-envio/', DireccionEnvioAPIView.as_view(),  name='api_direcciones_envio'),
    path('direcciones-facturacion/',  DireccionFactAPIView.as_view(),   name='api_direcciones_facturacion'),
    path('tipos-comprobantes/', TipoComprobanteAPIView.as_view(), name='api_tipos_comprobantes'),
    path('tipos-embalajes/',    TipoEmbalajeAPIView.as_view(),    name='api_tipos_embalajes'),
    path('almacenes/',         AlmacenAPIView.as_view(),         name='api_almacenes'),
    path('listas-precios/',    ListaPreciosAPIView.as_view(),    name='api_listas_precios'),
    path('vendedores/',        VendedorAPIView.as_view(),        name='api_vendedores'),
    path('tipos-documentos/',   TipoDocumentoAPIView.as_view(),   name='api_tipos_documentos'),
    path('series/',            SerieAPIView.as_view(),           name='api_series'),
    path('cuentas-contables/', CuentaContableAPIView.as_view(),  name='api_cuentas_contables'),
]
