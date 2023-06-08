from rest_framework import serializers
from .models import Persona, PertenenciaGrupoPoblacional
from app_diversidad_sexual.serializers import DiversidadSexualSerializer
from app_diversidad_sexual.models import DiversidadSexual

class PertenenciaGrupoPoblacionalSerializer(serializers.ModelSerializer):
    nombre_grupo_poblacional = serializers.CharField(max_length=300, required=True)
    class Meta:
        model = PertenenciaGrupoPoblacional
        fields = '__all__'

class PertenenciaGrupoPoblacionalListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_grupo_poblacional
    
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict) and 'nombre_grupo_poblacional' in data:
            return data['nombre_grupo_poblacional'].strip()
        raise serializers.ValidationError('Invalid input format.')
    
    

class PersonaSerializer(serializers.ModelSerializer):
    
    ciudad_nacimiento = serializers.CharField(max_length=100, default="Ciudad no especificada", required=False)
    municipio_nacimiento = serializers.CharField(max_length=100, default="Municipio no especificado", required=False)
    corregimiento_nacimiento = serializers.CharField(max_length=100, default="Corregimiento no especificado", required=False)
    ciudad_residencia = serializers.CharField(max_length=100, default="Ciudad no especificada", required=False)
    municipio_residencia = serializers.CharField(max_length=100, default="Municipio no especificado", required=False)
    corregimiento_residencia = serializers.CharField(max_length=100, default="Corregimiento no especificado", required=False)
    
    pertenencia_grupo_poblacional = PertenenciaGrupoPoblacionalListingField(
        many=True, 
        queryset=PertenenciaGrupoPoblacional.objects.all(),
        required=False, 
        )
    # pertenencia_grupo_poblacional = PertenenciaGrupoPoblacionalSerializer(many=True, required=False)
    # pertenencia_grupo_poblacional = serializers.ListField(
    #     child=serializers.CharField(max_length=300),
    #     write_only=True #! Sin este campo aparecen errores
    # ) 
   
    diversidad_sexual = serializers.SerializerMethodField()
    def get_diversidad_sexual(self, obj):
        try:
            diversidad_sexual_instance = DiversidadSexual.objects.get(id_persona_id=obj.id_persona)
            serializer = DiversidadSexualSerializer(diversidad_sexual_instance)  
            return serializer.data
        except DiversidadSexual.DoesNotExist:
            return []
        
    
    class Meta:
        model = Persona
        fields = '__all__'
   

    def create(self, validated_data):
        
        pertenencia_grupo_poblacional_names = validated_data.pop('pertenencia_grupo_poblacional',[]) 
        persona = Persona.objects.create(**validated_data) 
        print(pertenencia_grupo_poblacional_names)
        
        for pertenencia_grupo_poblacional_name in pertenencia_grupo_poblacional_names:  
            try: 
                pertenencia_grupo_poblacional = PertenenciaGrupoPoblacional.objects.get (nombre_grupo_poblacional=pertenencia_grupo_poblacional_name.strip()) 
            except PertenenciaGrupoPoblacional.DoesNotExist: 
                pertenencia_grupo_poblacional = PertenenciaGrupoPoblacional.objects.create(nombre_grupo_poblacional=pertenencia_grupo_poblacional_name.strip())    
            persona.pertenencia_grupo_poblacional.add(pertenencia_grupo_poblacional)
         
        return persona
        
    
