from django.db import models

# Create your models here.
from app_registro.models import Persona

class DiversidadSexual(models.Model):
    id_diversidad_sexual = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False)
    # id_persona = models.CharField(max_length=30, null=False, unique=True) 
    cambio_nombre_sexo_documento = models.CharField(max_length=50)
    recibir_orientacion_cambio_en_documento = models.BooleanField()

    class Meta:
        db_table = "Diversidad_sexual"