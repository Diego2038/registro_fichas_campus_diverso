from django.urls import path
from .views import DiversidadSexualListCreateView, DiversidadSexualRetrieveUpdateDestroyView, PronombreListCreateView, PronombreRetrievelUpdateDestroyView, IdentidadGeneroListCreateView, IdentidadGeneroRetrievelUpdateDestroyView

urlpatterns = [
    path('diversidad-sexual/', DiversidadSexualListCreateView.as_view(), name='diversidad-sexual-list-create'),
    path('diversidad-sexual/<str:id_persona>/', DiversidadSexualRetrieveUpdateDestroyView.as_view(), name='diversidad-sexual-retrieve-update-destroy'),
    path('pronombre/', PronombreListCreateView.as_view(), name='pronombre-list-create'),
    path('pronombre/<str:pk>/', PronombreRetrievelUpdateDestroyView.as_view(),name='pronombre-retrieve-update-destroy'),
    path('identidad-genero/', IdentidadGeneroListCreateView.as_view(), name='identidad-genero-list-create'),
    path('identidad-genero/<str:pk>/', IdentidadGeneroRetrievelUpdateDestroyView.as_view(),name='identidad-genero-retrieve-update-destroy'),
]