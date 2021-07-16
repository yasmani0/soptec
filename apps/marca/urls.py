from django.urls import path
from apps.marca.views import index, update, localindex, localupdate, local_asistentes_index, local_asistentes_update
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name="Marca"),
    path('update/<int:id>/', login_required(update),  name="Marca_update"),
    path('listar', login_required(localindex), name="Local_Marca"),
    path('listar/update/<int:id>/',
         login_required(localupdate),  name="Local_Marca_update"),
    path('mostrar', login_required(local_asistentes_index),
         name="local_asistentes_index"),
    path('mostrar/update/<int:id>/',
         login_required(local_asistentes_update),  name="Local_Asistentes_Marca_update"),
]
