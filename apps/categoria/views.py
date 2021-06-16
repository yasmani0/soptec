from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.categoria.forms import CategoriaForm
from apps.categoria.models import Categoria
from django.contrib.auth.models import User
from apps.pedido.models import Pedido, PedidoEspecifico
from apps.datoscuenta.models import DatosCuenta
from apps.datoscuenta.forms import DatosCuentaForm
from django.contrib import messages
import json


# Create your views here.


def index(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        categoria = Categoria.objects.all()
        datos_cuenta = DatosCuenta.objects.all()
        form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)

        if request.method == 'POST':
            form = CategoriaForm(request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Categoria agregada correctamente")
            else:
                messages.error(request, "El nombre de la categoria ya existe")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = CategoriaForm()
            contexto = {'categoria': categoria, 'form': form,'datos_cuenta': datos_cuenta,'form_cuenta': form_cuenta}
        return render(request, 'categoria/index.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html' )


def update(request, id):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        categoria = Categoria.objects.get(id=id)
        if request.method == 'POST':
            forms = CategoriaForm(
                request.POST, instance=categoria, files=request.FILES)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Categoria actualizada correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse(json.dumps("El servicio ya existe"), content_type="application/json")
        else:
            forms = CategoriaForm(instance=categoria)
            return render(request, 'categoria/update.html', {'categoria': categoria, 'forms': forms})
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html' )


def categoria_listar(request):
    categoria = Categoria.objects.all().order_by('id')
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(cliente=cliente, estado=False)
        items = pedido.pedidoespecifico_set.all()
        cartItems = pedido.get_cart_items
    else:
        return render(request, 'categoriaProductoSL/index.html', {'categoria': categoria})
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = pedido['pedido.get_cart_items']

    contexto = {'categoria': categoria, 'cartItems': cartItems}
    return render(request, 'categoriaProducto/index.html', contexto)
