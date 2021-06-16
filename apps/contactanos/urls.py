from django.urls import path
from apps.contactanos.views import index

urlpatterns = [
    path('', index, name="Contactanos"),
]
