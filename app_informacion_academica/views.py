from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app_registro.models import Persona
from .models import InformacionAcademica
from .serializers import InformacionAcademicaSerializer

class InformacionAcademicaListCreateView(generics.ListCreateAPIView):
    queryset = InformacionAcademica.objects.all()
    serializer_class = InformacionAcademicaSerializer

class InformacionAcademicaRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InformacionAcademica.objects.all()
    serializer_class = InformacionAcademicaSerializer
    lookup_field = 'id_persona'
    
    def get_object(self):
        id_persona = self.kwargs['id_persona'] 
        persona = get_object_or_404(Persona, numero_documento=id_persona)
        informacion_academica = get_object_or_404(InformacionAcademica, id_persona=persona)
        return informacion_academica
    
    def put(self, request, *args, **kwargs):
        id_persona = self.kwargs['id_persona']
        persona = Persona.objects.get(numero_documento=id_persona)
        informacion_academica = InformacionAcademica.objects.get(id_persona=persona)
        serializer = self.get_serializer(informacion_academica, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
      
    def delete(self):
        id_persona = self.kwargs['id_persona']
        persona = Persona.objects.get(numero_documento=id_persona)
        informacion_academica = InformacionAcademica.objects.get(id_persona=persona)
        self.perform_destroy(informacion_academica)
        return Response(status.HTTP_204_NO_CONTENT)
