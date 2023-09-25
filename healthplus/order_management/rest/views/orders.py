from django.shortcuts import get_object_or_404

from rest_framework import generics

from order_management.models import Order
from ..serializers.orders import OrderSerializer


class OrderListView(generics.ListAPIView):
    """Logged In Patient can view his Orders"""

    queryset = Order.objects.filter()
    permission_classes = []
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user)
