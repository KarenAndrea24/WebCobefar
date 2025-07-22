from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from apps.sample.forms import LoteAsignadoForm
from apps.sample.models import Lote, OrdenVenta
from web_project import TemplateLayout


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to sample/urls.py file for more pages.
"""


class SampleView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        mapping = {
            "ordenes_ventas/ordenes_ventas.html": ("Ordenes de ventas", "ordenes-ventas_json"),
        }
        titulo, url_name = mapping.get(self.template_name, (None, None))
        if titulo and url_name:
            from django.urls import reverse
            context["titulo"] = titulo
            context["url_json"] = reverse(url_name)

        return context


def ordenes_venta_json(request):
    ordenes = OrdenVenta.objects.all().values(
        'id',
        'numero_ov',
        'fecha_creacion',
        'hora_creacion',
        'ov_vinculado',
        'monto_total',
        'asesor_comercial',
        'destino',
        'canal_ventas',
        'cantidad_items',
        'pickear',
        'estado_asignacion_lotes',
        'estado_sap',
        'respuesta_integrador',
    )
    data = list(ordenes)
    return JsonResponse({'data': data})


def asignar_lotes(request, orden_id):
    orden = get_object_or_404(OrdenVenta, id=orden_id)
    detalles = orden.detalles.all()
    lotes_disponibles = Lote.objects.all()
    lotes_asignados = orden.lotes_asignados.all()

    if request.method == 'POST':
        pass

    context = {
        'orden': orden,
        'detalles': detalles,
        'lotes_disponibles': lotes_disponibles,
        'lotes_asignados': lotes_asignados,
        'form': LoteAsignadoForm() 
    }

    return render(request, 'ordenes_ventas/modals/modal_asignar_lotes.html', context)


def visualizar_orden_venta(request, orden_id):
    orden = get_object_or_404(OrdenVenta, id=orden_id)
    detalles = orden.detalles.all()
    # personas_autorizadas = orden.personas_autorizadas.all()

    if request.method == 'POST':
        pass

    context = {
        'orden': orden,
        'detalles': detalles,
        # 'personas_autorizadas': personas_autorizadas,
    }

    return render(request, 'ordenes_ventas/modals/modal_visualizar_ov.html', context)
