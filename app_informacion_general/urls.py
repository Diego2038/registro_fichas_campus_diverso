from django.urls import path 
from .views import InformacionGeneralListCreateView, InformacionGeneralRetrievelUpdateDestroyView 

urlpatterns = [ 
    path("informacion-general/", InformacionGeneralListCreateView.as_view(), name='informacion-general-list-create-view'),
    path('informacion-general/<str:id_persona>/', InformacionGeneralRetrievelUpdateDestroyView.as_view(), name='informacion-general-retrievel-update-destroy-view'),
]