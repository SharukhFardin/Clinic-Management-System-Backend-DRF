from django.db import models

from core.models import CustomBaseModel
from organization.models import Organization, Patient, Doctor
from .choices import *


class DiseaseCategory(CustomBaseModel):
    "Disease Category model"
    name = models.CharField(max_length=255)
    description = models.TextField()


class Disease(CustomBaseModel):
    "Disease model"
    name = models.CharField(max_length=255)
    description = models.TextField()
    disease_category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class MedicineCategory(CustomBaseModel):
    "Disease Category model"
    name = models.CharField(max_length=255)
    description = models.TextField()


class Medicine(CustomBaseModel):
    "Disease model"
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    medicine_category = models.ForeignKey(MedicineCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class LabTest(CustomBaseModel):
    "Model for class test"
    name = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=LabTestType.choices)


class Appointment(CustomBaseModel):
    "Model for labtest booking"
    patient = models.ForeignKey(
        Patient, on_delete=models.SET_NULL, null=True, blank=True
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    schedule_start = models.DateTimeField()
    schedule_end = models.DateTimeField()
    location = models.CharField(max_length=20, choices=AppointmentLocation.choices)
    type = models.CharField(max_length=20, choices=AppointmentType.choices)
    status = models.CharField(max_length=20, choices=AppointmentStatus.choices)
    address = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    # For follow-up appointments
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appointment_followup",
    )

    def save(self, *args, **kwargs):
        if self.type == AppointmentType.FollowUp:
            if not self.parent:
                raise ValueError(
                    "Follow-up appointments must have a parent appointment."
                )
        super().save(*args, **kwargs)


class LabTestAppointmentConnector(CustomBaseModel):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    lab_test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
