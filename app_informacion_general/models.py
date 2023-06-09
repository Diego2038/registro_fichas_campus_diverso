from django.db import models

# Create your models here. 
from app_registro.models import Persona


class OcupacionActual(models.Model):
    id_ocupacion_actual = models.AutoField(primary_key=True)
    nombre_ocupacion_actual = models.CharField(max_length=200)
    
    
class ActividadTiempoLibre(models.Model):
    id_actividad_tiempo_libre = models.AutoField(primary_key=True)
    nombre_actividad_tiempo_libre = models.CharField(max_length=200)
    observacion_actividad_tiempo_libre = models.TextField(blank=True, null=False, default="Sin observación")
    id_informacion_general = models.ForeignKey('InformacionGeneral', on_delete=models.CASCADE, related_name="actividades_tiempo_libre", blank=True, null=True)
 
 
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
    observacion_general_redes_de_apoyo = models.TextField()
    observacion_general_factores_de_riesgo = models.TextField()
    creencia_religiosa = models.TextField()
    encuentro_inicial = models.CharField(max_length=30)
    observacion_horario = models.TextField()
    origen_descubrimiento_campus_diverso = models.CharField(max_length=300)
    comentarios_o_sugerencias_de_usuario = models.TextField()
    ocupaciones_actuales = models.ManyToManyField(OcupacionActual, max_length=200, related_name="informaciones_generales") 

    class Meta:
        db_table = "Informacion_general"
    
    def __str__(self):
        return f"InformacionGeneral {self.id_informacion_general}"
   
    
    
# class FuenteIngresos(models.Model):
#     id_fuente_ingresos = models.AutoField(primary_key=True)
#     nombre_fuente_ingresos = models.CharField(max_length=200)
#     observacion_fuente_ingresos = models.TextField(blank=True, null=True)
#     id_informacion_general = models.ForeignKey(InformacionGeneral, on_delete=models.CASCADE)

# class ConvivenciaVivienda(models.Model):
#     id_convivencia_vivienda = models.AutoField(primary_key=True)
#     nombre_convivencia_vivienda = models.CharField(max_length=200)
#     observacion_convivencia_vivienda = models.TextField(blank=True, null=True)
#     id_informacion_general = models.ForeignKey(InformacionGeneral, on_delete=models.CASCADE)

# class RedApoyo(models.Model):
#     id_red_apoyo = models.AutoField(primary_key=True)
#     nombre_red_apoyo = models.CharField(max_length=200)
#     observacion_red_apoyo = models.TextField(blank=True, null=True)
#     id_informacion_general = models.ForeignKey(InformacionGeneral, on_delete=models.CASCADE) 
    
# class FactorRiesgo(models.Model):
#     id_factor_riesgo = models.AutoField(primary_key=True)
#     nombre_factor_riesgo = models.CharField(max_length=200)
#     observacion_factor_riesgo = models.TextField(blank=True, null=True)
    
#     id_informacion_general = models.ForeignKey(InformacionGeneral, on_delete=models.CASCADE)

