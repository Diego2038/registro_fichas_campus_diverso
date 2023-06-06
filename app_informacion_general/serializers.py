from rest_framework import serializers
from app_registro.models import Persona
from .models import InformacionGeneral 

 
class InformacionGeneralSerializer(serializers.ModelSerializer):

    id_persona = serializers.CharField(max_length=30, required=True) 
    
    class Meta:
        model = InformacionGeneral
        fields = '__all__'
    
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
          
        persona = Persona.objects.get(numero_documento=id_persona)
        
        informacion_academica = InformacionGeneral.objects.create(id_persona=persona, **validated_data)
         
        return informacion_academica