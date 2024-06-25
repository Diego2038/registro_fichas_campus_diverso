from rest_framework import serializers
from rest_framework.exceptions import NotFound
from .models import Seguimiento
from app_registro.models import Persona 
from app_profesional.models import UserProfesional
from django.shortcuts import get_object_or_404

class ProfesionalListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['username'].strip()
        raise serializers.ValidationError('Invalid input format.')

class SeguimientoSerializer(serializers.ModelSerializer):
    id_persona = serializers.CharField(max_length=30, required=True)
    profesionales = ProfesionalListingField(
        many=True,
        queryset= UserProfesional,
        required=False,
    )
    
    class Meta:
        model = Seguimiento
        fields = '__all__'
        
    def create(self, validated_data):
        id_persona = validated_data.pop('id_persona')
        profesionales = validated_data.pop('profesionales', [])
        
        persona = Persona.objects.filter(numero_documento=id_persona).first()
        if not persona:
            raise NotFound(detail=f"The id_persona {id_persona} don't exist", code=404)
        
        if not profesionales:
            raise NotFound(detail=f"profesionales field don't should be void", code=403)
        
        seguimiento = Seguimiento.objects.create(id_persona=persona, **validated_data)
        # Profesionales
        for username in profesionales:
            profesional = get_object_or_404(UserProfesional, username=username)
            seguimiento.profesionales.add(profesional)

        return seguimiento

    def update(self, instance, validated_data):
        profesionales = validated_data.pop('profesionales', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Profesionales
        if profesionales:
            instance.profesionales.clear()
            for username in profesionales:
               profesional = get_object_or_404(UserProfesional, username=username)
               instance.profesionales.add(profesional) 
        
        return super().update(instance, validated_data)