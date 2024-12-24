from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el Nombre del Laboratorio'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese la Ciudad del Laboratorio'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el País del Laboratorio'}),
        }