from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TriangulationViewSet

triangulation_router = DefaultRouter()
triangulation_router.register(r'triangulation', TriangulationViewSet, basename='')