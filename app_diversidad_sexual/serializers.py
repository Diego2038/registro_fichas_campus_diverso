from rest_framework import serializers
from .models import DiversidadSexual

class DiversidadSexualSerializer(serializers.ModelSerializer):
    cedula_persona = serializers.CharField(max_length=30, required=True)
    
    class Meta:
        model = DiversidadSexual
        fields = '__all__'