from rest_framework import serializers
from .models import Seguimiento
from app_registro.models import Persona 

class SeguimientoSerializer(serializers.ModelSerializer):
    id_persona = serializers.CharField(max_length=30, required=True)
    
    class Meta:
        model = Seguimiento
        fields = '__all__'
        
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
        
        persona = Persona.objects.get(numero_documento=id_persona)
        seguimiento = Seguimiento.objects.create(id_persona=persona, **validated_data)
        return seguimiento