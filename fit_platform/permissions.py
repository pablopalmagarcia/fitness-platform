from rest_framework.permissions import BasePermission
from django.conf import settings

class HasAPIKey(BasePermission):
    """
    Custom permission that checks for a specific API key in the request headers.
    """
    def has_permission(self, request, view):
        token = request.headers.get('X-API-KEY')
        return token == settings.API_KEY