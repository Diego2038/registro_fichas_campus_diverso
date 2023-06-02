from rest_framework import serializers
from .models import Persona, PertenenciaGrupoPoblacional



class PertenenciaGrupoPoblacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PertenenciaGrupoPoblacional
        fields = '__all__'



class PersonaSerializer(serializers.ModelSerializer):
    pertenencia_grupo_poblacional = PertenenciaGrupoPoblacionalSerializer(many=True, required=True)
    # pertenencia_grupo_poblacional = serializers.SerializerMethodField()

    class Meta:
        model = Persona
        fields = '__all__'

    # def get_pertenencia_grupo_poblacional(self, obj):
    #     from .serializers import PertenenciaGrupoPoblacionalSerializer
    #     # pertenencias = obj.pertenencia_grupo_poblacional.all()
    #     # serializer = PertenenciaGrupoPoblacionalSerializer(pertenencias)
    #     # return serializer.data
    #     if hasattr(obj, 'pertenencia_grupo_poblacional'):
    #         pertenencias = obj.pertenencia_grupo_poblacional.all()
    #     else:
    #         pertenencias = []

    #     serializer = PertenenciaGrupoPoblacionalSerializer(pertenencias, many=True, required=False)
    #     return serializer.data
    
    def create(self, validated_data):
        pertenencia_grupo_poblacional_ids = validated_data.pop('pertenencia_grupo_poblacional', [])
        persona = Persona.objects.create(**validated_data)
        
        for pertenencia_grupo_poblacional_id in pertenencia_grupo_poblacional_ids:
            pertenencia_grupo_poblacional = PertenenciaGrupoPoblacional.objects.get(id_grupo_poblacional=pertenencia_grupo_poblacional_id)
            pertenencia_grupo_poblacional.personas.add(persona)
        
        return persona
        
    
