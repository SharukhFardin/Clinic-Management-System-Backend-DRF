from django.urls import path

from ..views.medicine import MedicineView, MedicineList


urlpatterns = [
    path(
        r"/we/medicines",
        MedicineView.as_view(),
        name="medicine-list",
    ),
    path(
        r"/we/medicines/<uuid:uid>",
        MedicineList.as_view(),
        name="medicine-details",
    ),
]
