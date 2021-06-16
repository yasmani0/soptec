from django.urls import path
from apps.inicio.views import index, pedido_cancelado, pedido_cancelado_envio, mis_pedidos, detalle_pedidos, detalle_imagen_comprobante
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name="Inicio"),
    path('cancelado/<int:id>/', pedido_cancelado, name="Pedido_Cancelado"),
    path('cancelado/envio/<int:id>/', pedido_cancelado_envio,
         name="Pedido_Cancelado_Envio"),
    path('mis_pedidos/', login_required(mis_pedidos), name="Mis_Pedidos"),
    path('detalle/<int:id>/', detalle_pedidos, name="Detalle_Pedidos"),
    path('detalle_comprobante/<int:id>/',
         detalle_imagen_comprobante, name="Detalle_Comprobante"),

]
