from django.urls import path, include
from rest_framework import routers

from sourcing.views import (
    LoginViewSet,
    UserViewSet,
    FarmViewSet,
    HarvestViewSet,
    ResourceViewSet,
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
    "Meant to handle all requests in regarding to sourcing requests."
)

urlpatterns = [
    path("", include(router.urls)),
]
