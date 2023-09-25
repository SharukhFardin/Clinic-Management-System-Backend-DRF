from rest_framework import serializers
from health_support.models import LabTest
from organization.rest.serializers.we import OrganizationSerializer
from organization.rest.serializers.patient import PatientSerializer


class LabTestSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    patient = PatientSerializer()

    class Meta:
        model = LabTest
        fields = (
            "uid",
            "name",
            "slug",
            "description",
            "organization",
            "patient",
            "type",
            "created_at",
            "updated_at",
            "description",
        )
