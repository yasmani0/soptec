from django.urls import path
from apps.usuario.views import usuario_login, usuario_register, usuario_perfil, salir

urlpatterns = [
    path('Usuarios/Login', usuario_login, name="usuario_login"), 
    path('Usuarios/Register', usuario_register, name="usuario_register"), 
    path('Usuarios/Perfil', usuario_perfil, name="usuario_perfil"), 
    path('Usuarios/Salir', salir, name="usuario_salir"), 
    
]

