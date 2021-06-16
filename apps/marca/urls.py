from django.urls import path
from apps.marca.views import index, update
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(index), name="Marca"),
    path('update/<int:id>/', login_required(update),  name="Marca_update"),
]
