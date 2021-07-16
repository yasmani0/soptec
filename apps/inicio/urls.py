from django.urls import path
from apps.inicio.views import index, terminos_servicios, politica_privacidad, pedido_cancelado, pedido_cancelado_envio, mis_pedidos, detalle_pedidos, detalle_imagen_comprobante, local_detalle_pedidos, local_detalle_imagen_comprobante, local_pedido_cancelado, admin_pedido_cancelado, local_asistentes_detalle_pedidos, local_asistentes_detalle_imagen_comprobante, local_asistentes_pedido_cancelado
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name="Inicio"),
    path('terminos_servicios/', terminos_servicios, name="Terminos_Servicios"),
    path('politica_privacidad/', politica_privacidad, name="Politica_Privacidad"),

    path('cancelado/<int:id>/', pedido_cancelado, name="Pedido_Cancelado"),
    path('cancelado/envio/<int:id>/', pedido_cancelado_envio,
         name="Pedido_Cancelado_Envio"),
    path('mis_pedidos/', login_required(mis_pedidos), name="Mis_Pedidos"),
    path('detalle/<int:id>/', detalle_pedidos, name="Detalle_Pedidos"),
    path('detalle_comprobante/<int:id>/',
         detalle_imagen_comprobante, name="Detalle_Comprobante"),
    path('local_detalle/<int:id>/', local_detalle_pedidos,
         name="Local_Detalle_Pedidos"),
    path('local_detalle_comprobante/<int:id>/',
         local_detalle_imagen_comprobante, name="Local_Detalle_Comprobante"),
    path('local_pedido_canceladof/<int:id>/',
         login_required(local_pedido_cancelado), name="Local_Pedido_CanceladoF"),
    path('admin_pedido_canceladof/<int:id>/',
         login_required(admin_pedido_cancelado), name="Admin_Pedido_CanceladoF"),

    path('local_asistente_detalle/<int:id>/', local_asistentes_detalle_pedidos,
         name="Local_Asistentes_Detalle_Pedidos"),
    path('local_asistentes_detalle_comprobante/<int:id>/',
         local_asistentes_detalle_imagen_comprobante, name="Local_Asistentes_Detalle_Comprobante"),
    path('local_asistente_pedido_canceladof/<int:id>/',
         login_required(local_asistentes_pedido_cancelado), name="Local_Asistentes_Pedido_CanceladoF"),



]
