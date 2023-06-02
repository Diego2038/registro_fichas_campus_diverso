from rest_framework import serializers
from .models import Persona, PertenenciaGrupoPoblacional



class PersonaSerializer(serializers.ModelSerializer):
    # pertenencia_grupo_poblacional = PertenenciaGrupoPoblacionalSerializer(many=True, required=False)
    pertenencia_grupo_poblacional = serializers.SerializerMethodField()

    class Meta:
        model = Persona
        fields = '__all__'

    def get_pertenencia_grupo_poblacional(self, obj):
        from .serializers import PertenenciaGrupoPoblacionalSerializer
        # pertenencias = obj.pertenencia_grupo_poblacional.all()
        # serializer = PertenenciaGrupoPoblacionalSerializer(pertenencias)
        # return serializer.data
        if hasattr(obj, 'pertenencia_grupo_poblacional'):
            pertenencias = obj.pertenencia_grupo_poblacional.all()
        else:
            pertenencias = []

        serializer = PertenenciaGrupoPoblacionalSerializer(pertenencias, many=True, required=False)
        return serializer.data
    
class PertenenciaGrupoPoblacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PertenenciaGrupoPoblacional
        fields = '__all__'
