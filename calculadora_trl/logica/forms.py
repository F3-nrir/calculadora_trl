from django import forms
from .models import Modelo

class ModeloForm(forms.Form):
    modelo = forms.ModelChoiceField(queryset=Modelo.objects.all(), widget=forms.RadioSelect())
