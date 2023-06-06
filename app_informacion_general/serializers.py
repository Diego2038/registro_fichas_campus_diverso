from rest_framework import serializers
from app_registro.models import Persona
from .models import InformacionGeneral, OcupacionActual 

 


class OcupacionActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcupacionActual
        fields = '__all__' 

class OcupacionActualListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_ocupacion_actual
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_ocupacion_actual'].strip()
        raise serializers.ValidationError('Invalid input format.')

class InformacionGeneralSerializer(serializers.ModelSerializer):

    id_persona = serializers.CharField(max_length=30, required=True) 
    
    ocupaciones_actuales = OcupacionActualListingField(
        many=True,
        queryset=OcupacionActual.objects.all(),
        required=False,
    )

    
    class Meta:
        model = InformacionGeneral
        fields = '__all__'
    
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona',[])
        
        ocupaciones_actuales = validated_data.pop('ocupaciones_actuales',[])
        
        persona = Persona.objects.get(numero_documento=id_persona)
        
        informacion_academica = InformacionGeneral.objects.create(id_persona=persona, **validated_data)
        
         # OcupacionActual
        for nombre_ocupacion_actual in ocupaciones_actuales:
            ocupacion_actual, _ = OcupacionActual.objects.get_or_create(nombre_ocupacion_actual=nombre_ocupacion_actual)
            informacion_academica.ocupaciones_actuales.add(ocupacion_actual) 
         
        return informacion_academica