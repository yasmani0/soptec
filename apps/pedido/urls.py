from django.urls import path
from apps.pedido.views import index, update, completados, cancelados, local_pedidos_pendientes, local_pedidos_completados, local_pedidos_cancelados, local_pedido_update
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name="Pedidos"),
    path('completados', login_required(completados), name="Pedido_Completado"),
    path('cancelados', login_required(cancelados), name="Pedido_Cancelado"),
    path('update', login_required(update), name="Pedido_Update"),
    path('local_listar_pendientes', login_required(
        local_pedidos_pendientes), name="Local_Pedidos"),
    path('local_listar_completados', login_required(local_pedidos_completados),
         name="Local_Pedido_Completado"),
    path('local_listar_cancelados', login_required(local_pedidos_cancelados),
         name="Local_Pedido_Cancelado"),
    path('local_pedido_update', login_required(local_pedido_update),
         name="Local_Pedido_Update"),

]
