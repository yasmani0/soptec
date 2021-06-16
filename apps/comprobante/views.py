from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from apps.datoscuenta.models import DatosCuenta
from apps.comprobante.models import Comprobante
from apps.comprobante.forms import ComprobanteForm
from django.contrib.auth.models import User
from apps.cliente.models import Cliente
from apps.pedido.models import Pedido, MetodoEnvio, PedidoEspecifico
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import connection
import datetime
import json
# libreria comprobante
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


def index(request):

    if request.user.is_authenticated:
        datos_cuenta = DatosCuenta.objects.all()

        pedidoRetiro = Pedido.objects.filter(
            estado=True, cliente=request.user.cliente.id, tipo_envio=1, estadoc=0)
        filtroPedidoRetiro = Pedido.objects.filter(
            estado=True, cliente=request.user.cliente.id, tipo_envio=1, estadoc=0).count()

        pedidoEnvio = Pedido.objects.filter(
            estado=True, cliente=request.user.cliente.id, tipo_envio=2, estadoc=0)
        filtroPedidoEnvio = Pedido.objects.filter(
            estado=True, cliente=request.user.cliente.id, tipo_envio=2, estadoc=0).count()
        cliente = request.user.cliente

        if request.method == 'POST':
            nombre = datetime.datetime.now().timestamp()

            comp = Comprobante()
            comp.nombre = nombre
            comp.estado = 0
            comp.imagen = request.FILES.get('imagenComprobante')
            comp.id_cliente = Cliente.objects.get(
                id_cliente=request.POST.get('id_cliente'))
            comp.id_pedido = Pedido.objects.get(
                id=request.POST.get('id_pedido'))

            estado = 1
            idP = request.POST.get('id_pedido')
            comp.save()
            cursor = connection.cursor()
            cursor.execute("Update pedido_pedido set estadoc='" +
                           str(estado) + "' where id="+str(idP))

            messages.success(
                request, "Pedido realizado correctamente mira tus pedidos, Gracias por su compra ...")

            return render(request, 'base/base.html')
        else:

            contexto = {'datos_cuenta': datos_cuenta,
                        'pedidoRetiro': pedidoRetiro, 'filtroPedidoRetiro': filtroPedidoRetiro, 'pedidoEnvio': pedidoEnvio, 'filtroPedidoEnvio': filtroPedidoEnvio}
            return render(request, 'comprobante/index.html', contexto)
    else:
        print("Usuario no esta logeado")
        contexto = {'datos_cuenta': datos_cuenta, 'pedidoRetiro': pedidoRetiro,
                    'filtroPedidoRetiro': filtroPedidoRetiro, 'pedidoEnvio': pedidoEnvio, 'filtroPedidoEnvio': filtroPedidoEnvio}
        return render(request, 'comprobante/index.html', contexto)


class generarComprobante(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):

        try:
            template = get_template('comprobante/generar.html')
            idDetalle = Pedido.objects.get(pk=self.kwargs['pk'])

            cliente = User.objects.raw(
                'select u.id, u.first_name  , u.last_name , cl.telefono, cl.cedula, pe.estado from auth_user as u inner join cliente_cliente as cl on cl.id_cliente_id = u.id inner join pedido_pedido as pe on pe.cliente_id=cl.id where pe.id='+str(idDetalle))

            totales = Pedido.objects.raw(
                'SELECT p.id, p."totalPagar", p."totalPagar" * 0.12 as iva, p."totalPagar" + (p."totalPagar" * 0.12) as totaf FROM public.pedido_pedido as p where id='+str(idDetalle))

            productos = PedidoEspecifico.objects.raw(
                'select proe.id, proe.cantidad, proe.pedido_id, proe.producto_id, pro.nombre, pro.precio, pro.imagen, proe.cantidad * pro.precio as subtotal from pedido_pedidoespecifico as proe inner join producto_producto as pro on proe.producto_id=pro.id where proe.pedido_id='+str(idDetalle))

            context = {
                'sale': Pedido.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'Soptec PC', 'address': 'Ecuador - Sangolqui'},
                'detalle': productos,
                'total': totales,
                'usuario': cliente,
                'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.jpeg'),
            }

            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'

            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response, link_callback=self.link_callback)
            # if error then show some funy view
            if pisa_status.err:
                return HttpResponseRedirect(reverse_lazy('Mis_Pedidos'))
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('Mis_Pedidos'))
