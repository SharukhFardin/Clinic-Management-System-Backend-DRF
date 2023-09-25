from django.urls import path, include


urlpatterns = [
    path(r"/me/", include("health_support.rest.urls.appointment")),
    path(r"", include("health_support.rest.urls.medicine")),
    path(r"", include("health_support.rest.urls.labtest")),
]
