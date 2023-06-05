from django.urls import path
from .views import DiversidadSexualListCreateView, DiversidadSexualRetrieveUpdateDestroyView, PronombreListCreateView, PronombreRetrievelUpdateDestroyView

urlpatterns = [
    path('diversidad-sexual/', DiversidadSexualListCreateView.as_view(), name='diversidad-sexual-list-create'),
    path('diversidad-sexual/<str:id_persona>/', DiversidadSexualRetrieveUpdateDestroyView.as_view(), name='diversidad-sexual-retrieve-update-destroy'),
    path('pronombre/', PronombreListCreateView.as_view(), name='pronombre-list-create'),
    path('pronombre/<str:pk>/', PronombreRetrievelUpdateDestroyView.as_view(),name='pronombre-retrieve-update-destroy')
    # path('pertenencia_grupo_poblacional/', PertenenciaGrupoPoblacionalListCreateView.as_view(), name='pertenencia-grupo-poblacional-list-create'),
    # path('pertenencia_grupo_poblacional/<str:pk>/', PertenenciaGrupoPoblacionalRetrieveUpdateDestroyView.as_view(), name='pertenencia-grupo-poblacional-retrieve-update-destroy'),
]