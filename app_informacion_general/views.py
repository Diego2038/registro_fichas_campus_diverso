from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app_registro.models import Persona
from .models import InformacionGeneral, OcupacionActual, ActividadTiempoLibre, FuenteIngresos, ConvivenciaVivienda, RedApoyo, FactorRiesgo, EncuentroDiaHora
from .serializers import InformacionGeneralSerializer, OcupacionActualSerializer, ActividadTiempoLibreSerializer, FuenteIngresosSerializer, ConvivenciaViviendaSerializer, RedApoyoSerializer, FactorRiesgoSerializer, EncuentroDiaHoraSerializer


# EncuentroDiaHora
class EncuentroDiaHoraListCreateView(generics.ListCreateAPIView):
    queryset = EncuentroDiaHora.objects.all()
    serializer_class = EncuentroDiaHoraSerializer

class EncuentroDiaHoraRetrievelUpdateDestroyView (generics.RetrieveUpdateDestroyAPIView):
    queryset = EncuentroDiaHora.objects.all()
    serializer_class = EncuentroDiaHoraSerializer
    
    def get_serializer(self, *args, **kwargs): #! Para poder realizar las actualizaciones sin necesidad de todos los atributos
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


# FactorRiesgo
class FactorRiesgoListCreateView(generics.ListCreateAPIView):
    queryset = FactorRiesgo.objects.all()
    serializer_class = FactorRiesgoSerializer

class FactorRiesgoRetrievelUpdateDestroyView (generics.RetrieveUpdateDestroyAPIView):
    queryset = FactorRiesgo.objects.all()
    serializer_class = FactorRiesgoSerializer
    
    def get_serializer(self, *args, **kwargs): #! Para poder realizar las actualizaciones sin necesidad de todos los atributos
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


# RedApoyo
class RedApoyoListCreateView(generics.ListCreateAPIView):
    queryset = RedApoyo.objects.all()
    serializer_class = RedApoyoSerializer

class RedApoyoRetrievelUpdateDestroyView (generics.RetrieveUpdateDestroyAPIView):
    queryset = RedApoyo.objects.all()
    serializer_class = RedApoyoSerializer
    
    def get_serializer(self, *args, **kwargs): #! Para poder realizar las actualizaciones sin necesidad de todos los atributos
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)


# ConvivenciaVivienda
class ConvivenciaViviendaListCreateView(generics.ListCreateAPIView):
    queryset = ConvivenciaVivienda.objects.all()
    serializer_class = ConvivenciaViviendaSerializer

class ConvivenciaViviendaRetrievelUpdateDestroyView (generics.RetrieveUpdateDestroyAPIView):
    queryset = ConvivenciaVivienda.objects.all()
    serializer_class = ConvivenciaViviendaSerializer
    
    def get_serializer(self, *args, **kwargs): #! Para poder realizar las actualizaciones sin necesidad de todos los atributos
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)

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
