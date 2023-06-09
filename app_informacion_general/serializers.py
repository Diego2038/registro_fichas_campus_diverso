from rest_framework import serializers
from app_registro.models import Persona
from .models import InformacionGeneral, OcupacionActual, ActividadTiempoLibre, FuenteIngresos, ConvivenciaVivienda, RedApoyo

 

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
         
        return informacion_general