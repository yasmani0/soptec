"""soporte_pc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# para agregrar archivos medias importamos las dos de abajo
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView,  PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.inicio.urls'), name='Inicio'),
    path('SPCAdmin/', include('apps.admin.urls'), name='Admin'),
    path('categoria/', include('apps.categoria.urls'), name='Categoria'),
    path('usuario/', include('apps.usuario.urls'), name='Usuario'),
    path('producto/', include('apps.producto.urls'), name='Producto'),
    path('marca/', include('apps.marca.urls'), name='Marca'),
    path('servicios/', include('apps.servicios.urls'), name='Servicios'),
    path('contactanos/', include('apps.contactanos.urls'), name='Contactanos'),
    path('quienesSomos/', include('apps.quienessomos.urls'), name='QuienesSomos'),
    path('pedidos/', include('apps.pedido.urls'), name='Pedidos'),
    path('comprobante/', include('apps.comprobante.urls'), name='Comprobante'),
    # REESTABLECIMIENTO DE CONTRASEÑA, es importante los nombres de las vistas
    path('reset/password_reset', PasswordResetView.as_view(template_name='restablecer/password_reset_form.html',
         email_template_name="registration/password_reset_email.html"), name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(
        template_name='restablecer/password_reset_done.html'), name='password_reset_done'),
    # colocamos el token del parametro
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(
        template_name='restablecer/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(
        template_name='restablecer/password_reset_complete.html'), name='password_reset_complete')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
