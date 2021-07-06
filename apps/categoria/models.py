from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100, blank=False, unique=True, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    imagen = CloudinaryField('imagen', null=True)
    estado = models.CharField(max_length=2, blank=True, null=True, default="1")

    def __str__(self):
        return '{}'.format(self.nombre)
