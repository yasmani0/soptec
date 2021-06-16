from django.db import models
from apps.cliente.models import Cliente
from apps.producto.models import Producto

# Create your models here.


class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, blank=True, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False, blank=True, null=True)
    disponibilidad = models.CharField(
        max_length=2, blank=True, null=True, default="0")
    estadoc = models.CharField(
        max_length=2, blank=True, null=True, default="0")
    tipo_envio = models.CharField(
        max_length=2, blank=True, null=True, default="0")
    transaccion_id = models.CharField(max_length=100, null=True)
    totalPagar = models.FloatField(max_length=10, blank=True, null=True)
    imagen = models.ImageField(upload_to='img/comprobante', null=True)

    def __str__(self):
        return str(self.id)

    # total del carrito

    @property
    def get_cart_total(self):
        orderitems = self.pedidoespecifico_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.pedidoespecifico_set.all()
        total = sum([item.cantidad for item in orderitems])
        return total


class PedidoEspecifico(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, blank=True, null=True)
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(default=0, blank=True, null=True)
    fecha_agregacion = models.DateTimeField(auto_now_add=True)
    # valor total

    def __str__(self):
        return '{}'.format(self.producto)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total


class MetodoEnvio(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, blank=True, null=True)
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, blank=True, null=True)
    ciudad = models.CharField(
        max_length=200, null=True, blank=True, default="local")
    direccion = models.CharField(
        max_length=200, null=True, blank=True, default="local")

    def __str__(self):
        return '{}'.format(self.direccion)
