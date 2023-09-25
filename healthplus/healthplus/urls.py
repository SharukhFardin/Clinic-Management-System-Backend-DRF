from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from schema_graph.views import Schema

urlpatterns = [
    path("staff/", admin.site.urls),
    # organization app
    path("api", include("organization.rest.urls")),
    # health_support app
    path("api", include("health_support.rest.urls")),
    # order_management app
    path("api", include("order_management.rest.urls")),
    # swagger urls
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # For generating model graph
    path("schema", Schema.as_view()),
    # JWT api urls
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Django Silk
    path("silk", include("silk.urls", namespace="silk")),
]

# urlpatterns += patterns('', url(r'^silk', include('silk.urls', namespace='silk')))
