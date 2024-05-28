from rest_framework.routers import DefaultRouter
from .views import profesional_viewsets

router = DefaultRouter()

router.register(r'profesional', profesional_viewsets, basename='profesional')

urlpatterns = router.urls