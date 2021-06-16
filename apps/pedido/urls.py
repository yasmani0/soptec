from django.urls import path
from apps.pedido.views import index, update, completados, cancelados
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name="Pedidos"),
    path('update', login_required(update), name="Pedido_Update"),
    path('completados', login_required(completados), name="Pedido_Completado"),
    path('cancelados', login_required(cancelados), name="Pedido_Cancelado"),
]
