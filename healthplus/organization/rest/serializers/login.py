from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import get_object_or_404

from organization.utils import get_token

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = get_object_or_404(User.objects.filter(), email=email)

        if not user.check_password(password):
            raise AuthenticationFailed(detail="Invalid credentials.")

        # Get JWT tokens
        tokens = get_token(user)
        validated_data["refresh"] = tokens["refresh"]
        validated_data["access"] = tokens["access"]

        return validated_data