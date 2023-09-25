from django.shortcuts import get_object_or_404

from rest_framework import generics

from organization.models import OrganizationUser
from ..serializers.appointment import *
from organization.rest.permissions import IsOrganizationMember


class CreateAppointmentWithDoctorView(generics.CreateAPIView):
    """Create an appointment for logged in Patient with an Doctor"""

    permission_classes = []
    serializer_class = CreateAppointmentWithDoctorSerializer


class CreateAppointmentForLabTestView(generics.CreateAPIView):
    """Create an appointment for logged in Patient for a lab-test"""

    permission_classes = []
    serializer_class = CreateAppointmentForLabTestSerializer
