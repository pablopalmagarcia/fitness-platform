from rest_framework import mixins, viewsets, generics, status
from .models import Profile
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class UserCreateView(generics.CreateAPIView):
    """
    View for creating new users.
    """
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        """
        Create a new user and return authentication tokens.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['access'] = str(token.access_token)
        data['refresh'] = str(token)
        return Response(data, status=status.HTTP_201_CREATED)
    
class UserViewSet(viewsets.ModelViewSet):
    """
    View for retrieving, updating, or deleting a user.
    """
    serializer_class = UserSerializer
    def get_queryset(self):
        """
        Limit the queryset to the authenticated user only.
        """
        return User.objects.filter(id=self.request.user.id)
    def create(self, request, *args, **kwargs):
        """
        Disable user creation through this endpoint.
        """
        return Response(
            {"detail": "Use /api/users/create/ to create new users."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

class ProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    View for retrieving and updating a user's profile.
    """
    serializer_class = ProfileSerializer
    def get_queryset(self):
        """
        Return only the profile associated with the authenticated user.
        """
        return Profile.objects.filter(user=self.request.user)