from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app_registro.models import Persona
from .models import DocumentosAutorizacion
from .serializers import DocumentosAutorizacionSerializer


# DocumentosAutorizacion
class DocumentosAutorizacionListCreateView(generics.ListCreateAPIView):
    queryset = DocumentosAutorizacion.objects.all()
    serializer_class = DocumentosAutorizacionSerializer

class DocumentosAutorizacionRetrievelUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentosAutorizacion.objects.all()
    serializer_class = DocumentosAutorizacionSerializer
    lookup_field = 'id_persona'
    
    def get_serializer(self, *args, **kwargs): #! Para poder realizar las actualizaciones sin necesidad de todos los atributos
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
    
    def get_object(self):
        id_persona = self.kwargs['id_persona'] 
        persona = get_object_or_404(Persona, numero_documento=id_persona)
        documentos_autorizacion = get_object_or_404(DocumentosAutorizacion, id_persona=persona)
        return documentos_autorizacion
    
    def put(self, request, *args, **kwargs):
        id_persona = self.kwargs['id_persona']
        persona = Persona.objects.get(numero_documento=id_persona)
        documentos_autorizacion = DocumentosAutorizacion.objects.get(id_persona=persona)
        serializer = self.get_serializer(documentos_autorizacion, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
      
    def delete(self):
        id_persona = self.kwargs['id_persona']
        persona = Persona.objects.get(numero_documento=id_persona)
        documentos_autorizacion = DocumentosAutorizacion.objects.get(id_persona=persona)
        self.perform_destroy(documentos_autorizacion)
        return Response(status.HTTP_204_NO_CONTENT)
