from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.producto.models import Producto
from apps.producto.forms import ProductoForm
from apps.categoria.models import Categoria
from apps.marca.models import Marca
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
from apps.pedido.models import Pedido, PedidoEspecifico, MetodoEnvio
from apps.datoscuenta.models import DatosCuenta
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.contrib import messages
from apps.cliente.models import Cliente
from apps.datoscuenta.models import DatosCuenta
from apps.datoscuenta.forms import DatosCuentaForm

import datetime
import json

# Create your views here.


def index(request):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        producto = Producto.objects.all()
        categoria = Categoria.objects.all()
        marca = Marca.objects.all().order_by('nombre')
        datos_cuenta = DatosCuenta.objects.all()
        form_cuenta = DatosCuentaForm(request.POST, files=request.FILES)
        

        if request.method == 'POST':
            # id = request.POST.get('id_cat')
            form = ProductoForm(request.POST, files=request.FILES)
            if form.is_valid():
                # form.instance.id_categoria = id
                form.id_marca = request.POST.get('id_marca')
                form.save()
                messages.success(request, "Producto agregado correctamente")
            else:
                messages.error(request, "El nombre del producto ya existe")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = ProductoForm()
            contexto = {'producto': producto, 'form': form,
                        'categoria': categoria, 'marca': marca,'datos_cuenta':datos_cuenta,'form_cuenta':form_cuenta}
        return render(request, 'producto/index.html', contexto)
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html' )

# def update(request, id):
#     producto = Producto.objects.get(id=id)
#     if request.method == 'POST':
#         forms = ProductoForm(request.POST, instance=producto, files=request.FILES)
#         if forms.is_valid():
#             forms.save()
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#         else:
#             return HttpResponse(json.dumps("El producto ya existe"), content_type="application/json")
#     else:
#         forms = ProductoForm(instance=producto)
#         return render(request, 'producto/update.html', {'producto': producto, 'forms': forms})


