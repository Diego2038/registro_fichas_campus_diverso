from rest_framework import serializers
from .models import Persona, PertenenciaGrupoPoblacional


class PertenenciaGrupoPoblacionalSerializer(serializers.ModelSerializer):
    nombre_grupo_poblacional = serializers.CharField(max_length=300, required=True)
    class Meta:
        model = PertenenciaGrupoPoblacional
        fields = '__all__'



class PersonaSerializer(serializers.ModelSerializer):
    # pertenencia_grupo_poblacional = PertenenciaGrupoPoblacionalSerializer(many=True, required=True)
    pertenencia_grupo_poblacional = serializers.ListField(
        child=serializers.CharField(max_length=300),
        write_only=True #! Sin este campo aparecen errores
    ) 
    
    class Meta:
        model = Persona
        fields = '__all__'
  

    def create(self, validated_data):
        
        pertenencia_grupo_poblacional_names = validated_data.pop('pertenencia_grupo_poblacional',[]) 
        persona = Persona.objects.create(**validated_data) 
        print(pertenencia_grupo_poblacional_names)
        
        for pertenencia_grupo_poblacional_name in pertenencia_grupo_poblacional_names: 
            try: 
                pertenencia_grupo_poblacional = PertenenciaGrupoPoblacional.objects.get(nombre_grupo_poblacional=pertenencia_grupo_poblacional_name.strip()) 
            except PertenenciaGrupoPoblacional.DoesNotExist as e:
                pertenencia_grupo_poblacional = PertenenciaGrupoPoblacional.objects.create(nombre_grupo_poblacional=pertenencia_grupo_poblacional_name.strip())    
            pertenencia_grupo_poblacional.personas.add(persona) 
        
        return persona
        
    
