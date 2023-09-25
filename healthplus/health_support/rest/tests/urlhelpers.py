from django.urls import reverse


def medicine_list_url():
    return reverse("health_support.medicine-list")