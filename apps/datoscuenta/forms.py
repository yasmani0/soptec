from django import forms
from apps.datoscuenta.models import DatosCuenta


class DatosCuentaForm(forms.ModelForm):
    class Meta:

        nombre_banco = forms.CharField(required=True)
        numero_cuenta = forms.CharField(required=True)

        model = DatosCuenta
        fields = [
            'nombre_banco',
            'numero_cuenta',
            'estado',
        ]

        labels = {
            'nombre_banco': 'Nombre del banco',
            'numero_cuenta': 'Número de cuenta',
            'estado': 'Estado',
        }
        widgets = {
            'nombre_banco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre del banco ...'}),
            'numero_cuenta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el numero de cuenta ...'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el estado ...'}),
        }
