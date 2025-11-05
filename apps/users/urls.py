"""
URL configuration for user and profile endpoints.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateView, UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("profiles", ProfileViewSet, basename="profiles")

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path("", include(router.urls)),
]