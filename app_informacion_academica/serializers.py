from rest_framework import serializers
from app_registro.models import Persona
from .models import InformacionAcademica, Estamento

class EstamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estamento
        fields = '__all__'

class EstamentoListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_estamento
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_estamento'].strip()
        raise serializers.ValidationError('Invalid input format.')

class InformacionAcademicaSerializer(serializers.ModelSerializer):

    id_persona = serializers.CharField(max_length=30, required=True)
    estamentos = EstamentoListingField(
        many=True,
        queryset= Estamento.objects.all(),
        required=False,
    )
    
    class Meta:
        model = InformacionAcademica
        fields = '__all__'
    
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
        
        estamentos = validated_data.pop('estamentos',[])
        
        persona = Persona.objects.get(numero_documento=id_persona)
        
        informacion_academica = InformacionAcademica.objects.create(id_persona=persona, **validated_data)
        
        for nombre_estamento in estamentos:
            estamento,_ = Estamento.objects.get_or_create(nombre_estamento=nombre_estamento)
            informacion_academica.estamentos.add(estamento)
        
        return informacion_academica
        
    
    
      
