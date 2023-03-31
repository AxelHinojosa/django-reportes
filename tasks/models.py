from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    Titulo = models.CharField(max_length=100)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Completado = models.DateTimeField(null=True, blank=True)
    Creado = models.DateTimeField(auto_now_add=True)
    Recepcion = models.BooleanField(default=True)
    Generacion = models.BooleanField(default=True)
    Entregado = models.BooleanField(default=True)

    def __str__(self):
        return self.Titulo + '- de ' + self.Usuario.username