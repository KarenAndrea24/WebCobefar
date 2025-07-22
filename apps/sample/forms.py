from django import forms

from apps.sample.models import LoteAsignado


class LoteAsignadoForm(forms.ModelForm):
    class Meta:
        model = LoteAsignado
        fields = ['lote', 'cantidad_asignada']
        widgets = {
            'cantidad_asignada': forms.NumberInput(attrs={'min': 0, 'step': 0.01, 'class': 'form-control'}),
        }
