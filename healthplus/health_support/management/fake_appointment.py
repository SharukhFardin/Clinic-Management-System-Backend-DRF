from typing import Any
from django.core.management.base import BaseCommand
from organization.models import Patient, Doctor, Organization

from health_support.choices import *
from ..models import Appointment
from faker import faker
import random


class Command(BaseCommand):
    help = "Generate 100 fake appointments"

    def handle(self, *args: Any, **options: Any) -> str | None:
        fake = faker()
        patients = Patient.objects.all()
        doctors = Doctor.objects.all()
        organizations = Organization.objects.all()

        for _ in range(100):
            appointment = Appointment(
                patient=random.choice(patients),
                doctor=random.choice(doctors),
                organization=random.choice(organizations),
                schedule_start=fake.date_time_this_decade(),
                schedule_end=fake.date_time_this_decade(),
                location=fake.random_element(
                    elements=[choice[0] for choice in AppointmentLocation.choices]
                ),
                type=fake.random_element(
                    elements=[choice[0] for choice in AppointmentType.choices]
                ),
                status=fake.random_element(
                    elements=[choice[0] for choice in AppointmentStatus.choices]
                ),
                address=fake.address(),
                slug=fake.slug(),
            )
            appointment.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully generated 100 fake appointments.")
        )

        return super().handle(*args, **options)
