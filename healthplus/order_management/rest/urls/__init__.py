from django.urls import path, include


urlpatterns = [
    path(r"", include("order_management.rest.urls.cart")),
    path(r"", include("order_management.rest.urls.orders")),
]
