from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Persona, PertenenciaGrupoPoblacional
from .serializers import PersonaSerializer, PertenenciaGrupoPoblacionalSerializer

# Persona
class PersonaListCreateView(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class PersonaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'numero_documento'
    
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)

# Pertenencia grupo poblacional

class PertenenciaGrupoPoblacionalListCreateView(generics.ListCreateAPIView):
    queryset = PertenenciaGrupoPoblacional.objects.all()
    serializer_class = PertenenciaGrupoPoblacionalSerializer

class PertenenciaGrupoPoblacionalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PertenenciaGrupoPoblacional.objects.all()
    serializer_class = PertenenciaGrupoPoblacionalSerializer 