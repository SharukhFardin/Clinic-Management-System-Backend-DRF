from django.urls import path

from ..views.we import OrganizationUserList, OrganizationList


urlpatterns = [
    path(
        r"/we/staffs",
        OrganizationUserList.as_view(),
        name="organization-user-list",
    ),
    path(
        r"/we",
        OrganizationList.as_view(),
        name="organization-list",
    ),
]
