from django.db import models

# Create your models here. 
from app_registro.models import Persona

class InformacionGeneral(models.Model):
    id_informacion_general = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False)
    dedicacion_externa = models.CharField(max_length=100)
    tipo_acompanamiento_recibido = models.CharField(max_length=70)
    observacion_tipo_acompanamiento_recibido = models.TextField()
    tipo_entidad_acompanamiento_recibido = models.TextField()
    tipo_profesional_acompanamiento_recibido = models.TextField()
    calificacion_acompanamiento_recibido = models.IntegerField(null=True)
    motivo_calificacion_acompanamiento = models.TextField(null=True)
    actividades_especificas_tiempo_libre = models.TextField()
    observacion_general_actividades_especificas_tiempo_libre = models.TextField()
    observacion_general_fuente_de_ingresos = models.TextField()
    observacion_general_relacion_familiar = models.TextField()
    relacion_familiar = models.IntegerField()
    nombre_persona_confianza = models.TextField()
    telefono_persona_confianza = models.TextField()
    observacion_general_redes_de_apoyo = models.TextField()
    observacion_general_factores_de_riesgo = models.TextField()
    creencia_religiosa = models.TextField()
    encuentro_inicial = models.CharField(max_length=30)
    observacion_horario = models.TextField()
    origen_descubrimiento_campus_diverso = models.CharField(max_length=300)
    comentarios_o_sugerencias_de_usuario = models.TextField() 

    class Meta:
        db_table = "Informacion_general"
    
    def __str__(self):
        return f"InformacionGeneral {self.id_informacion_general}"
