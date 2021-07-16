from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from apps.cliente.models import Cliente


def send_email(mail, nombre, asunto, mensaje):
    context = {'mail': mail, 'nombre': nombre,
               'asunto': asunto, 'mensaje': mensaje}
    template = get_template('contactanos/email.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Mensaje de Soptec PC',
        'Mensaje enviando ',
        settings.EMAIL_HOST_USER,
        ['karlaeve1720@outlook.com']
    )

    email.attach_alternative(content, 'text/html')
    email.send()


def index(request):
    clientes = Cliente.objects.raw(
        "select u.id, u.username, u.first_name, u.last_name, email, u.is_active, c.tipo_usuario, c.id_cliente_id from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id where u.id=" +
        str(request.user.id)
    )
    contexto = {'clientes': clientes}

    if request.method == 'POST':
        nombre = request.POST.get('nombre_info')
        mail = request.POST.get('email_info')
        asunto = request.POST.get('asunto_info')
        mensaje = request.POST.get('message')
        send_email(mail, nombre, asunto, mensaje)
        messages.success(
            request, "Tu mensaje se envio correctamente, en poco tiempo recibiras tu respuesta")
    return render(request, 'contactanos/index.html', contexto)
