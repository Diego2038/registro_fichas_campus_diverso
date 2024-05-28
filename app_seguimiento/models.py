from django.db import models

# Create your models here.
from app_registro.models import Persona
from app_profesional.models import Profesional

class Seguimiento(models.Model):
    id_seguimiento = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=False, null=False, related_name="seguimientos")
    id_profesional = models.ForeignKey(Profesional, on_delete=models.DO_NOTHING, blank=False, null=False)
    fecha = models.DateField()
    observacion = models.TextField(blank=False, null=False)
    
    class Meta:
        db_table = "Seguimiento"
    
    def __str__(self):
        return f"DocumentosAutorizacion {self.id_seguimiento}"
