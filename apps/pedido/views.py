from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.pedido.models import Pedido, PedidoEspecifico, MetodoEnvio
from apps.datoscuenta.forms import DatosCuentaForm
from apps.datoscuenta.models import DatosCuenta
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import connection
import json


def index(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        pedido = Pedido.objects.filter(estado=True, disponibilidad=0)
        pedidoEspecifico = PedidoEspecifico.objects.all()
        metodoEnvio = MetodoEnvio.objects.all()
        datos_cuenta = DatosCuenta.objects.all()
        form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
        context = {'pedido': pedido, 'pedidoEspecifico': pedidoEspecifico,
                'metodoEnvio': metodoEnvio, 'datos_cuenta':datos_cuenta,'form_cuenta':form_cuenta}
        return render(request, 'pedido/index.html', context)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html' )
    



def update(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        if request.method == 'POST':
            id_pedido = request.POST.get('idConf')
            estado = request.POST.get('estadoPedido')
            estadoc = 1
            try:
                if id_pedido:
                    cursor = connection.cursor()
                    cursor.execute("Update pedido_pedido set disponibilidad='" +
                                str(estado)+"', estadoc='" +
                                str(estadoc)+"' where id="+str(id_pedido))
                    messages.success(request, "Estado del pedido actualizado")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                return HttpResponse(json.dumps("Error  1"), content_type="application/json")

            return HttpResponse(json.dumps(""), content_type="application/json")
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html' )


def completados(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        pedido = Pedido.objects.filter(estado=True, disponibilidad=1)
        pedidoEspecifico = PedidoEspecifico.objects.all()
        metodoEnvio = MetodoEnvio.objects.all()
        datos_cuenta = DatosCuenta.objects.all()
        form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
        context = {'pedido': pedido, 'pedidoEspecifico': pedidoEspecifico,
                'metodoEnvio': metodoEnvio, 'datos_cuenta':datos_cuenta,'form_cuenta':form_cuenta}
        return render(request, 'pedido/completados.html', context)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html' )


def cancelados(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        pedido = Pedido.objects.filter(estado=True, disponibilidad=2)
        pedidoEspecifico = PedidoEspecifico.objects.all()
        metodoEnvio = MetodoEnvio.objects.all()
        datos_cuenta = DatosCuenta.objects.all()
        form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
        context = {'pedido': pedido, 'pedidoEspecifico': pedidoEspecifico,
                'metodoEnvio': metodoEnvio, 'datos_cuenta':datos_cuenta,'form_cuenta':form_cuenta}
        return render(request, 'pedido/cancelados.html', context)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html' )
