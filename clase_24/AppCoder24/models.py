from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    fecha_de_inicio = models.DateField(null=True)

    def __str__(self):
        return f"({self.camada}) {self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

