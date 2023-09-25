from rest_framework import serializers
from health_support.models import LabTest
from organization.rest.serializers.user import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = LabTest
        fields = (
            "uid",
            "name",
            "slug",
            "user",
            "created_at",
            "updated_at",
        )
