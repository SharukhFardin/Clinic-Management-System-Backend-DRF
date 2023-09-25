from django.shortcuts import get_object_or_404

from rest_framework import generics

from organization.models import Organization
from ..serializers.we import OrganizationSerializer, OrganizationUserSerializer
from organization.rest.permissions import IsOrganizationMember


class OrganizationList(generics.ListCreateAPIView):
    """Create or view list for all the organization doctors for ogranization users"""

    permission_classes = [IsOrganizationMember]
    serializer_class = OrganizationSerializer


class OrganizationUserList(generics.ListCreateAPIView):
    """Add New Staff in the Organization and Show the list of Staff"""

    permission_classes = [IsOrganizationMember]
    serializer_class = OrganizationUserSerializer
