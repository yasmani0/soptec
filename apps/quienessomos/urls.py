from django.urls import path
from apps.quienessomos.views import index

urlpatterns = [
    path('', index, name="QuienesSomos"),
]
