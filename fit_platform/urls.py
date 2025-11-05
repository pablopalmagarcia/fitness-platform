"""
URL configuration for fit_platform project.
Also includes user API endpoints and JWT authentication routes.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='access_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]