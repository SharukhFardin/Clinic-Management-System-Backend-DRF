from django.urls import reverse

def create_patient_url():
    return reverse("health_support.medicine-list")