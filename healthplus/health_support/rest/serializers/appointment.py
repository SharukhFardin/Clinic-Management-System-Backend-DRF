from rest_framework import serializers
from health_support.models import Appointment, LabTest, LabTestAppointmentConnector
from organization.models import Organization, Doctor
from organization.rest.serializers.we import OrganizationSerializer
from organization.rest.serializers.doctor import DoctorSerializer
from organization.rest.serializers.patient import PatientSerializer


class CreateAppointmentWithDoctorSerializer(serializers.Serializer):
    # Patient can create an Appointment for lab test or doctor

    uid = serializers.CharField()
    slug = serializers.CharField()
    patient = serializers.UUIDField()
    doctor = serializers.UUIDField()
    organization = serializers.UUIDField()
    schedule_start = serializers.DateTimeField()
    schedule_end = serializers.DateTimeField()
    location = serializers.CharField()
    type = serializers.CharField()
    status = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        # doctor_uid = self.context["request"].query_params.get("doctor_uid")

        # Standard way to get doctor UID
        doctor_uid = self.context["view"].kwargs.get("doctor_uid", None)

        # Fetch the Doctor instances based on the UID
        try:
            doctor = Doctor.objects.get(uid=doctor)

        except Doctor.DoesNotExist:
            raise serializers.ValidationError(
                "Doctor with the specified UID does not exist."
            )

        try:
            organization = Doctor.objects.get(uid=organization)

        except Organization.DoesNotExist:
            raise serializers.ValidationError(
                "Organization with the specified UID does not exist."
            )

        # Create the Appointment object with doctor, patient, and validated data
        appointment = Appointment.objects.create(
            doctor=doctor, patient=user, organization=organization, **validated_data
        )

        return appointment


"""
class CreateAppointmentWithDoctorSerializer(serializers.ModelSerializer):
    # Patient can create an Appointment with doctor

    patient = PatientSerializer()
    doctor = DoctorSerializer()
    # organization = OrganizationSerializer()

    class Meta:
        model = Appointment
        fields = [
            "uid",
            "slug",
            "patient",
            "doctor",
            "organization",
            "description",
            "schedule_start",
            "schedule_end",
            "location",
            "type",
            "status",
            "address",
            "parent",
        ]
        read_only_fields = ['status', ]


    def create(self, validated_data):
        # Much more works are still left to be done.
        request = self.context.get("request")
        user = request.user

        # doctor_uid = self.context["request"].query_params.get("doctor_uid")

        # Standard way to get doctor UID
        doctor_uid = self.context["view"].kwargs["doctor_uid"]

        # Fetch the Doctor and Patient instances based on the UID
        try:
            doctor = Doctor.objects.get(uid=doctor_uid)

        except Doctor.DoesNotExist:
            raise serializers.ValidationError(
                "Doctor with the specified UID does not exist."
            )
        


        # Create the Appointment object with doctor, patient, and validated data
        appointment = Appointment.objects.create(
            doctor=doctor, patient=user, **validated_data
        )

        return appointment
"""


class CreateAppointmentForLabTestSerializer(serializers.Serializer):
    """Patient can create an appointment for lab test"""

    uid = serializers.CharField()
    slug = serializers.CharField()
    patient = serializers.UUIDField()
    organization = OrganizationSerializer()
    schedule_start = serializers.DateTimeField()
    schedule_end = serializers.DateTimeField()
    location = serializers.CharField()
    type = serializers.CharField()
    status = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        # Extract the labtest_uid from the URL's query parameters
        labtest_uid = request.query_params.get("uid")

        # request.

        # Fetch the LabTest instance based on the UID
        try:
            labtest = LabTest.objects.get(uid=labtest_uid)
        except LabTest.DoesNotExist:
            raise serializers.ValidationError(
                "LabTest with the specified UID does not exist."
            )

        # Create the Appointment object with doctor, patient, and validated data
        appointment = Appointment.objects.create(patient=user, **validated_data)

        # Establishing a relation with appointment and labtest
        LabTestAppointmentConnector.objects.create(
            appointment=appointment, labtest=labtest
        )

        return appointment
