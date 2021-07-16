from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.pedido.models import Pedido, PedidoEspecifico, MetodoEnvio
from django.contrib.auth.models import User
from apps.comprobante.models import Comprobante
from django.views.generic import TemplateView
from apps.producto.models import Producto
from apps.cliente.models import Cliente
from apps.inicio.serializers import *
from django.contrib import messages
from django.db import connection
import json


def index(request):
    clientes = Cliente.objects.raw(
        "select u.id, u.username, u.first_name, u.last_name, email, u.is_active, c.tipo_usuario, c.id_cliente_id from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id where u.id=" +
        str(request.user.id)
    )
    contexto = {'clientes': clientes}
    return render(request, 'base/base.html', contexto)


def terminos_servicios(request):
    clientes = Cliente.objects.raw(
        "select u.id, u.username, u.first_name, u.last_name, email, u.is_active, c.tipo_usuario, c.id_cliente_id from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id where u.id=" +
        str(request.user.id)
    )
    contexto = {'clientes': clientes}
    return render(request, 'terminos_servicios/index.html', contexto)


def politica_privacidad(request):
    clientes = Cliente.objects.raw(
        "select u.id, u.username, u.first_name, u.last_name, email, u.is_active, c.tipo_usuario, c.id_cliente_id from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id where u.id=" +
        str(request.user.id)
    )
    contexto = {'clientes': clientes}
    return render(request, 'politica_privacidad/index.html', contexto)


class Error404View(TemplateView):
    template_name = 'errores/404/index.html'


class Error500View(TemplateView):
    template_name = 'errores/500/index.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()

        def view(request):
            r = v(request)
            r.render()
            return r
        return view


def pedido_cancelado(request, id):
    estado = 2
    try:
        cursor = connection.cursor()
        cursor.execute("Update pedido_pedido set estadoc='" +
                       str(estado) + "', disponibilidad='"+str(estado)+"' where id="+str(id))
        messages.success(request, "Pedido cancelado")
        return redirect("Inicio")
    except:
        return HttpResponse(json.dumps("Error  1"), content_type="application/json")

    return redirect("Inicio")


def pedido_cancelado_envio(request, id):
    estado = 2
    try:
        cursor = connection.cursor()
        cursor.execute("Update pedido_pedido set estadoc='" +
                       str(estado) + "', disponibilidad='"+str(estado)+"' where id="+str(id))
        messages.success(request, "Pedido cancelado")
        return redirect("Inicio")
    except:
        return HttpResponse(json.dumps("Error  1"), content_type="application/json")

    return redirect("Inicio")


def mis_pedidos(request):

    clientes = Cliente.objects.raw(
        "select u.id, u.username, u.first_name, u.last_name, email, u.is_active, c.tipo_usuario, c.id_cliente_id from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id where u.id=" +
        str(request.user.id)
    )

    misPedidos = Pedido.objects.raw(
        'SELECT p.id, p."totalPagar", p.fecha_pedido, (p."totalPagar" * 0) + 5 as iva, p."totalPagar" + 5 as totalf FROM public.pedido_pedido as p where estado=true AND cliente_id='+str(
            request.user.cliente.id)+'ORDER BY p.id DESC'
    )
    context = {'misPedidos': misPedidos, 'clientes': clientes}
    return render(request, 'pedido/mispedidos.html', context)


def detalle_pedidos(request, id):
    if request.method == 'GET':

        productos = PedidoEspecifico.objects.raw(
            'select proe.id, proe.cantidad, proe.pedido_id, proe.producto_id, pro.nombre, pro.precio, pro.imagen, proe.cantidad * pro.precio as subtotal from pedido_pedidoespecifico as proe inner join producto_producto as pro on proe.producto_id=pro.id where proe.pedido_id='+str(id))

        totales = Pedido.objects.raw(
            'SELECT p.id, p.tipo_envio, p."totalPagar", (p."totalPagar" * 0) + 5 as iva, p."totalPagar" + 5 as totalf FROM public.pedido_pedido as p where estado=true AND id='+str(id))

    context = {'productos': productos, 'totales': totales}
    return render(request, 'pedido/detallepedidos.html', context)


