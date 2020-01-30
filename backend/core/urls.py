from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import CarViewSet


router = DefaultRouter()
router.register("cars", CarViewSet)

urlpatterns = router.urls