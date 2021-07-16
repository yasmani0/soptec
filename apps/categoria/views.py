from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.categoria.forms import CategoriaForm
from apps.categoria.models import Categoria
from apps.cliente.models import Cliente
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
            contexto = {'categoria': categoria, 'form': form,
                        'datos_cuenta': datos_cuenta, 'form_cuenta': form_cuenta}
        return render(request, 'categoria/index.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


def update(request, id):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        categoria = Categoria.objects.get(id=id)
        if request.method == 'POST':
            forms = CategoriaForm(
                request.POST, instance=categoria, files=request.FILES)
            if forms.is_valid():
                forms.save()
                messages.success(
                    request, "Categoria actualizada correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse(json.dumps("El servicio ya existe"), content_type="application/json")
        else:
            forms = CategoriaForm(instance=categoria)
            return render(request, 'categoria/update.html', {'categoria': categoria, 'forms': forms})
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')

# admin local


def indexlocal(request):
    is_admin_local = User.objects.filter(
        id=request.user.id)
    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=2)
    if is_admin_local and is_tipo_usuario:
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
            contexto = {'categoria': categoria, 'form': form,
                        'datos_cuenta': datos_cuenta, 'form_cuenta': form_cuenta}
        return render(request, 'LocalFuncionalidades/categoria/index.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


def updatelocal(request, id):
    is_admin_local = User.objects.filter(
        id=request.user.id)
    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=2)
    if is_admin_local and is_tipo_usuario:
        categoria = Categoria.objects.get(id=id)
        if request.method == 'POST':
            forms = CategoriaForm(
                request.POST, instance=categoria, files=request.FILES)
            if forms.is_valid():
                forms.save()
                messages.success(
                    request, "Categoria actualizada correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse(json.dumps("El servicio ya existe"), content_type="application/json")
        else:
            forms = CategoriaForm(instance=categoria)
            return render(request, 'LocalFuncionalidades/categoria/update.html', {'categoria': categoria, 'forms': forms})
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')

# asitentes


def index_asistente_local(request):
    is_asistente_local = User.objects.filter(
        id=request.user.id)
    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=3)
    if is_asistente_local and is_tipo_usuario:
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
            contexto = {'categoria': categoria, 'form': form,
                        'datos_cuenta': datos_cuenta, 'form_cuenta': form_cuenta}
        return render(request, 'LocalAsistentesFuncionalidades/categoria/index.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


def update_asistente_local(request, id):
    is_asistente_local = User.objects.filter(
        id=request.user.id)
    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=3)
    if is_asistente_local and is_tipo_usuario:
        categoria = Categoria.objects.get(id=id)
        if request.method == 'POST':
            forms = CategoriaForm(
                request.POST, instance=categoria, files=request.FILES)
            if forms.is_valid():
                forms.save()
                messages.success(
                    request, "Categoria actualizada correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse(json.dumps("El servicio ya existe"), content_type="application/json")
        else:
            forms = CategoriaForm(instance=categoria)
            return render(request, 'LocalAsistentesFuncionalidades/categoria/update.html', {'categoria': categoria, 'forms': forms})
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


# listar cliente
def categoria_listar(request):
    categoria = Categoria.objects.all().order_by('id')

    clientes = Cliente.objects.raw(
        "select u.id, u.username, u.first_name, u.last_name, email, u.is_active, c.tipo_usuario, c.id_cliente_id from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id where u.id=" +
        str(request.user.id)
    )

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(
            cliente=cliente, estado=False)
        items = pedido.pedidoespecifico_set.all()
        cartItems = pedido.get_cart_items
    else:
        return render(request, 'categoriaProductoSL/index.html', {'categoria': categoria, 'clientes': clientes})
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = pedido['pedido.get_cart_items']

    contexto = {'categoria': categoria,
                'cartItems': cartItems, 'clientes': clientes}
    return render(request, 'categoriaProducto/index.html', contexto)
