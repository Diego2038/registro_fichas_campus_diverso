from django.urls import path
from .views import PersonaListCreateView, PersonaRetrieveUpdateDestroyView

urlpatterns = [
    path('personas/', PersonaListCreateView.as_view(), name='persona-list-create'),
    path('personas/<int:pk>/', PersonaRetrieveUpdateDestroyView.as_view(), name='persona-retrieve-update-destroy'),
]
