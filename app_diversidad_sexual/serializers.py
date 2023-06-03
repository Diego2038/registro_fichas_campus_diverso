from rest_framework import serializers
from .models import DiversidadSexual
from app_registro.models import Persona

class DiversidadSexualSerializer(serializers.ModelSerializer):
    id_persona = serializers.CharField(max_length=30, required=True)
    # id_persona = serializers.CharField(source='id_persona.numero_documento')
    
    class Meta:
        model = DiversidadSexual
        fields = '__all__'
    
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
        persona = Persona.objects.get(numero_documento=id_persona) #! Así son más fáciles las consultas

        diversidad_sexual = DiversidadSexual.objects.create(id_persona=persona, **validated_data)
        return diversidad_sexual 