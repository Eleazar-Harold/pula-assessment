from django.urls import path, include
from rest_framework import routers

from sourcing.views import (
    LoginViewSet,
    UserViewSet,
)


router = routers.DefaultRouter()
router.register("v1/authtoken/generate", UserViewSet, base_name="generate_auth_token")
router.register("v1/authtoken/obtain", LoginViewSet, base_name="obtain_auth_token")


router.get_api_root_view().cls.__name__ = "Sourcing API"
router.get_api_root_view().cls.__doc__ = (
    "This is a central sourcing API."
    "Meant to handle all requests in regarding to sourcing requests."
)

urlpatterns = [
    path("", include(router.urls)),
]
