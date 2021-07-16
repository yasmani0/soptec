#from django.contrib import admin
from django.urls import path
from apps.local.views import index, update_cuenta_local, localadmuser, local_usuario_register_adm, local_usuario_actualizar_adm

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name="LocalAdmin"),
    path('local/update/', login_required(update_cuenta_local),
         name="Cuenta_update_local"),
    path('users', login_required(localadmuser), name="LocalUsers"),
    path('users/registeradml', login_required(local_usuario_register_adm),
         name="LocalUserRegisterAdm"),
    path('users/actualizaradm',
         login_required(local_usuario_actualizar_adm), name="LocalUserUpdateAdm"),
]
