from django import forms
from apps.categoria.models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields=[
            'nombre',
            'descripcion',
            'estado',
            'imagen',
        ]
        
        labels={
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'estado':'Estado',
            'imagen':'Imagen'
            }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre ...'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la descripcion ...'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el estado ...'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }



