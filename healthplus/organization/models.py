from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField

# from varsitileimagefield.fields import VarsitileImageField

from django.db import models
from django.contrib.auth.models import (
    User,
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid

from core.models import CustomBaseModel
from .choices import *


class UserManager(BaseUserManager):
    # Manager class for users

    def create_user(self, email, password=None, **extra_fields):
        # Method for creating user
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):  # autoslugfield
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        # user.is_active = True
        user.save(using=self._db)

        return user


# Custom User Model for the system
class User(AbstractBaseUser, PermissionsMixin):
    "Users in the system"
    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    # phone_number = PhoneNumberField(blank=True)
    slug = AutoSlugField(unique=True, populate_from="name")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"


# Organization Model. Pharmacy is a organization in case of this system.
class Organization(CustomBaseModel):
    "Organization in the system"
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )
    name = models.CharField(max_length=100)
    CEO_name = models.CharField(max_length=100)
    tax_number = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100)
    website_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    phone_number = PhoneNumberField()
    summary = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    def get_name(self):
        return self.name


# Model to hold relavant data to every organization User. It is a inbetween model between organization & User
class OrganizationUser(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    role = models.CharField(
        max_length=10, choices=OrganizationUserRoles.choices, default="customer"
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"ID: {self.id}, Org: {self.organization}, User: {self.user}, Role: {self.role}"


class Doctor(CustomBaseModel):
    "Doctors in the system"
    designation = models.CharField(max_length=255)
    specialty = models.CharField(max_length=50)
    expertise = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, populate_from="user__name")


class Patient(CustomBaseModel):
    "Patients in the system"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, populate_from="user__name")
