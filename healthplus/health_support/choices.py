from django.db import models


class LabTestType(models.TextChoices):
    XRAY = "XRAY", "Xray"
    MRI = "MRI", "Mri"


class AppointmentType(models.TextChoices):
    LABTEST = "LABTEST", "Labtest"
    CHECKUP = "CHECKUP", "Checkup"
    FOLLOWUP = "FOLLOWUP", "Followup"


class AppointmentStatus(models.TextChoices):
    APPROVED = "APPROVED", "Approved"
    PENDING = "PENDING", "Pending"
    DENIED = "DENIED", "Denied"


class AppointmentLocation(models.TextChoices):
    HOME = "HOME", "Home"
    ONSITE = "ONSITE", "Onsite"