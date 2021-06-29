from django.db import models
from apps.cliente.models import Cliente
from apps.pedido.models import Pedido
from cloudinary.models import CloudinaryField


class Comprobante(models.Model):
    nombre = models.CharField(
        max_length=100, blank=False, null=False)
    imagen = CloudinaryField('imagen', null=True)
    estado = models.CharField(max_length=2, blank=True, null=True, default="1")
    id_cliente = models.ForeignKey(
        Cliente, null=True, blank=True, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(
        Pedido, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)
