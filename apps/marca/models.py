from django.db import models
from apps.categoria.models import Categoria

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(
        max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=2, blank=True, null=True, default="1")
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.nombre)
