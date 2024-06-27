from django import forms
from .models import TipoServicio, Servicio

class TipoServicioForm(forms.ModelForm):
    class Meta:
        model = TipoServicio
        fields = ['nombre']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['valor', 'descripcion', 'hotel', 'tipo_servicio']