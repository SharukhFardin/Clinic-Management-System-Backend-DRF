from django.shortcuts import get_object_or_404

from rest_framework import generics

from health_support.models import LabTest
from ..serializers.labtest import LabTestSerializer
from organization.rest.permissions import IsOrganizationMember


class LabTestView(generics.ListAPIView):
    """Logged In Patient can view the labtest he has enlisted"""

    queryset = LabTest.objects.filter()
    permission_classes = []
    serializer_class = LabTestSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user)
