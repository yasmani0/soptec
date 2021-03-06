from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.marca.models import Marca
from apps.marca.forms import MarcaForm
from django.contrib import messages
from apps.datoscuenta.models import DatosCuenta
from apps.datoscuenta.forms import DatosCuentaForm
from apps.categoria.models import Categoria
from django.contrib.auth.models import User
from apps.cliente.models import Cliente
import json

# Create your views here.


def index(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        marca = Marca.objects.all()
        datos_cuenta = DatosCuenta.objects.all()
        categoria = Categoria.objects.filter(estado=1)
        form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
        if request.method == 'POST':
            form = MarcaForm(request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Marca agregada correctamente")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = MarcaForm()
            contexto = {'marca': marca, 'form': form,
                        'datos_cuenta': datos_cuenta, 'form_cuenta': form_cuenta, 'categoria': categoria}
        return render(request, 'marca/index.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


def update(request, id):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        marca = Marca.objects.get(id=id)
        if request.method == 'POST':
            forms = MarcaForm(
                request.POST, instance=marca, files=request.FILES)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Marca actualizada correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse(json.dumps("Error al guardar"), content_type="application/json")
        else:
            forms = MarcaForm(instance=marca)
            return render(request, 'marca/update.html', {'marca': marca, 'forms': forms})
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')

# Administracion del local


def localindex(request):

    is_admin_local = User.objects.filter(
        id=request.user.id)

    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=2)

    if is_admin_local and is_tipo_usuario:
        marca = Marca.objects.all()
        datos_cuenta = DatosCuenta.objects.all()
        categoria = Categoria.objects.filter(estado=1)
        form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
        if request.method == 'POST':
            form = MarcaForm(request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Marca agregada correctamente")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = MarcaForm()
            contexto = {'marca': marca, 'form': form,
                        'datos_cuenta': datos_cuenta, 'form_cuenta': form_cuenta, 'categoria': categoria}
        return render(request, 'LocalFuncionalidades/marca/index.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


def localupdate(request, id):
    is_admin_local = User.objects.filter(
        id=request.user.id)
    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=2)
    if is_admin_local and is_tipo_usuario:
        marca = Marca.objects.get(id=id)
        if request.method == 'POST':
            forms = MarcaForm(
                request.POST, instance=marca, files=request.FILES)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Marca actualizada correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse(json.dumps("Error al guardar"), content_type="application/json")
        else:
            forms = MarcaForm(instance=marca)
            return render(request, 'LocalFuncionalidades/marca/update.html', {'marca': marca, 'forms': forms})
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')

# asistentes


def local_asistentes_index(request):

    is_asistente_local = User.objects.filter(
        id=request.user.id)

    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=3)

    if is_asistente_local and is_tipo_usuario:
        marca = Marca.objects.all()
        datos_cuenta = DatosCuenta.objects.all()
        categoria = Categoria.objects.filter(estado=1)
        form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
        if request.method == 'POST':
            form = MarcaForm(request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Marca agregada correctamente")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = MarcaForm()
            contexto = {'marca': marca, 'form': form,
                        'datos_cuenta': datos_cuenta, 'form_cuenta': form_cuenta, 'categoria': categoria}
        return render(request, 'LocalAsistentesFuncionalidades/marca/index.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


def local_asistentes_update(request, id):
    is_asistente_local = User.objects.filter(
        id=request.user.id)
    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=3)
    if is_asistente_local and is_tipo_usuario:
        marca = Marca.objects.get(id=id)
        if request.method == 'POST':
            forms = MarcaForm(
                request.POST, instance=marca, files=request.FILES)
            if forms.is_valid():
                forms.save()
                messages.success(request, "Marca actualizada correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse(json.dumps("Error al guardar"), content_type="application/json")
        else:
            forms = MarcaForm(instance=marca)
            return render(request, 'LocalAsistentesFuncionalidades/marca/update.html', {'marca': marca, 'forms': forms})
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')
