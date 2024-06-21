from rest_framework import serializers
from .models import Seguimiento
from app_registro.models import Persona 
from app_profesional.models import UserProfesional

class SeguimientoSerializer(serializers.ModelSerializer):
    id_persona = serializers.CharField(max_length=30, required=True)
    
    class Meta:
        model = Seguimiento
        fields = '__all__'
        
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
        id_profesionales = validated_data.pop('profesionales')
        #! TODO: Fix, Por ahora sólo guarda id's enteros
        persona = Persona.objects.get(numero_documento=id_persona)
        seguimiento = Seguimiento.objects.create(id_persona=persona, **validated_data)
        for id in id_profesionales:
            # profesional = UserProfesional.objects.get(id=id)
            seguimiento.profesionales.add(id)

        return seguimiento