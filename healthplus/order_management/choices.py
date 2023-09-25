from django.db import models


class DelivaryStatusChoices(models.TextChoices):
    PENDING = "PENDIN", "Pending"
    IN_TRANSIT = "IN_TRANSIT", "In_Transit"
    DELIVERED = "DELIVERED", "Delivered"
    FAILED = "FAILED", "Failed"
    COMPLETED = "COMPLETED", "Completed"
