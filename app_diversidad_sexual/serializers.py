from rest_framework import serializers
from .models import DiversidadSexual, Pronombre
from app_registro.models import Persona


class PronombreSerializer(serializers.ModelSerializer):
    nombre_pronombre = serializers.CharField(max_length=50, required=True)
    
    class Meta:
        model = Pronombre
        fields = '__all__'

class PronombreListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_pronombre
    
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_pronombre'].strip()
        raise serializers.ValidationError('Invalid input format.')

class DiversidadSexualSerializer(serializers.ModelSerializer):
    id_persona = serializers.CharField(max_length=30, required=True)
    
    pronombres = PronombreListingField(
        many=True,
        queryset=Pronombre.objects.all(),
        required=False,
    )
    
     
    class Meta:
        model = DiversidadSexual
        fields = '__all__'
    
    def create(self, validated_data):
        # Persona
        id_persona = validated_data.pop('id_persona')
        persona = Persona.objects.get(numero_documento=id_persona) #! Así son más fáciles las consultas
        
        # Creación del objeto DiversidadSexual
        diversidad_sexual = DiversidadSexual.objects.create(id_persona=persona, **validated_data)
        
        # Pronombre
        pronombres = validated_data.pop('pronombres', [])
        for pronombre in pronombres:
            pronombres = Pronombre.objects.get_or_create(nombre_pronombre=pronombre)
            diversidad_sexual.pronombres.add(pronombres)

        return diversidad_sexual 