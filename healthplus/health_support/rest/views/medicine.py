from django.shortcuts import get_object_or_404

from rest_framework import generics

from ..serializers.appointment import CreateAppointmentWithDoctorSerializer
from organization.rest.permissions import IsOrganizationMember


class MedicineView(generics.ListCreateAPIView):
    """Create an appointment for logged in Patient with an Doctor"""

    permission_classes = [IsOrganizationMember]
    serializer_class = CreateAppointmentWithDoctorSerializer


class MedicineList(generics.RetrieveUpdateDestroyAPIView):
    """Create an appointment for logged in Patient with an Doctor"""

    permission_classes = [IsOrganizationMember]
    serializer_class = CreateAppointmentWithDoctorSerializer
