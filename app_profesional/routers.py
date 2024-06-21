from rest_framework.routers import DefaultRouter
from .views import profesional_viewsets, login
from django.urls import path

router = DefaultRouter()

router.register(r'profesional', profesional_viewsets, basename='profesional')

urlpatterns = router.urls + [
    path('login/', login, name='login'),
]