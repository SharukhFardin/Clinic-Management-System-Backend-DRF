from django.urls import path

from ..views.appointment import (
    CreateAppointmentForLabTestView,
    CreateAppointmentWithDoctorView,
)


urlpatterns = [
    path(
        r"appointment/doctors/<uuid:uid>",
        CreateAppointmentWithDoctorView.as_view(),
        name="create-appointment-with-doctor",
    ),
    path(
        r"appointment/labtests/<uuid:uid>",
        CreateAppointmentForLabTestView.as_view(),
        name="create-appointment-w",
    ),
]
