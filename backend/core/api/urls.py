from rest_framework.routers import DefaultRouter
from triangulation.api.urls import triangulation_router
from django.urls import path, include

router = DefaultRouter()
router.registry.extend(triangulation_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
