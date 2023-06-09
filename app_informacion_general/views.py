from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app_registro.models import Persona
from .models import InformacionGeneral, OcupacionActual, ActividadTiempoLibre, FuenteIngresos
from .serializers import InformacionGeneralSerializer, OcupacionActualSerializer, ActividadTiempoLibreSerializer, FuenteIngresosSerializer

# FuenteIngresos
class FuenteIngresosListCreateView(generics.ListCreateAPIView):
    queryset = FuenteIngresos.objects.all()
    serializer_class = FuenteIngresosSerializer

class FuenteIngresosRetrievelUpdateDestroyView (generics.RetrieveUpdateDestroyAPIView):
    queryset = FuenteIngresos.objects.all()
    serializer_class = FuenteIngresosSerializer
    
    def get_serializer(self, *args, **kwargs): #! Para poder realizar las actualizaciones sin necesidad de todos los atributos
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)

# ActividadTiempoLibre
class ActividadTiempoLibreListCreateView(generics.ListCreateAPIView):
    queryset = ActividadTiempoLibre.objects.all()
    serializer_class = ActividadTiempoLibreSerializer
   
class ActividadTiempoLibreRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActividadTiempoLibre.objects.all()
    serializer_class = ActividadTiempoLibreSerializer 
    
    def get_serializer(self, *args, **kwargs): #! Para poder realizar las actualizaciones sin necesidad de todos los atributos
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
  
# OcupacionActual
class OcupacionActualListCreateView(generics.ListCreateAPIView):
    queryset = OcupacionActual.objects.all()
    serializer_class = OcupacionActualSerializer
   
class OcupacionActualRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OcupacionActual.objects.all()
    serializer_class = OcupacionActualSerializer
  
# InformacionGeneral
class InformacionGeneralListCreateView(generics.ListCreateAPIView):
    queryset = InformacionGeneral.objects.all()
    serializer_class = InformacionGeneralSerializer

class InformacionGeneralRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InformacionGeneral.objects.all()
    serializer_class = InformacionGeneralSerializer
    lookup_field = 'id_persona'
    
    def get_object(self):
        id_persona = self.kwargs['id_persona'] 
        persona = get_object_or_404(Persona, numero_documento=id_persona)
        informacion_academica = get_object_or_404(InformacionGeneral, id_persona=persona)
        return informacion_academica
    
    def put(self, request, *args, **kwargs):
        id_persona = self.kwargs['id_persona']
        persona = Persona.objects.get(numero_documento=id_persona)
        informacion_academica = InformacionGeneral.objects.get(id_persona=persona)
        serializer = self.get_serializer(informacion_academica, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
      
    def delete(self):
        id_persona = self.kwargs['id_persona']
        persona = Persona.objects.get(numero_documento=id_persona)
        informacion_academica = InformacionGeneral.objects.get(id_persona=persona)
        self.perform_destroy(informacion_academica)
        return Response(status.HTTP_204_NO_CONTENT)
