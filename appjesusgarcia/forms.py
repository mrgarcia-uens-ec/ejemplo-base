from django import forms

class FormBusqueda(forms.Form):
    filtro = forms.CharField(label="Filtrar por", required=False)
    otro = forms.BooleanField(label="Prueba", required=False)