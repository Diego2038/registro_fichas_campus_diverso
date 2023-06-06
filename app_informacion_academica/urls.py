from django.urls import path 
from .views import InformacionAcademicaListCreateView, InformacionAcademicaRetrievelUpdateDestroyView

urlpatterns = [
    # path('diversidad-sexual/', DiversidadSexualListCreateView.as_view(), name='diversidad-sexual-list-create'),
    # path('diversidad-sexual/<str:id_persona>/', DiversidadSexualRetrieveUpdateDestroyView.as_view(), name='diversidad-sexual-retrieve-update-destroy'),
    path("informacion-academica/", InformacionAcademicaListCreateView.as_view(), name='informacion-academica-list-create-view'),
    path('informacion-academica/<str:id_persona>/', InformacionAcademicaRetrievelUpdateDestroyView.as_view(), name='informacion-academica-retrievel-update-destroy-view')
]