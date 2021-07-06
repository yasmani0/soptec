from django.urls import path
from apps.servicios.views import index

urlpatterns = [
    path('', index, name="Servicios"),
]
