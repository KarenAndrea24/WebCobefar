from django.http import JsonResponse
from django.views.generic import TemplateView
from apps.sample.models import OrdenVenta
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
        'asesor_comercial__username',
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
