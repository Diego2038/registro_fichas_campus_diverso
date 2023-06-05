from rest_framework import serializers
from .models import DiversidadSexual, Pronombre, IdentidadGenero, ExpresionGenero
from app_registro.models import Persona


class ExpresionGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpresionGenero
        fields = '__all__'

class IdentidadGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentidadGenero
        fields = '__all__'

class PronombreSerializer(serializers.ModelSerializer):
    nombre_pronombre = serializers.CharField(max_length=50, required=True)
    
    class Meta:
        model = Pronombre
        fields = '__all__'

# Listing Fields de los serializers

class ExpresionGeneroListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_expresion_genero
   
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_expresion_genero'].strip()
        raise serializers.ValidationError('Invalid input format.')

class IdentidadGeneroListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_identidad_genero
    
    def to_internal_value(self, data):
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, dict):
            return data['nombre_identidad_genero'].strip()
        raise serializers.ValidationError('Invalid input format.')


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
    
    expresiones_de_genero = ExpresionGeneroListingField(
        many=True,
        queryset=ExpresionGenero.objects.all(),
        required=False,
    )
    
    identidades_de_genero = IdentidadGeneroListingField(
        many=True,
        queryset=IdentidadGenero.objects.all(),
        required=False,
    )
    
    pronombres = PronombreListingField(
        many=True,
        queryset=Pronombre.objects.all(),
        required=False,
    )
    
     
    class Meta:
        model = DiversidadSexual
        fields = '__all__'
    
    def create(self, validated_data):
        # Extracción de campos de la petición JSON
        id_persona = validated_data.pop('id_persona')
        expresiones_de_genero = validated_data.pop('expresiones_de_genero')
        pronombres = validated_data.pop('pronombres', [])
        identidades_de_genero = validated_data.pop('identidades_de_genero')
        
        persona = Persona.objects.get(numero_documento=id_persona) #! Así son más fáciles las consultas
        
        # Creación del objeto DiversidadSexual
        diversidad_sexual = DiversidadSexual.objects.create(id_persona=persona, **validated_data)
        
        # Pronombre
        for pronombre in pronombres:
            pronombres, _ = Pronombre.objects.get_or_create(nombre_pronombre=pronombre)
            diversidad_sexual.pronombres.add(pronombres)
        # IdentidadGenero
        for nombre_identidad_genero in identidades_de_genero:
            identidad_genero, _ = IdentidadGenero.objects.get_or_create(nombre_identidad_genero=nombre_identidad_genero)
            diversidad_sexual.identidades_de_genero.add(identidad_genero)
        # ExpresionGenero
        for nombre_expresion_genero in expresiones_de_genero:
            expresion_genero, _ = ExpresionGenero.objects.get_or_create(nombre_expresion_genero=nombre_expresion_genero)
            diversidad_sexual.expresiones_de_genero.add(expresion_genero)
             

        return diversidad_sexual 