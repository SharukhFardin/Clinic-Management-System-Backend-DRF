from django.db import models
from organization.models import User
from core.models import CustomBaseModel
from health_support.models import LabTest, Medicine
import uuid

from .choices import *


# Order model for managing orders
class Order(CustomBaseModel):
    name = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Models to define the items in an Order
class OrderItem(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    medicine = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, null=True, blank=True
    )
    labtest = models.ForeignKey(
        LabTest, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.PositiveIntegerField()


# Cart Model for users
class Cart(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# CartItem model
class CartItem(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    medicine = models.ForeignKey(
        Medicine, on_delete=models.CASCADE, null=True, blank=True
    )
    labtest = models.ForeignKey(
        LabTest, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity


# This model will store delivary status
class DeliveryStatus(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=DelivaryStatusChoices.choices, default="Pending"
    )
    updated_at = models.DateTimeField(auto_now=True)
