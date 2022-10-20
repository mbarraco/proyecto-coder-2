from django.db import models

from django.contrib.auth.models import User


class Mensaje(models.Model):
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=100)



class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Blog(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre