from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']
    def validate(self, attrs):
        """
        Ensure that each '_liked' field contains only integers.
        """
        for key, value in attrs.items():
            if key.endswith('_liked'):
                invalids = [i for i in value if not isinstance(i, int)]
                if invalids: 
                    raise serializers.ValidationError({key: f'Invalid data in the list, only numbers are allowed: {invalids}'})

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length=8, max_length=16)
    username = serializers.CharField(max_length=18)
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id','username', 'password', 'profile']
    def create(self, validated_data):
        """
        Create a new user instance with a hashed password.
        """
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user
