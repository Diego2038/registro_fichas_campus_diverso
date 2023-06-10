from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics, status
from .models import Seguimiento
from .serializers import SeguimientoSerializer
from app_registro.models import Persona
from rest_framework.response import Response

class SeguimientoListCreateView(generics.ListCreateAPIView):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer
    
class SeguimientoRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer
    
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
      
    # def get_object(self):
    #     id_persona = self.kwargs['id_persona']
    #     persona = get_object_or_404(Persona, numero_documento=id_persona)
    #     seguimientos = Seguimiento.objects.filter(numero_documento=persona)
    #     if seguimientos.exists():
    #         return seguimientos
    #     else:
    #         raise status.HTTP_404_NOT_FOUND
      
     