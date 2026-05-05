from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='card_image/', null=True, blank=True)


class Alumno(models.Model):
    persona=models.OneToOneField(Persona, on_delete=models.CASCADE)
    nro_alumno = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)
