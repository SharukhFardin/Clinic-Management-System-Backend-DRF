from rest_framework import permissions
from organization.models import OrganizationUser
from rest_framework.exceptions import PermissionDenied


class IsOrganizationMember(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        try:
            organization_user = OrganizationUser.objects.filter(user)
        except:
            raise PermissionDenied("Only authenticated organization members have permission to access this")

        return True