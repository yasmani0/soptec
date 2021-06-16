from django.db import models


class DatosCuenta(models.Model):
    nombre_banco = models.CharField(
        max_length=100, blank=False, unique=True, null=False)
    numero_cuenta = models.CharField(
        max_length=100, blank=False, unique=True, null=False)
    estado = models.CharField(max_length=2, blank=True, null=True, default="1")

    def __str__(self):
        return '{}'.format(self.nombre_banco)
