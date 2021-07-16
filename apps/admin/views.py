from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import connection
from apps.admin.serializers import *
from apps.datoscuenta.models import DatosCuenta
from apps.datoscuenta.forms import DatosCuentaForm
from apps.cliente.models import Cliente
from apps.pedido.models import Pedido
from django.contrib import messages
from datetime import datetime
import json


def index(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        datos_cuenta = DatosCuenta.objects.all()
        pedidoP = Pedido.objects.filter(estado=True, disponibilidad=0).count()
        pedidoC = Pedido.objects.filter(estado=True, disponibilidad=1).count()
        pedidoCan = Pedido.objects.filter(
            estado=True, disponibilidad=2).count()

        operacionesRec = Pedido.objects.raw(
            'SELECT id, tipo_envio ,"totalPagar", fecha_pedido, disponibilidad, ("totalPagar" * 0) + 5 as iva, "totalPagar" + (5) as totalf FROM public.pedido_pedido where estado=true AND NOT disponibilidad>2::text ORDER BY id DESC LIMIT 10'
        )

        usuariosReg = User.objects.filter(
            is_active=True, is_superuser=False).count()

        # grafica
        try:
            pedido_completado_grafica_data = []
            pedido_pendiente_grafica_data = []
            pedido_cancelado_grafica_data = []
            year = datetime.now().year
            # obteniendo pedidos completados
            for m in range(1, 13):
                datosgrafica = Pedido.objects.filter(
                    fecha_pedido__year=year, fecha_pedido__month=m, disponibilidad=1, estado=True).count()
                pedido_completado_grafica_data.append(int(datosgrafica))

            # obteniendo pedidos pendientes
            for m in range(1, 13):
                datosgraficapp = Pedido.objects.filter(
                    fecha_pedido__year=year, fecha_pedido__month=m, disponibilidad=0, estado=True).count()
                pedido_pendiente_grafica_data .append(
                    int(datosgraficapp))

            # obteniendo pedidos cancelados
            for m in range(1, 13):
                datosgraficapc = Pedido.objects.filter(
                    fecha_pedido__year=year, fecha_pedido__month=m, disponibilidad=2, estado=True).count()
                pedido_cancelado_grafica_data .append(
                    int(datosgraficapc))
        except:
            pass

        if request.method == 'POST':
            form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
            nombre_persona = request.POST.get('nombre_persona')
            nombre_banco = request.POST.get('nombre_banco')
            numero = request.POST.get('numero_cuenta')

            try:
                DatosCuenta.objects.create(
                    nombre_persona=nombre_persona,
                    nombre_banco=nombre_banco,
                    numero_cuenta=numero
                )
                messages.success(request, "Cuenta agregada correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                messages.error(
                    request, "Cuenta o numero de ya existente, ingrese otra cuenta")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form_cuenta = DatosCuentaForm()
            contexto = {'datos_cuenta': datos_cuenta, 'form_cuenta': form_cuenta, 'pedidoP': pedidoP,
                        'pedidoC': pedidoC, 'pedidoCan': pedidoCan, 'usuariosReg': usuariosReg, 'operacionesRec': operacionesRec, 'pedido_completado_grafica_data': pedido_completado_grafica_data, 'pedido_pendiente_grafica_data': pedido_pendiente_grafica_data, 'pedido_cancelado_grafica_data': pedido_cancelado_grafica_data}
        return render(request, 'base_admin/base.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


def update(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        if request.method == 'POST':
            id_cuenta = request.POST.get('id_cuenta')
            nombre_banco = request.POST.get('nombre_banco')
            nombre_persona = request.POST.get('nombre_persona')
            numero = request.POST.get('numero_cuenta')
            estado = request.POST.get('estado')
            # print("id: ", id_cuenta, "nombre: ", nombre,
            #       "numero: ", numero, "estado: ", estado)
            try:
                if id_cuenta:
                    cursor = connection.cursor()
                    cursor.execute("Update datoscuenta_datoscuenta set nombre_banco='"+str(nombre_banco)+"', nombre_persona='"+str(nombre_persona)+"', numero_cuenta='"+str(
                        numero)+"', estado='"+str(estado)+"' where id="+str(id_cuenta))
                    messages.success(
                        request, "Cuenta actualizada correctamente")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                return HttpResponse(json.dumps("Error  1"), content_type="application/json")

            return HttpResponse(json.dumps(""), content_type="application/json")
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


def admuser(request):
    if request.user.is_authenticated:
        is_admin = User.objects.filter(
            id=request.user.id).filter(is_superuser=1)
        if is_admin:
            datos_cuenta = DatosCuenta.objects.all()
            form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
            cursor = connection.cursor()
            usuarios = Cliente.objects.raw(
                "select u.id, u.username, u.first_name, u.last_name, email, u.is_active, c.tipo_usuario, c.id_cliente_id from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id where u.is_superuser='0' ORDER BY u.id desc"
            )
            # usuarios = User.objects.raw(
            #     "select id, username, first_name, last_name, email, is_active from auth_user where is_superuser='0' ORDER BY id asc")
            user = {'usuarios': usuarios, 'datos_cuenta': datos_cuenta,
                    'form_cuenta': form_cuenta}

            return render(request, 'usuario/index.html', user)
        else:
            messages.error(request, "Acceso denegado")
            return render(request, 'base/base.html')


def usuario_register_adm(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        if request.method == 'POST':
            username = request.POST.get('usuario_reg_adm').lower()
            tipousuario = request.POST.get('id_tiposuario')
            nombre = request.POST.get('nombre_reg_adm')
            apellido = request.POST.get('apellido_reg_adm')
            email = request.POST.get('email_reg_adm')
            clave = request.POST.get('clave_reg_adm')

            if tipousuario != '1' or tipousuario != '2' or tipousuario != '3':
                messages.error(request, "Acceso denegado")
                return redirect("usuario_salir")

            try:
                user = User.objects.create_user(
                    username=username,
                    first_name=nombre,
                    last_name=apellido,
                    email=email,
                    password=clave
                )

                Cliente.objects.create(
                    id_cliente_id=user.id, tipo_usuario=tipousuario)

                messages.success(request, "Usuario agregado correctamente")

                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                messages.error(
                    request, "Usuario ya registrado, ingrese otro usuario")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')


# función para actualizar el perfil


def usuario_actualizar_adm(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        if request.method == 'POST':
            id_user = request.POST.get('id_upd_adm')
            tipousuario = request.POST.get('tipousuario_upd_adm')
            username = request.POST.get('usuario_upd_adm').lower()
            nombre = request.POST.get('nombre_upd_adm')
            apellido = request.POST.get('apellido_upd_adm')
            email = request.POST.get('email_upd_adm')
            estado = request.POST.get('estado_upd_adm')
            clave_pasada = request.POST.get('clave_pasada_upd_adm')
            clave_nueva = request.POST.get('clave_nueva_upd_adm')
            verif_user = User.objects.filter(username=username).count()

            if tipousuario != '1' or tipousuario != '2' or tipousuario != '3':
                messages.error(request, "Acceso denegado")
                return redirect("usuario_salir")

            if estado == "0":
                estado = False
            else:
                estado = True

            if verif_user > 2:
                return HttpResponse(json.dumps("YA EXISTE 111"), content_type="application/json")
            else:
                try:
                    if username:
                        cursor = connection.cursor()

                        try:
                            cursor.execute("Update auth_user set username='"+str(username)+"', first_name='"+str(nombre)+"', last_name='"+str(
                                apellido)+"', email='"+str(email)+"' , is_active='"+str(estado)+"' where id="+str(id_user))
                            cursor.execute("Update cliente_cliente set tipo_usuario='"+str(
                                tipousuario)+"' where id_cliente_id="+str(id_user))
                        except:
                            pass

                        user = User.objects.get(id=id_user)
                        if user.check_password(clave_pasada):
                            user.set_password(clave_nueva)
                            user.save()
                        messages.success(
                            request, "Usuario actualizado correctamente")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                except:
                    messages.error(
                        request, "Usuario ya registrado, ingrese otro usuario")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return HttpResponse(json.dumps(""), content_type="application/json")
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html')

# función para actualizar el perfil del admin y local


def perfil_actualizar_adm(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    is_admin_local = User.objects.filter(
        id=request.user.id)

    is_tipo_usuario = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=2)

    is_tipo_usuario_asistente = Cliente.objects.filter(
        id_cliente=request.user.id, tipo_usuario=3)
    if is_admin:
        if request.method == 'POST':
            id_adm = request.POST.get('id_adm')
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            email = request.POST.get('email')
            cedula = request.POST.get('cedula')
            telefono = request.POST.get('telefono')

            try:
                if id_adm:
                    cursor = connection.cursor()
                    cursor.execute("Update auth_user set first_name='"+str(nombre)+"', last_name='"+str(
                        apellido)+"', email='"+str(email)+"' where id="+str(id_adm))

                    cursor.execute("Update cliente_cliente set cedula='"+str(cedula)+"', telefono='"+str(
                        telefono)+"' where id_cliente_id="+str(id_adm))

                    messages.success(
                        request, "Perfil actualizado correctamente")

                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                return HttpResponse(json.dumps("Error  1"), content_type="application/json")

            return HttpResponse(json.dumps(""), content_type="application/json")
    else:
        if is_admin_local and is_tipo_usuario:
            if request.method == 'POST':
                id_adm = request.POST.get('id_adm')
                nombre = request.POST.get('nombre')
                apellido = request.POST.get('apellido')
                email = request.POST.get('email')
                cedula = request.POST.get('cedula')
                telefono = request.POST.get('telefono')

                try:
                    if id_adm:
                        cursor = connection.cursor()
                        cursor.execute("Update auth_user set first_name='"+str(nombre)+"', last_name='"+str(
                            apellido)+"', email='"+str(email)+"' where id="+str(id_adm))

                        cursor.execute("Update cliente_cliente set cedula='"+str(cedula)+"', telefono='"+str(
                            telefono)+"' where id_cliente_id="+str(id_adm))

                        messages.success(
                            request, "Perfil actualizado correctamente")

                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                except:
                    messages.error(
                        request, "Cedula ya registrada, ingrese otra cedula")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                return HttpResponse(json.dumps(""), content_type="application/json")
        else:
            if is_admin_local and is_tipo_usuario_asistente:
                if request.method == 'POST':
                    id_adm = request.POST.get('id_adm')
                    nombre = request.POST.get('nombre')
                    apellido = request.POST.get('apellido')
                    email = request.POST.get('email')
                    cedula = request.POST.get('cedula')
                    telefono = request.POST.get('telefono')

                    try:
                        if id_adm:
                            cursor = connection.cursor()
                            cursor.execute("Update auth_user set first_name='"+str(nombre)+"', last_name='"+str(
                                apellido)+"', email='"+str(email)+"' where id="+str(id_adm))

                            cursor.execute("Update cliente_cliente set cedula='"+str(cedula)+"', telefono='"+str(
                                telefono)+"' where id_cliente_id="+str(id_adm))

                            messages.success(
                                request, "Perfil actualizado correctamente")

                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    except:
                        messages.error(
                            request, "Cedula ya registrada, ingrese otra cedula")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                    return HttpResponse(json.dumps(""), content_type="application/json")
            else:
                messages.error(request, "Acceso denegado")
                return render(request, 'base/base.html')
