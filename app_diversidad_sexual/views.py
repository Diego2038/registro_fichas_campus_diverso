from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import DiversidadSexual, Pronombre, IdentidadGenero, ExpresionGenero
from .serializers import DiversidadSexualSerializer,PronombreSerializer, IdentidadGeneroSerializer, ExpresionGeneroSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from app_registro.models import Persona 

# ExpresionGenero
class ExpresionGeneroListCreateView(generics.ListCreateAPIView):
    queryset = ExpresionGenero.objects.all()
    serializer_class = ExpresionGeneroSerializer
    
class ExpresionGeneroRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpresionGenero.objects.all()
    serializer_class = ExpresionGeneroSerializer

# IdentidadGenero
class IdentidadGeneroListCreateView(generics.ListCreateAPIView):
    queryset = IdentidadGenero.objects.all()
    serializer_class = IdentidadGeneroSerializer
    
class IdentidadGeneroRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IdentidadGenero.objects.all()
    serializer_class = IdentidadGeneroSerializer

# Pronombre
class PronombreListCreateView(generics.ListCreateAPIView):
    queryset = Pronombre.objects.all()
    serializer_class = PronombreSerializer
    
class PronombreRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pronombre.objects.all()
    serializer_class = PronombreSerializer


# Diversidad Sexual
class DiversidadSexualListCreateView(generics.ListCreateAPIView):
    queryset = DiversidadSexual.objects.all()
    serializer_class = DiversidadSexualSerializer


class DiversidadSexualRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiversidadSexual.objects.all()
    serializer_class = DiversidadSexualSerializer
    lookup_field = 'id_persona'
    
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
    
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