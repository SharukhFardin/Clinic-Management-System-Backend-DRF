from rest_framework import permissions
from organization.models import OrganizationUser, Patient, Doctor
from rest_framework.exceptions import PermissionDenied


class IsOrganizationMember(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        try:
            organization_user = OrganizationUser.objects.filter(user)
        except:
            raise PermissionDenied(
                "Only authenticated organization members have permission to access this"
            )

        return True


class IsPatient(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        try:
            patient = Patient.objects.filter(user)
        except:
            raise PermissionDenied("Only patients can access this")

        return True


class IsDoctor(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        try:
            doctor = Doctor.objects.filter(user)
        except:
            raise PermissionDenied("Only doctors can access this")

        return True
