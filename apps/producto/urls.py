from django.urls import path
from apps.producto.views import index, update, update1, update2, update3, detalle_producto, cart, checkout, updatePedidoEspecifico, pedidoProcesados, prueba
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name="Producto"),
    path('update/<int:id>/', login_required(update2), name="producto_update"),
    path('detalle/<int:id>/', detalle_producto, name="producto_detalle"),
    path('carrito/', cart, name="Cart_detalle"),
    path('checkout/', checkout, name="Verificar_pago"),
    path('update_producto_especifico/', updatePedidoEspecifico,
         name="update_producto_especifico"),
    path('pedido_procesado/', pedidoProcesados,
         name="pedido_procesado"),
    path('prueba/', prueba,
         name="prueba"),
]