def detalle_imagen_comprobante(request, id):
    if request.method == 'GET':
        comprobante = Comprobante.objects.filter(id_pedido=id)

    context = {'comprobante': comprobante}
    return render(request, 'pedido/vercomprobante.html', context)


def admin_pedido_cancelado(request, id):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        estado = 2
        estadofinal = 3
        try:
            cursor = connection.cursor()
            cursor.execute("Update pedido_pedido set estado=false, estadoc='" +
                           str(estado) + "', disponibilidad='"+str(estadofinal)+"' where id="+str(id))
            messages.success(request, "Pedido eliminado")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponse(json.dumps("Error  1"), content_type="application/json")
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


# admin local


def local_detalle_pedidos(request, id):
    if request.method == 'GET':

        productos = PedidoEspecifico.objects.raw(
            'select proe.id, proe.cantidad, proe.pedido_id, proe.producto_id, pro.nombre, pro.precio, pro.imagen, proe.cantidad * pro.precio as subtotal from pedido_pedidoespecifico as proe inner join producto_producto as pro on proe.producto_id=pro.id where proe.pedido_id='+str(id))

        totales = Pedido.objects.raw(
            'SELECT p.id, p.tipo_envio , p."totalPagar", (p."totalPagar" * 0) + 5 as iva, p."totalPagar" + (5) as totalf FROM public.pedido_pedido as p where estado=true AND id='+str(id))

    context = {'productos': productos, 'totales': totales}
    return render(request, 'LocalFuncionalidades/pedido/detallepedidos.html', context)


def local_detalle_imagen_comprobante(request, id):
    if request.method == 'GET':
        comprobante = Comprobante.objects.filter(id_pedido=id)

    context = {'comprobante': comprobante}
    return render(request, 'LocalFuncionalidades/pedido/vercomprobante.html', context)


def local_pedido_cancelado(request, id):
    is_admin_local = User.objects.filter(
        id=request.user.id)
    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=2)
    if is_admin_local and is_tipo_usuario:
        estado = 2
        estadofinal = 3
        try:
            cursor = connection.cursor()
            cursor.execute("Update pedido_pedido set estado=false, estadoc='" +
                           str(estado) + "', disponibilidad='"+str(estadofinal)+"' where id="+str(id))
            messages.success(request, "Pedido eliminado")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponse(json.dumps("Error  1"), content_type="application/json")
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')

# asistentes


def local_asistentes_detalle_pedidos(request, id):
    if request.method == 'GET':

        productos = PedidoEspecifico.objects.raw(
            'select proe.id, proe.cantidad, proe.pedido_id, proe.producto_id, pro.nombre, pro.precio, pro.imagen, proe.cantidad * pro.precio as subtotal from pedido_pedidoespecifico as proe inner join producto_producto as pro on proe.producto_id=pro.id where proe.pedido_id='+str(id))

        totales = Pedido.objects.raw(
            'SELECT p.id, p.tipo_envio , p."totalPagar", (p."totalPagar" * 0) + 5 as iva, p."totalPagar" + (5) as totalf FROM public.pedido_pedido as p where estado=true AND id='+str(id))

    context = {'productos': productos, 'totales': totales}
    return render(request, 'LocalAsistentesFuncionalidades/pedido/detallepedidos.html', context)


def local_asistentes_detalle_imagen_comprobante(request, id):
    if request.method == 'GET':
        comprobante = Comprobante.objects.filter(id_pedido=id)

    context = {'comprobante': comprobante}
    return render(request, 'LocalAsistentesFuncionalidades/pedido/vercomprobante.html', context)


def local_asistentes_pedido_cancelado(request, id):
    is_admin_local = User.objects.filter(
        id=request.user.id)
    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=3)
    if is_admin_local and is_tipo_usuario:
        estado = 2
        estadofinal = 3
        try:
            cursor = connection.cursor()
            cursor.execute("Update pedido_pedido set estado=false, estadoc='" +
                           str(estado) + "', disponibilidad='"+str(estadofinal)+"' where id="+str(id))
            messages.success(request, "Pedido eliminado")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponse(json.dumps("Error  1"), content_type="application/json")
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')
