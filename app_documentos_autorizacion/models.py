from django.db import models

# Create your models here.
from django.db import models
from app_registro.models import Persona

class DocumentosAutorizacion(models.Model):
    id_documentos_autorizacion = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False, related_name="documentos_autorizacion")
    autorizacion_manejo_de_datos = models.BooleanField()
    firma_consentimiento_informado = models.BooleanField()
    firma_terapia_hormonal = models.BooleanField(null=True, blank=True)
    documento_digital_y_archivo = models.BooleanField(null=True, blank=True)
    apgar_familiar = models.IntegerField()
    ecomapa = models.BooleanField(null=True, blank=True)
    arbol_familiar = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = "DocumentosAutorizacion"

    def __str__(self):
        return f"DocumentosAutorizacion {self.id_documentos_autorizacion}"

