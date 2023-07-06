from rest_framework.routers import DefaultRouter
from .views import informacion_academica_viewset, estamento_viewset

router = DefaultRouter()

router.register(r'informacion-academica', informacion_academica_viewset, basename="informacion-academica")
router.register(r'estamento', estamento_viewset, basename="estamento")

urlpatterns = router.urls