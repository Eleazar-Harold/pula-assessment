from django.urls import include, path, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import routers
from rest_framework import permissions

from sourcing.views import (
    FarmViewSet,
    HarvestViewSet,
    LoginViewSet,
    ResourceViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register("v1/authtoken/generate", UserViewSet, basename="generate_auth_token")
router.register("v1/authtoken/obtain", LoginViewSet, basename="obtain_auth_token")
router.register("v1/farm", FarmViewSet, basename="farms")
router.register("v1/harvest", HarvestViewSet, basename="harvests")
router.register("v1/resource", ResourceViewSet, basename="resources")

router.get_api_root_view().cls.__name__ = "Sourcing API"
router.get_api_root_view().cls.__doc__ = (
    "This is a central sourcing API."
    " Meant to handle all requests in regarding to sourcing requests."
)

schema_view = get_schema_view(
   openapi.Info(
      title="Sourcing API",
      default_version='v1',
      description="This API allows us to handle all sourcing requests",
      contact=openapi.Contact(email="eleazar.yewa.harold@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
