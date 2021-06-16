from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Cliente(models.Model):
    id_cliente = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    cedula = models.CharField(
        max_length=10, blank=True, unique=True, null=True)

    def __str__(self):
        return '{}'.format(self.id_cliente)
