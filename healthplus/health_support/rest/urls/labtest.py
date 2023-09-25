from django.urls import path

from ..views.labtest import LabTestView


urlpatterns = [
    path(
        r"/me/labtests",
        LabTestView.as_view(),
        name="labtest-list",
    ),
]
