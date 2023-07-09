from rest_framework import serializers
from app_registro.models import Persona
from .models import InformacionGeneral, OcupacionActual, ActividadTiempoLibre, FuenteIngresos, ConvivenciaVivienda, RedApoyo, FactorRiesgo, EncuentroDiaHora

 

# Serializers 

class FuenteIngresosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuenteIngresos
        fields = '__all__'

class OcupacionActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcupacionActual
        fields = '__all__' 

class ActividadTiempoLibreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ActividadTiempoLibre
        fields = "__all__"

class ConvivenciaViviendaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ConvivenciaVivienda
        fields = "__all__"
        
class RedApoyoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = RedApoyo
        fields = "__all__"
        
class FactorRiesgoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = FactorRiesgo
        fields = "__all__"

class EncuentroDiaHoraSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EncuentroDiaHora
        fields = "__all__"

#! Se utilizó esta clase para que excluya el campo id_informacion_general al momento de realizar la petición HTTP
class EncuentroDiaHoraGetSerializer(serializers.ModelSerializer): 
    class Meta:
        model = EncuentroDiaHora
        exclude = ['id_informacion_general']

# ListingField
class OcupacionActualListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_ocupacion_actual
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_ocupacion_actual'].strip()
        raise serializers.ValidationError('Invalid input format.')


class ActividadTiempoLibreListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'nombre_actividad_tiempo_libre': value.nombre_actividad_tiempo_libre,
            'observacion_actividad_tiempo_libre': value.observacion_actividad_tiempo_libre
        }

    def to_internal_value(self, data):
        if isinstance(data, dict):
            nombre_actividad = data.get('nombre_actividad_tiempo_libre', '').strip()
            observacion_actividad = data.get('observacion_actividad_tiempo_libre', '').strip()
            return {
                'nombre_actividad_tiempo_libre': nombre_actividad,
                'observacion_actividad_tiempo_libre': observacion_actividad
            }
        raise serializers.ValidationError('Invalid input format.')


# Serializer Informacion General
class InformacionGeneralSerializer(serializers.ModelSerializer):

    id_persona = serializers.CharField(max_length=30, required=True) 
    
    ocupaciones_actuales = OcupacionActualListingField(
        many=True,
        queryset=OcupacionActual.objects.all(),
        required=False,
    )
    
    actividades_tiempo_libre = ActividadTiempoLibreSerializer(many=True)
    fuentes_de_ingresos = FuenteIngresosSerializer(many=True)
    convivencias_en_vivienda = ConvivenciaViviendaSerializer(many=True)
    redes_de_apoyo = RedApoyoSerializer(many=True)
    factores_de_riesgo = FactorRiesgoSerializer(many=True)
    encuentro_dias_horas = EncuentroDiaHoraGetSerializer(many=True)
    
    class Meta:
        model = InformacionGeneral
        fields = '__all__'
    
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona',[])
        
        ocupaciones_actuales = validated_data.pop('ocupaciones_actuales',[])
        actividades_tiempo_libre = validated_data.pop('actividades_tiempo_libre',[])
        fuentes_de_ingresos = validated_data.pop('fuentes_de_ingresos',[])
        convivencias_en_vivienda = validated_data.pop('convivencias_en_vivienda',[])
        redes_de_apoyo = validated_data.pop('redes_de_apoyo',[])
        factores_de_riesgo = validated_data.pop('factores_de_riesgo',[])
        encuentro_dias_horas = validated_data.pop('encuentro_dias_horas',[])
        
        persona = Persona.objects.get(numero_documento=id_persona)
        
        informacion_general = InformacionGeneral.objects.create(id_persona=persona, **validated_data)
        
         # OcupacionActual
        for nombre_ocupacion_actual in ocupaciones_actuales:
            ocupacion_actual, _ = OcupacionActual.objects.get_or_create(nombre_ocupacion_actual=nombre_ocupacion_actual)
            informacion_general.ocupaciones_actuales.add(ocupacion_actual)
         
        # ActividadTiempoLibre    
        for actividad_tiempo_libre_data in actividades_tiempo_libre: 
            ActividadTiempoLibre.objects.create(id_informacion_general=informacion_general,**actividad_tiempo_libre_data)
        
        # FuenteIngresos
        for fuente_ingreso_data in fuentes_de_ingresos:
            FuenteIngresos.objects.create(id_informacion_general=informacion_general, **fuente_ingreso_data)
            
        # ConvivenciaVivienda
        for convivencia_vivienda_data in convivencias_en_vivienda:
            ConvivenciaVivienda.objects.create(id_informacion_general=informacion_general, **convivencia_vivienda_data)
        
        # RedApoyo
        for red_apoyo_data in redes_de_apoyo:
            RedApoyo.objects.create(id_informacion_general=informacion_general, **red_apoyo_data)
            
        # FactorRiesgo
        for factor_riesgo_data in factores_de_riesgo:
            FactorRiesgo.objects.create(id_informacion_general=informacion_general, **factor_riesgo_data)
            
        # EncuentroDiaHora
        for encuentro_dia_hora_data in encuentro_dias_horas:
            # EncuentroDiaHora.objects.create(id_informacion_general=informacion_general, **encuentro_dia_hora_data)
            # encuentro_dia_hora = EncuentroDiaHora.objects.get_or_create(**encuentro_dia_hora_data)
            # informacion_general.encuentro_dias_horas.add(encuentro_dia_hora)
            encuentro_dia_hora = EncuentroDiaHora.objects.filter(**encuentro_dia_hora_data).first()
            if not encuentro_dia_hora:
                encuentro_dia_hora = EncuentroDiaHora.objects.create(**encuentro_dia_hora_data)
            informacion_general.encuentro_dias_horas.add(encuentro_dia_hora)
         
        return informacion_general