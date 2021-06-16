from django import forms
from apps.comprobante.models import Comprobante


class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        fields = [
            'nombre',
            'imagen',
            'estado',
            'id_cliente',
            'id_pedido',
        ]

        labels = {
            'nombre': 'Nombre',
            'imagen': 'Imagen',
            'estado': 'Estado',
            'id_cliente': 'Cliente',
            'id_pedido': 'Pedido',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre ...'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el estado ...'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la imagen'}),
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'id_pedido': forms.Select(attrs={'class': 'form-control'}),
        }
