#from django.contrib import admin
from django.urls import path
from apps.categoria.views import index, update, categoria_listar, indexlocal, updatelocal
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name="Categoria"),
    path('update/<int:id>/', login_required(update),  name="Categoria_update"),
    path('listar', login_required(indexlocal), name="Local_Categoria"),
    path('updatecategorial/<int:id>/', login_required(updatelocal),
         name="Local_Categoria_update"),
    path('views/', categoria_listar, name="CategoriaProducto"),

]
