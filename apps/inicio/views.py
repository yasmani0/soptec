from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from apps.pedido.models import Pedido, PedidoEspecifico, MetodoEnvio
from apps.comprobante.models import Comprobante
from apps.producto.models import Producto
from apps.inicio.serializers import *
from django.contrib import messages
from django.db import connection
import json


def index(request):
    return render(request, 'base/base.html')


def pedido_cancelado(request, id):
    estado = 2
    try:
        cursor = connection.cursor()
        cursor.execute("Update pedido_pedido set estadoc='" +
                       str(estado) + "', disponibilidad='"+str(estado)+"' where id="+str(id))
        messages.success(request, "Pedido cancelado")
        return render(request, 'base/base.html')
    except:
        return HttpResponse(json.dumps("Error  1"), content_type="application/json")

    return render(request, 'base/base.html')


def pedido_cancelado_envio(request, id):
    estado = 2
    try:
        cursor = connection.cursor()
        cursor.execute("Update pedido_pedido set estadoc='" +
                       str(estado) + "', disponibilidad='"+str(estado)+"' where id="+str(id))
        messages.success(request, "Pedido cancelado")
        return render(request, 'base/base.html')
    except:
        return HttpResponse(json.dumps("Error  1"), content_type="application/json")

    return render(request, 'base/base.html')


def mis_pedidos(request):
    misPedidos = Pedido.objects.filter(
        estado=True, cliente=request.user.cliente.id)
    context = {'misPedios': misPedidos}
    return render(request, 'pedido/mispedidos.html', context)


def detalle_pedidos(request, id):
    if request.method == 'GET':

        productos = PedidoEspecifico.objects.raw(
            'select proe.id, proe.cantidad, proe.pedido_id, proe.producto_id, pro.nombre, pro.precio, pro.imagen, proe.cantidad * pro.precio as subtotal from pedido_pedidoespecifico as proe inner join producto_producto as pro on proe.producto_id=pro.id where proe.pedido_id='+str(id))

    context = {'productos': productos}
    return render(request, 'pedido/detallepedidos.html', context)


def detalle_imagen_comprobante(request, id):
    if request.method == 'GET':
        comprobante = Comprobante.objects.filter(id_pedido=id)

    context = {'comprobante': comprobante}
    return render(request, 'pedido/vercomprobante.html', context)