def update(request, id):
    if request.user.is_authenticated:
        is_admin = User.objects.filter(
            id=request.user.id).filter(is_superuser=1)
        if is_admin:
            producto = Producto.objects.get(id=id)
            aux3 = request.POST.get('id')
            if request.method == 'POST':
                form = ProductoForm(
                    request.POST, instance=producto, files=request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(
                        request, "Producto actualizado correctamente")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                form = ProductoForm(instance=producto)

            return render(request, 'producto/update.html', {'producto': producto, 'form': form})
        else:
            return HttpResponse("Acceso Denegado Admin")
    


class update1(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/update.html'
    success_url = reverse_lazy('producto/index.html')


def update2(request, id):
    is_admin = User.objects.filter(id=request.user.id).filter(is_superuser=1)
    if is_admin:
        producto = Producto.objects.get(id=id)
        if request.method == "POST":
            form = ProductoForm(request.POST, instance=producto,
                                files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Producto actualizado correctamente")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse(json.dumps("El servicio ya existe"), content_type="application/json")
        else:
            form = ProductoForm(instance=producto)
        return render(request, 'producto/update.html', {'form': form})
    else:
        messages.error(request, "Acceso denegado")
        return render(request, 'base/base.html' )


def update3(request):
    if request.method == 'POST':
        id_pro = request.POST.get('id_pro')
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        estado = request.POST.get('estado')
        imagen = request.POST.get('imagen')
        descripcion = request.POST.get('descripcion')
        id_categoria = request.POST.get('id_categoria')
        try:
            if id_pro:
                cursor = connection.cursor()
                cursor.execute("Update producto_producto set nombre='"+str(nombre)+"', precio='"+str(precio)+"', cantidad='" + str(cantidad) +
                               "' , estado='" + str(estado) + "' , imagen='" + str(imagen) + "' , descripcion='"+str(descripcion)+"', id_categoria_id='"+str(id_categoria)+"' where id="+str(id_pro))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
            return HttpResponse(json.dumps(imagen), content_type="application/json")

    return HttpResponse(json.dumps(""), content_type="application/json")


def detalle_producto(request, id):
    producto = Producto.objects.filter(estado=1, id_categoria_id=id)
    categoria = Categoria.objects.filter(id=id)
    marca = Marca.objects.filter(estado=1, id_categoria=id)

    if request.user.is_authenticated:
        filtroPedido = Pedido.objects.filter(
            estado=True, cliente=request.user.cliente.id, estadoc=0).count()
        print("El filtrado es : ", filtroPedido)
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(
            cliente=cliente, estado=False)
        items = pedido.pedidoespecifico_set.all()
        cartItems = pedido.get_cart_items
    else:
        return render(request, 'categoriaProductoSL/detalleProducto.html', {'producto': producto, 'categoria': categoria, 'marca': marca})
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = pedido['pedido.get_cart_items']

    return render(request, 'categoriaProducto/detalleProducto.html', {'producto': producto, 'categoria': categoria, 'marca': marca, 'cartItems': cartItems, 'filtroPedido': filtroPedido})


def cart(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(
            cliente=cliente, estado=False)
        items = pedido.pedidoespecifico_set.all()
        cartItems = pedido.get_cart_items
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = pedido['pedido.get_cart_items']

    context = {'items': items, 'pedido': pedido, 'cartItems': cartItems}
    return render(request, 'pedido/carrito.html', context)


def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        datos_cuenta = DatosCuenta.objects.all()
        pedidoComprobante = Pedido.objects.all()
        pedido, created = Pedido.objects.get_or_create(
            cliente=cliente, estado=False)
        items = pedido.pedidoespecifico_set.all()
        cartItems = pedido.get_cart_items
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = pedido['pedido.get_cart_items']

    context = {'items': items, 'pedido': pedido,
               'cartItems': cartItems, 'datos_cuenta': datos_cuenta, 'pedidoComprobante': pedidoComprobante}
    return render(request, 'pedido/verificar.html', context)


def updatePedidoEspecifico(request):

    if request.user.is_authenticated:
        filtroPedido = Pedido.objects.filter(
            estado=True, cliente=request.user.cliente.id, estadoc=0).count()
        print("El filtro es, ", filtroPedido)
        if filtroPedido == 0:
            data = json.loads(request.body)
            productId = data['productId']
            action = data['action']

            cliente = request.user.cliente
            producto = Producto.objects.get(id=productId)
            pedido, created = Pedido.objects.get_or_create(
                cliente=cliente, estado=False)

            pedidoespecifico, created = PedidoEspecifico.objects.get_or_create(
                pedido=pedido, producto=producto)

            if action == 'add':
                if producto.cantidad == 0:
                    messages.error(request, "No hay suficientes productos")
                else:
                    pedidoespecifico.cantidad = (pedidoespecifico.cantidad + 1)
                    producto.cantidad = (producto.cantidad - 1)
                    cursor = connection.cursor()
                    cursor.execute("Update producto_producto set cantidad='" +
                                   str(producto.cantidad) + "' where id="+str(producto.id))
                    messages.success(request, "Agregado")
            elif action == 'remove':
                pedidoespecifico.cantidad = (pedidoespecifico.cantidad - 1)
                producto.cantidad = (producto.cantidad + 1)
                cursor = connection.cursor()
                cursor.execute("Update producto_producto set cantidad='" +
                               str(producto.cantidad) + "' where id="+str(producto.id))
                messages.success(request, "Eliminado")

            pedidoespecifico.save()

            if pedidoespecifico.cantidad <= 0:
                pedidoespecifico.delete()

            print('Action: ', action)
            print('productId: ', productId)
            return JsonResponse("Agregado", safe=False)
        else:
            data = json.loads(request.body)
            productId = data['productId']
            action = data['action']

            if action == 'add':
                messages.success(
                    request, "Solo puede realizar un pedido a la vez, confirme su pedido")
            return JsonResponse("No se puede agregar", safe=False)
    else:
        messages.success(request, "No se encuentra logeado")


@csrf_protect
def pedidoProcesados(request):
    transaccion_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, created = Pedido.objects.get_or_create(
            cliente=cliente, estado=False)
        total = float(data['form']['total'])
        tipoEnvio = data['envio']['seleccion']
        pedido.transaccion_id = transaccion_id

        ciudadL = data['envio']['city']
        direccionL = data['envio']['address']

        if total == pedido.get_cart_total:
            pedido.estado = True
            pedido.tipo_envio = tipoEnvio
            pedido.totalPagar = total
        pedido.save()

        if pedido.estado == True:
            if ciudadL == "" or direccionL == "":
                MetodoEnvio.objects.create(
                    cliente=cliente,
                    pedido=pedido,
                    ciudad="Local",
                    direccion="Local",
                )

                messages.success(
                    request, "Pedido relizado correctamente retie su pedido en la siguiente dirreción ...")

            else:
                MetodoEnvio.objects.create(
                    cliente=cliente,
                    pedido=pedido,
                    ciudad=data['envio']['city'],
                    direccion=data['envio']['address'],
                )

                idA = data['form']['idA']
                cedula = data['form']['cedula']
                telefono = data['form']['telefono']

                cursor = connection.cursor()
                cursor.execute("Update cliente_cliente set cedula='"+str(cedula) +
                               "', telefono='"+str(telefono)+"' where id_cliente_id="+str(idA))
                messages.success(
                    request, "Pedido relizado correctamente por favor suba su comprobante con el deposito realizado...")

        # return render(request, 'base/base.html')

    else:
        print("Usuario no esta logeado")
    return JsonResponse("Pago completado", safe=False)


def prueba(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # detalle metodo de envio

            id_A = request.POST.get('id_A')
            city = request.POST.get('city')
            address = request.POST.get('address')
            imagen = request.FILES.get('imagenComprobante')

            # detalle usuario
            cedula = request.POST.get('cedula')
            telefono = request.POST.get('telefono')

            # pedido
            total = request.POST.get('totalPagar')

            print("El id es: ", id_A, "la ciudad es: ", city, "la dirrecion es: ", address, "la imagen es: ",
                  imagen, "la cedula es: ", cedula, "el telefono es: ", telefono, "y el total es: ", total)

            # return HttpResponse("Acceso Denegado Admin 1")

            transaccion_id = datetime.datetime.now().timestamp()
            cliente = request.user.cliente
            pedido, created = Pedido.objects.get_or_create(
                cliente=cliente, estado=False)
            totalF = float(total)
            pedido.transaccion_id = transaccion_id

            if total == pedido.get_cart_total:
                pedido.estado = True
                pedido.totalPagar = totalF
            pedido.save()

            if pedido.estado == True:
                try:
                    envio = MetodoEnvio.objects.create(
                        cliente="pepe",
                        pedido=59,
                        ciudad=city,
                        direccion=address
                    )
                    cursor = connection.cursor()
                    cursor.execute("Update cliente_cliente set cedula='"+str(cedula) +
                                   "', telefono='"+str(telefono)+"' where id_cliente_id="+str(id_A))
                except:
                    return HttpResponse(json.dumps("El nombre de usuario ya existe"), content_type="application/json")

            return render(request, 'base/base.html', contexto)

            messages.success(request, "Pedido relizado correctamente ...")

        else:
            print("Usuario no esta logeado")

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return HttpResponse("Acceso Denegado  4")
