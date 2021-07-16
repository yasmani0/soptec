from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db import connection
# login, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from apps.cliente.models import Cliente
import json

# Create your views here.


def usuario_login(request):

    if request.method == 'POST':
        usuario = request.POST.get('users_login')
        password = request.POST.get('pass_login')

        is_admin = User.objects.filter(username=usuario).filter(is_superuser=1)

        is_admin_local = User.objects.filter(
            username=usuario)

        admin_locales = Cliente.objects.raw(
            "select u.id, u.username, u.is_active, c.tipo_usuario from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id"
        )

        if is_admin:
            user = authenticate(request, username=usuario, password=password)
            if user is not None:
                login(request, user)
                return redirect("Admin")

        if admin_locales:

            for adml in admin_locales:

                if adml.username == usuario and adml.tipo_usuario == '2' and adml.is_active == True:
                    user = authenticate(
                        request, username=usuario, password=password)
                    login(request, user)
                    messages.success(
                        request, "Inicio de sesión correctamente")
                    return redirect("LocalAdmin")

                if adml.username == usuario and adml.tipo_usuario == '3' and adml.is_active == True:
                    user = authenticate(
                        request, username=usuario, password=password)
                    login(request, user)
                    messages.success(
                        request, "Inicio de sesión correctamente")
                    return redirect("AsistenteLocal")

        verif_usuario_aux = User.objects.filter(username=usuario)
        if verif_usuario_aux:
            verif_usuario_aux = User.objects.get(username=usuario)
        kwargs = {'username': usuario}

        if verif_usuario_aux:
            verif_usuario = User.objects.filter(id=verif_usuario_aux.id)
            if verif_usuario:
                verif_usuario = User.objects.get(id=verif_usuario_aux.id)
                # return HttpResponse(json.dumps(verif_usuario.is_active), content_type="application/json")
                if verif_usuario.is_active:
                    user = authenticate(
                        request, username=usuario, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(
                            request, "Inicio de sesión correctamente")
                        return redirect("Inicio")
                    else:
                        messages.error(
                            request, "Usuario o contraseña incorrecta")
                        return redirect("Inicio")
                else:
                    messages.error(
                        request, "Lo sentimos tu cuenta ha sido deshabilitada")
                    return redirect("Inicio")
            else:
                messages.error(
                    request, "No exite esta cuenta, por favor registrese")
                return redirect("Inicio")
        else:
            messages.error(
                request, "No exite esta cuenta, por favor registrese")
            return redirect("Inicio")

        messages.error(
            request, "No exite esta cuenta, por favor registrese")
        return redirect("Inicio")


def salir(request):
    logout(request)
    return redirect("Inicio")


def usuario_register(request):
    if request.method == 'POST':
        username = request.POST.get('usuario_reg').lower()
        nombre = request.POST.get('nombre_reg')
        apellido = request.POST.get('apellido_reg')
        email = request.POST.get('email_reg')
        clave = request.POST.get('clave_reg')

        try:
            user = User.objects.create_user(
                username=username,
                first_name=nombre,
                last_name=apellido,
                email=email,
                password=clave
            )

            # cli = Cliente()
            # cli.id_cliente_id = user.id
            # cli.cedula = ''
            # cli.telefono = ''
            # cli.save()

            print("El id es: ", user.id-1)

            Cliente.objects.create(id_cliente_id=user.id)

            messages.success(
                request, "Usuario registrado correctamente, inicie sesión ...")
            return render(request, 'base/base.html')
        except:
            messages.success(
                request, "Nombre del usuario ya existe, ingrese otro usuario ...")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# función para actualizar el perfil


def usuario_perfil(request):
    if request.method == 'POST':
        id_user = request.POST.get('id_user')
        username = request.POST.get('usuario_update').lower()
        nombre = request.POST.get('nombre_update')
        apellido = request.POST.get('apellido_update')
        email = request.POST.get('email_update')
        clave_pasada = request.POST.get('clave_pasada')
        # clave_nueva = request.POST.get('clave_nueva')

        verif_user = User.objects.filter(username=username).count()
        user = User.objects.get(id=id_user)

        if verif_user > 2:
            return HttpResponse(json.dumps("YA EXISTE"), content_type="application/json")
        else:
            try:
                if username:
                    cursor = connection.cursor()
                    cursor.execute("Update auth_user set username='"+str(username)+"', first_name='"+str(
                        nombre)+"', last_name='"+str(apellido)+"' , email='"+str(email)+"' where id="+str(id_user))

                    # if user.check_password(clave_pasada):
                    #     user.set_password(clave_nueva)
                    #     user.save()
                    messages.success(request, "Editado con exito")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                return HttpResponse(json.dumps("YA EXISTE"), content_type="application/json")

    return HttpResponse(json.dumps(""), content_type="application/json")
