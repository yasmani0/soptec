from django.urls import path
from apps.comprobante.views import index, generarComprobante
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(index), name="Comprobante"),
    path('generar/<pk>', login_required(generarComprobante.as_view()),
         name="Comprobante_generado"),
]
