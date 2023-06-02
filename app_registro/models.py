from django.db import models

# Create your models here. 

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    incluir_correo_en_respuesta = models.BooleanField(default=False)
    nombre_identitario = models.CharField(max_length=150)
    nombre_y_apellido = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=30, unique=True)
    fecha_nacimiento = models.DateField()
    estrato_socioeconomico = models.IntegerField()
    municipio_nacimiento = models.CharField(max_length=50)
    departamento_nacimiento = models.CharField(max_length=50)
    pais_nacimiento = models.CharField(max_length=50)
    municipio_residencia = models.CharField(max_length=100)
    zona_residencial = models.CharField(max_length=100)
    direccion_residencia = models.CharField(max_length=200)
    barrio_residencia = models.CharField(max_length=150)
    comuna_barrio = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    estado_civil = models.CharField(max_length=30)
    identidad_etnico_racial = models.CharField(max_length=70)

    class Meta:
        db_table = "Persona"

class PertenenciaGrupoPoblacional(models.Model):
    id_grupo_poblacional = models.AutoField(primary_key=True)
    nombre_grupo_poblacional = models.CharField(max_length=300)
    personas = models.ManyToManyField(Persona, blank=True)

    class Meta:
        db_table = "Pertenencia_grupo_poblacional"
