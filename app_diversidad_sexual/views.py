from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import DiversidadSexual
from .serializers import DiversidadSexualSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from app_registro.models import Persona 

# Persona
class DiversidadSexualListCreateView(generics.ListCreateAPIView):
    queryset = DiversidadSexual.objects.all()
    serializer_class = DiversidadSexualSerializer


class DiversidadSexualRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiversidadSexual.objects.all()
    serializer_class = DiversidadSexualSerializer
    lookup_field = 'id_persona'
    
    def get_object(self):
        id_persona = self.kwargs['id_persona']
        persona = get_object_or_404(Persona, numero_documento=id_persona)
        diversidad_sexual = get_object_or_404(DiversidadSexual, id_persona=persona)
        return diversidad_sexual
    
    def put(self, request, *args, **kwargs):
        id_persona = self.kwargs['id_persona']
        persona = get_object_or_404(Persona, numero_documento=id_persona)
        diversidad_sexual = get_object_or_404(DiversidadSexual, id_persona=persona)
        serializer = self.get_serializer(diversidad_sexual, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        id_persona = self.kwargs['id_persona']
        persona = get_object_or_404(Persona, numero_documento=id_persona)
        diversidad_sexual = get_object_or_404(DiversidadSexual, id_persona=persona)
        self.perform_destroy(diversidad_sexual)
        return Response(status.HTTP_204_NO_CONTENT)