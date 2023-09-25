from rest_framework import serializers
from organization.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "uid",
            "name",
            "email",
            "password",
            "phone_number",
            "slug",
            "created_at",
            "updated_at",
            "is_active",
        )
