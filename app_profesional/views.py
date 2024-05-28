from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Profesional
from .serializers import ProfesionalSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class profesional_viewsets(viewsets.ModelViewSet):
    serializer_class = ProfesionalSerializer
    queryset = ProfesionalSerializer.Meta.model.objects.all()
    lookup_field = 'nick'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().partial_update(request, *args, **kwargs)
    
    def update(self, request, nick=None):
        profesional = get_object_or_404(Profesional, nick=nick)
        serializer = self.get_serializer(profesional, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors)