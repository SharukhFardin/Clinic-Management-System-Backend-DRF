from rest_framework import serializers
from organization.models import Patient
from .user import UserSerializer

from organization.helper.user import UserService

from phonenumber_field.serializerfields import PhoneNumberField


class PatientRegistrationSerializer(serializers.Serializer):
    uid = serializers.UUIDField(read_only=True, source="patient.uid")
    slug = serializers.SlugField(read_only=True, source="patient.slug")
    name = serializers.CharField(max_length=255)
    phone_number = PhoneNumberField()
    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=5,
        max_length=100,
        write_only=True,
    )
    address = serializers.CharField(max_length=50, allow_blank=True)
    user_type = serializers.CharField(max_length=50, read_only=True)

    def create(self, validated_data):
        """Create an User then assign that user as a Patient"""
        user_helper = UserService()

        # Create User
        user = user_helper.create_user(
            phone=validated_data.get("phone"),
            password=validated_data.get("password", str(validated_data["phone"])),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            email=validated_data.get("email", ""),
        )

        # Set that user as an patient
        patient = Patient.objects.create(user=user.id)

        return validated_data


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Patient
        fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
            "user",
        ]
