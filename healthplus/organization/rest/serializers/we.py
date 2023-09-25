from rest_framework import serializers
from organization.models import Organization, OrganizationUser
from ..serializers.user import UserSerializer

from organization.helper.user import UserService


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "uid",
            "slug",
            "parent",
            "name",
            "CEO_name",
            "tax_number",
            "registration_no",
            "website_url",
            "facebook_url",
            "instagram_url",
            "linkedin_url",
            "twitter_url",
            "phone_number",
            "summary",
            "description",
            "created_at",
            "updated_at",
        )


class OrganizationUserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer
    user = UserSerializer()

    class Meta:
        model = OrganizationUser
        fields = (
            "uid",
            "role",
            "organization",
            "user",
            "is_staff",
            "is_default",
        )

        def create(self, validated_data):
            """Create an User then assign that user as a Patient"""
            user_helper = UserService()

            organization_user = OrganizationUser.objects.filter(user).first()
            organization = organization_user.organization

            # Create User
            user = user_helper.create_user(
                phone=validated_data.get("phone"),
                password=validated_data.get("password", str(validated_data["phone"])),
                first_name=validated_data.get("first_name", ""),
                last_name=validated_data.get("last_name", ""),
                email=validated_data.get("email", ""),
            )

            # Create the OrganizationUser
            return OrganizationUser.objects.create(
                user=user.id, organization=organization.id, **validated_data
            )
