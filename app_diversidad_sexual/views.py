from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import DiversidadSexual
from .serializers import DiversidadSexualSerializer

# Persona
class DiversidadSexualListCreateView(generics.ListCreateAPIView):
    queryset = DiversidadSexual.objects.all()
    serializer_class = DiversidadSexualSerializer

class DiversidadSexualRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiversidadSexual.objects.all()
    serializer_class = DiversidadSexualSerializer
    lookup_field = 'id_persona'