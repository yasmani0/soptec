from django.db import models
from apps.categoria.models import Categoria
from apps.marca.models import Marca
from cloudinary.models import CloudinaryField

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(
        max_length=100, blank=False, unique=True, null=False)
    precio = models.FloatField(max_length=10, blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False, default="1")
    imagen = CloudinaryField('imagen', null=True)
    estado = models.CharField(max_length=2, blank=True, null=True, default="1")
    descripcion = models.TextField(
        max_length=500, blank=False, null=False, default="")
    id_categoria = models.ForeignKey(
        Categoria, null=False, blank=False, on_delete=models.CASCADE, default="1")
    id_marca = models.ForeignKey(
        Marca, null=False, blank=False, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return '{}'.format(self.nombre)
