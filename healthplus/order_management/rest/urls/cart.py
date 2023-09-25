from django.urls import path

from ..views.cart import CartManagementView, CartDelete


urlpatterns = [
    path(
        r"/me/cart/items",
        CartManagementView.as_view(),
        name="user-cart",
    ),
    path(
        r"/me/cart/<uuid:uid>",
        CartDelete.as_view(),
        name="user-cart-delete",
    ),
]
