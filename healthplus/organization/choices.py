from django.db import models


class OrganizationUserRoles(models.TextChoices):
    OWNER = "OWNER", "Owner"
    ADMIN = "ADMIN", "Admin"
    MANAGER = "MANAGER", "Manager"
    DOCTOR = "DOCTOR", "Doctor"
    STAFF = "STAFF", "Staff"
