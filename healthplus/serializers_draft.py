from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from versatileimagefield.serializers import VersatileImageFieldSerializer

from accountio.services.organizations import OrganizationService
from accountio.choices import OrganizationUserRoleChoices

from core.services.users import UserService
from core.models import User

from shared.variables import versatile_image_size


class PublicOrganizationUserOnboardingSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50, allow_blank=True)
    last_name = serializers.CharField(max_length=50, allow_blank=True)
    phone = PhoneNumberField()
    email = serializers.EmailField(allow_blank=True)
    password = serializers.CharField(
        min_length=5,
        max_length=100,
        write_only=True,
        required=False,
    )
    image = VersatileImageFieldSerializer(
        allow_null=True,
        allow_empty_file=True,
        sizes=versatile_image_size,
        write_only=True,
    )
    organization_name = serializers.CharField(max_length=255)
    contact_number = PhoneNumberField(allow_blank=True)
    kind = serializers.CharField(allow_blank=True)
    tax_number = serializers.CharField(allow_blank=True)
    registration_no = serializers.CharField(allow_blank=True)
    website_url = serializers.URLField(allow_blank=True)
    blog_url = serializers.URLField(allow_blank=True)
    linkedin_url = serializers.URLField(allow_blank=True)
    instagram_url = serializers.URLField(allow_blank=True)
    facebook_url = serializers.URLField(allow_blank=True)
    twitter_url = serializers.URLField(allow_blank=True)
    whatsapp_number = PhoneNumberField(allow_blank=True)
    summary = serializers.CharField(max_length=1000, allow_blank=True)
    description = serializers.CharField(max_length=1000, allow_blank=True)

    def create(self, validated_data):
        """Get or create a user by their phone number, create an organization,
        assign the user to it, set their role, and return the validated data."""
        user_helper = UserService()
        organization_helper = OrganizationService()

        try:
            # Get user by phone number
            user = user_helper.get_user_by_phone(validated_data["phone"])
        except User.DoesNotExist:
            # If user is not found then creating a new user
            user = user_helper.create_user(
                phone=validated_data.get("phone"),
                password=validated_data.get("password", str(validated_data["phone"])),
                first_name=validated_data.get("first_name", ""),
                last_name=validated_data.get("last_name", ""),
                email=validated_data.get("email", ""),
                image=validated_data.get("image", None),
            )

        # Creating organization
        organization = organization_helper.create_organization(
            name=validated_data.get("organization_name"),
            contact_number=validated_data.get("contact_number", ""),
            kind=validated_data.get("kind", ""),
            tax_number=validated_data.get("tax_number", ""),
            registration_no=validated_data.get("registration_no", ""),
            website_url=validated_data.get("website_url", ""),
            blog_url=validated_data.get("blog_url", ""),
            linkedin_url=validated_data.get("linkedin_url", ""),
            instagram_url=validated_data.get("instagram_url", ""),
            facebook_url=validated_data.get("facebook_url", ""),
            twitter_url=validated_data.get("twitter_url", ""),
            whatsapp_number=validated_data.get("whatsapp_number", ""),
            summary=validated_data.get("summary", ""),
            description=validated_data.get("description", ""),
        )

        # Creating a user of that organization
        organization_user = organization_helper.create_organization_user(
            organization=organization,
            role=OrganizationUserRoleChoices.OWNER,
            user=user,
        )

        return validated_data


""">>>>>>>>>>>>>>>>>>>>>>>>>>>USER HELPER<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
from core.choices import UserStatus

from core.models import User


class UserService:
    def create_superuser(
        self,
        phone: str,
        password: str,
        first_name: str = "",
        last_name: str = "",
        email: str = "",
        image: str = None,
    ) -> User:
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            email=email,
            image=image,
            status=UserStatus.ACTIVE,
            is_active=True,
            is_staff=True,
            is_verified=True,
            is_superuser=True,
        )

    def create_user(
        self,
        phone: str,
        password: str,
        first_name: str = "",
        last_name: str = "",
        email: str = "",
        image: str = None,
        status: UserStatus.choices = UserStatus.ACTIVE,
        is_active: bool = True,
        is_staff: bool = False,
        is_verified: bool = True,
    ) -> User:
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            email=email,
            image=image,
            status=status,
            is_active=is_active,
            is_staff=is_staff,
            is_verified=is_verified,
        )

    def get_user_by_phone(self, phone: str) -> User:
        return User.objects.get(phone=phone)

    def get_user_by_email(self, email: str) -> User:
        return User.objects.get(email=email)

    def get_user_by_either_phone_or_email(self, value) -> User:
        try:
            return self.get_user_by_email(email=value)

        except User.DoesNotExist:
            return self.get_user_by_phone(phone=value)
