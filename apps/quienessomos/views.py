from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from apps.cliente.models import Cliente


def index(request):
    clientes = Cliente.objects.raw(
        "select u.id, u.username, u.first_name, u.last_name, email, u.is_active, c.tipo_usuario, c.id_cliente_id from cliente_cliente as c inner join auth_user as u on u.id=c.id_cliente_id where u.id=" +
        str(request.user.id)
    )
    contexto = {'clientes': clientes}
    return render(request, 'quienesSomos/index.html', contexto)
