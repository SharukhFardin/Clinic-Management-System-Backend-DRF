from django.shortcuts import get_object_or_404

from rest_framework import generics

from ..serializers.cart import CartManagementSerializer, CartSerializer


class CartManagementView(generics.CreateAPIView):
    """Create or view list for all the organization doctors for ogranization users"""

    permission_classes = []
    serializer_class = CartManagementSerializer

    def get_queryset(self):
        user = self.request.user
        organization = user.OrganizationUser_set.first().organization
        return self.queryset.filter(organization)


class CartDelete(generics.DestroyAPIView):
    "User can delete it's cart"

    permission_classes = []
    serializer_class = CartSerializer
    lookup_field = "uid"
