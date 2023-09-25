from rest_framework import serializers
from organization.models import Doctor, Organization, OrganizationUser
from .user import UserSerializer

from organization.helper.user import UserService

from phonenumber_field.serializerfields import PhoneNumberField


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = [
            "uid",
            "slug",
            "created_at",
            "updated_at",
            "user",
            "designation",
            "specialty",
            "expertise",
        ]


class DoctorRegistrationSerializer(serializers.Serializer):
    """Individual Registration for doctors by providing organization UID"""

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
    designation = serializers.CharField(max_length=255)
    specialty = serializers.CharField(max_length=50)
    expertise = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """Create an User then assign that user as a Patient"""
        user_helper = UserService()

        request = self.context.get("request")

        # Extract the organization_uid from the URL's query parameters
        org_uid = request.query_params.get("uid")

        # Fetch the LabTest instance based on the UID
        try:
            organization = Organization.objects.get(uid=org_uid)
        except Organization.DoesNotExist:
            raise serializers.ValidationError(
                "Organization with the specified UID does not exist."
            )

        # Create User
        user = user_helper.create_user(
            phone=validated_data.get("phone"),
            password=validated_data.get("password", str(validated_data["phone"])),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            email=validated_data.get("email", ""),
        )

        # Set that user as an doctor
        Doctor.objects.create(user=user.id, **validated_data)

        # Set the doctor as a organization User
        OrganizationUser.objects.create(
            user=user, organization=organization, role="Doctor"
        )

        return validated_data
