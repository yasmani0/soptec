from django import forms
from apps.producto.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'precio',
            'cantidad',
            'imagen',
            'estado',
            'descripcion',
            'id_categoria',
            'id_marca',
        ]

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'cantidad': 'Cantidad',
            'imagen': 'Imagen',
            'estado': 'Estado',
            'descripcion': 'Características / Descripción',
            'id_categoria': 'Categoria',
            'id_marca': 'Marca',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre ...'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el precio ...', 'step': '0.01'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la cantidad ...'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el estado ...'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa las imagen'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa las características o descripción ...'}),
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),
            'id_marca': forms.Select(attrs={'class': 'form-control'}),
        }
