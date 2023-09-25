from django.urls import path

from ..views.patient import *


urlpatterns = [
    path(
        r"/me/patient/register",
        PatientRegistration.as_view(),
        name="patient-registration",
    ),
    path(
        r"/we/patients/<uuid:uid>",
        PatientList.as_view(),
        name="patient-detail",
    ),
    path(
        r"/we/patients/<uuid:uid>",
        PatientDetail.as_view(),
        name="patient-list",
    ),
]
