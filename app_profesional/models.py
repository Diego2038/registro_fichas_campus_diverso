from django.db import models

# Create your models here.

from app_registro.models import Persona

class Profesional(models.Model):
    id_profesional = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    def __str__(self):
        return f"Profesional {self.id_profesional} - {self.nombre}"
