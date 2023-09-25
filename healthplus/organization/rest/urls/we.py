from django.urls import path

from ..views.we import OrganizationUserList


urlpatterns = [
    path(
        r"/we/staffs",
        OrganizationUserList.as_view(),
        name="organization-user-list",
    ),
]
