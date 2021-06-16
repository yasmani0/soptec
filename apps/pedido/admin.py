from django.contrib import admin
from apps.pedido.models import Pedido, PedidoEspecifico, MetodoEnvio

# Register your models here.
admin.site.register(Pedido)
admin.site.register(PedidoEspecifico)
admin.site.register(MetodoEnvio)
