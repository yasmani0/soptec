#from django.contrib import admin
from django.urls import path
from apps.asistentelocal.views import index, update_cuenta_local_asistente, local_asistente_admuser, local_asistente_usuario_register_adm, local_asistente_usuario_actualizar_adm

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index, name="AsistenteLocal"),
    path('local/update/', login_required(update_cuenta_local_asistente),
         name="Cuenta_update_local_asistente"),
    path('users', login_required(local_asistente_admuser),
         name="Local_Asistente_Users"),
    path('users/registeradm', login_required(local_asistente_usuario_register_adm),
         name="LocalAsistenteUserRegisterAdm"),
    path('users/actualizaradm',
         login_required(local_asistente_usuario_actualizar_adm), name="LocalAsistenteUserUpdateAdm"),
]
