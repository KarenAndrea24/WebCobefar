from django.db import models
from django.contrib.auth import get_user_model


Usuario = get_user_model()


ESTADO_ASIGNACION_LOTES_CHOICES = [
    ('pendiente', 'Pendiente'),
    ('terminado', 'Terminado'),
]


ESTADO_SAP_CHOICES = [
    ('pendiente', 'Pendiente'),
    ('integrado', 'Integrado'),
    ('error', 'Error'),
]


class CondicionPago(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class LugarDestino(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class DireccionEnvio(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class DireccionFacturacion(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoComprobante(models.Model):
    numero_comprobante = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoEmbalaje(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Almacen(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class ListaPrecios(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Vendedor(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoDocumento(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# class Cliente(models.Model):
#     razon_social = models.CharField(max_length=255, unique=True)
#     ruc = models.CharField(max_length=11, unique=True)

#     def __str__(self):
#         return f"{self.razon_social} ({self.ruc})"


class PersonaAutorizada(models.Model):
    # orden_venta = models.ForeignKey(OrdenVenta, on_delete=models.CASCADE, related_name='personas_autorizadas')
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    numero_documento = models.CharField(max_length=20)
    nombres_apellidos = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.numero_documento} - {self.nombres_apellidos}"
    
    class Meta:
        verbose_name = "Persona autorizada"
        verbose_name_plural = "Personas autorizadas"


# class AsesorComercial(models.Model):
#     # orden_venta = models.ForeignKey(OrdenVenta, on_delete=models.CASCADE, related_name='personas_autorizadas')
#     tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
#     numero_documento = models.CharField(max_length=20)
#     nombres_apellidos = models.CharField(max_length=255)
#     celular = models.CharField(max_length=15)

#     def __str__(self):
#         return f"{self.numero_documento} - {self.nombres_apellidos}"
    
#     class Meta:
#         verbose_name = "Persona autorizada"
#         verbose_name_plural = "Personas autorizadas"


class OrdenVenta(models.Model):
    numero_ov = models.CharField("Número OV", max_length=20, unique=True)
    fecha_creacion = models.DateField("Fecha creación")
    hora_creacion = models.TimeField("Hora creación")
    ov_vinculado = models.CharField("O.V. Vinculado", max_length=20, blank=True, null=True)
    # asesor_comercial = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Asesor Comercial")
    asesor_comercial = models.CharField(max_length=255)
    # cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    cliente = models.CharField(max_length=255)
    destino = models.CharField("Destino", max_length=100)
    canal_ventas = models.CharField("Canal Ventas", max_length=50)
    cantidad_items = models.IntegerField("Cant. Items")
    pickear = models.BooleanField("Pickear", default=True)
    condicion_pago = models.ForeignKey(CondicionPago, on_delete=models.PROTECT)
    lugar_destino = models.ForeignKey(LugarDestino, on_delete=models.PROTECT)
    direccion_envio = models.ForeignKey(DireccionEnvio, on_delete=models.PROTECT)
    direccion_facturacion = models.ForeignKey(DireccionFacturacion, on_delete=models.PROTECT)
    tipo_comprobante = models.ForeignKey(TipoComprobante, on_delete=models.PROTECT)
    tipo_embalaje = models.ForeignKey(TipoEmbalaje, on_delete=models.PROTECT)
    almacen = models.ForeignKey(Almacen, on_delete=models.PROTECT)
    lista_precios = models.ForeignKey(ListaPrecios, on_delete=models.PROTECT)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    subtotal = models.DecimalField("SubTotal", max_digits=12, decimal_places=2, default=0)
    descuento_total = models.DecimalField("Descuento total (%)", max_digits=5, decimal_places=2, default=0)
    impuesto = models.DecimalField("Impuesto", max_digits=12, decimal_places=2, default=0)
    monto_total = models.DecimalField("Monto total", max_digits=12, decimal_places=2, default=0)
    zona = models.CharField("Zona", max_length=100, blank=True, null=True)
    persona_autorizada = models.ForeignKey(PersonaAutorizada, on_delete=models.PROTECT)
    linea_credito_disponible = models.DecimalField("Línea de crédito disponible", max_digits=12, decimal_places=2, blank=True, null=True)
    estado_asignacion_lotes = models.CharField("Estado asignación de lotes", max_length=50, choices=ESTADO_ASIGNACION_LOTES_CHOICES, default='pendiente')
    estado_sap = models.CharField("Estado SAP", max_length=50, choices=ESTADO_SAP_CHOICES, default='pendiente')
    respuesta_integrador = models.TextField("Respuesta de integrador", blank=True, null=True)

    def __str__(self):
        return self.numero_ov

    class Meta:
        verbose_name = "Orden de venta"
        verbose_name_plural = "Órdenes de venta"
        # ordering = ['-fecha_creacion', '-hora_creacion']


class DetalleOrdenVenta(models.Model):
    orden_venta = models.ForeignKey(OrdenVenta, on_delete=models.CASCADE, related_name='detalles')
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    stock_disponible = models.IntegerField()
    lista_precio = models.ForeignKey(ListaPrecios, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    umd = models.CharField("Unidad de medida", max_length=20)
    # cantidad_t = models.DecimalField("Cantidad total", max_digits=10, decimal_places=2)
    precio_igv_ad = models.DecimalField("Precio IGV A.D.", max_digits=10, decimal_places=2)
    porcentaje_descuento = models.DecimalField("Porcentaje descuento", max_digits=5, decimal_places=2)
    precio_igv_dd = models.DecimalField("Precio IGV D.D.", max_digits=10, decimal_places=2)
    afecto_impuesto = models.BooleanField("Afecto a impuesto", default=False)
    solo_impuesto = models.BooleanField("Solo impuesto", default=False)
    total = models.DecimalField("Total", max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    
    class Meta:
        verbose_name = "Detalle órden de venta"
        verbose_name_plural = "Detalles órdenes de venta"


class Lote(models.Model):
    nro_lote = models.CharField(max_length=50, unique=True)
    ubicacion = models.CharField(max_length=255)
    cantidad_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    fecha_admision = models.DateField()

    def __str__(self):
        return self.nro_lote

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"
        # ordering = ['-fecha_admision', '-fecha_vencimiento']


class LoteAsignado(models.Model):
    orden_venta = models.ForeignKey(OrdenVenta, on_delete=models.CASCADE, related_name='lotes_asignados')
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    cantidad_asignada = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.orden_venta.numero_ov} - {self.lote.nro_lote}"

    class Meta:
        verbose_name = "Lote asignado"
        verbose_name_plural = "Lotes asignados"
        # unique_together = ('orden_venta', 'lote')
