from django.urls import path
from .views import DiversidadSexualListCreateView, DiversidadSexualRetrieveUpdateDestroyView

urlpatterns = [
    path('personas/', DiversidadSexualListCreateView.as_view(), name='diversidad-sexual-list-create'),
    path('personas/<str:id_persona>/', DiversidadSexualRetrieveUpdateDestroyView.as_view(), name='diversidad-sexual-retrieve-update-destroy'),
    # path('pertenencia_grupo_poblacional/', PertenenciaGrupoPoblacionalListCreateView.as_view(), name='pertenencia-grupo-poblacional-list-create'),
    # path('pertenencia_grupo_poblacional/<str:pk>/', PertenenciaGrupoPoblacionalRetrieveUpdateDestroyView.as_view(), name='pertenencia-grupo-poblacional-retrieve-update-destroy'),
]