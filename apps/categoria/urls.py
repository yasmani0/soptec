#from django.contrib import admin
from django.urls import path
from apps.categoria.views import index, update, categoria_listar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name="Categoria"),
    path('views/', categoria_listar, name="CategoriaProducto"),
    path('update/<int:id>/', login_required(update),  name="Categoria_update"),

]
