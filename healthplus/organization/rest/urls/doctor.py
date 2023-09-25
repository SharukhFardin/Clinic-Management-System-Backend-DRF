from django.urls import path

from ..views.doctor import DoctorList, DoctorDetail, DoctorRegistration


urlpatterns = [
    path(
        r"/we/doctors",
        DoctorList.as_view(),
        name="doctor-list",
    ),
    path(
        r"/we/doctors/<uuid:uid>",
        DoctorDetail.as_view(),
        name="doctor-detail",
    ),
    path(
        r"/me/doctor/organizations/<uuid:uid>/register",
        DoctorRegistration.as_view(),
        name="doctor-registration",
    ),
]
