from django.db import models
from app_registro.models import Persona

# Create your models here.

class InformacionAcademica(models.Model):
    id_informacion_academica = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False)
    pertenencia_univalle = models.BooleanField()
    sede_universidad = models.CharField(max_length=20)
    nombre_programa_academico = models.CharField(max_length=100)
    codigo_estudiante = models.CharField(max_length=20, unique=True)
    semestre_academico = models.IntegerField()
    
    
  