from django.urls import path

from ..views.orders import OrderListView


urlpatterns = [
    path(
        r"/me/orders",
        OrderListView.as_view(),
        name="user-orders",
    ),
]
