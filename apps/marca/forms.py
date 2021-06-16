from django import forms
from apps.marca.models import Marca
from django.forms import ValidationError


class MarcaForm(forms.ModelForm):

    # id_categoria = forms.Select(required=True)
    # def clean_nombre(self):
    #     nombre = self.cleaned_data.get("nombre")
    #     existe = Marca.objects.filter(nombre=nombre).exists()
    #     if existe:
    #         raise ValidationError("Este nombre ya existe")
    #     return nombre

    class Meta:

        nombre = forms.CharField(required=True)

        model = Marca
        fields = [
            'nombre',
            'estado',
            'id_categoria',
        ]

        labels = {
            'nombre': 'Nombre',
            'estado': 'Estado',
            'id_categoria': 'Categoria',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre ...'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el estado ...'}),
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),
        }
