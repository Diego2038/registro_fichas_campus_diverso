from django.urls import path 
from .views import InformacionGeneralListCreateView, InformacionGeneralRetrievelUpdateDestroyView, OcupacionActualListCreateView, OcupacionActualRetrievelUpdateDestroyView 

urlpatterns = [ 
    path("informacion-general/", InformacionGeneralListCreateView.as_view(), name='informacion-general-list-create-view'),
    path('informacion-general/<str:id_persona>/', InformacionGeneralRetrievelUpdateDestroyView.as_view(), name='informacion-general-retrievel-update-destroy-view'),
    path("ocupacion-actual/", OcupacionActualListCreateView.as_view(), name='ocupacion-actual-list-create-view'),
    path('ocupacion-actual/<str:pk>/', OcupacionActualRetrievelUpdateDestroyView.as_view(), name='ocupacion-actual-retrievel-update-destroy-view'),
]