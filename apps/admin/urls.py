#from django.contrib import admin
from django.urls import path
from apps.admin.views import index, admuser, usuario_register_adm, usuario_actualizar_adm, perfil_actualizar_adm, update
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name="Admin"),
    path('users', login_required(admuser), name="Users"),
    path('users/registeradm', login_required(usuario_register_adm), name="UserRegisterAdm"),
    path('users/actualizaradm', login_required(usuario_actualizar_adm), name="UserUpdateAdm"),
    path('users/perfiladm', login_required(perfil_actualizar_adm), name="PerfilAdm"),
    path('users/update/', login_required(update),  name="Cuenta_update"),

]
