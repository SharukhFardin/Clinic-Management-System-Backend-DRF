from django.shortcuts import get_object_or_404

from rest_framework import generics

from organization.models import Patient
from ..serializers.patient import PatientRegistrationSerializer, PatientSerializer
from organization.rest.permissions import IsOrganizationMember


class PatientRegistration(generics.CreateAPIView):
    """Create or view list for all the organization doctors for ogranization users"""

    permission_classes = []
    serializer_class = PatientRegistrationSerializer

    def get_queryset(self):
        user = self.request.user
        organization = user.OrganizationUser_set.first().organization
        return self.queryset.filter(organization)


class PatientList(generics.ListAPIView):
    """Create or view list for all the organization doctors for ogranization users"""

    permission_classes = [IsOrganizationMember]
    serializer_class = PatientSerializer

    def get_queryset(self):
        user = self.request.user
        organization = user.OrganizationUser_set.first().organization
        return self.queryset.filter(organization)


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrive, update or delete organization doctors for ogranization users"""

    permission_classes = [IsOrganizationMember]
    serializer_class = PatientSerializer
    lookup_field = "uid"
