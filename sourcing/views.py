from django.contrib.auth.models import User

from rest_framework import filters, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from sourcing.models import Farm, Harvest, Resource
from sourcing.serializer import (
    FarmSerializer,
    HarvestSerializer,
    ResourceSerializer,
    UserSerializer,
)

# Create your views here.


"""
class that user logs in to to acquire their api-key/auth-token
"""


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""
        return ObtainAuthToken().post(request)


"""
class that registers user to get api-key/auth-token for use by other services
"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "username",
        "email",
        "last_name",
        "first_name",
    )
    serializer_class = UserSerializer

    """overrides serializer create to generate api-key/auth-token"""

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {"token": token.key}, status=status.HTTP_201_CREATED, headers=headers
        )


"""
class that creates, updates and gets farms against
api-key/auth-token for use by other services
"""


class FarmViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
    )
    authentication_classes = (TokenAuthentication,)
    serializer_class = FarmSerializer
    queryset = Farm.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "name",
        "size",
        "crop",
        "town",
        "owner__username",
        "owner__last_name",
        "owner__first_name",
        "id",
    )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)


"""
class that creates, updates and gets harvests against
api-key/auth-token for use by other services
"""


class HarvestViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
    )
    authentication_classes = (TokenAuthentication,)
    serializer_class = HarvestSerializer
    queryset = Harvest.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "harvest_weight",
        "dry_weight",
        "farm__name",
        "farm__owner__username",
        "farm__owner__last_name",
        "farm__owner__first_name",
        "id",
    )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)


"""
class that creates, updates and gets resources against
api-key/auth-token for use by other services
"""


class ResourceViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsAuthenticatedOrReadOnly,
    )
    authentication_classes = (TokenAuthentication,)
    serializer_class = ResourceSerializer
    queryset = Resource.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "name",
        "image",
        "harvest__farm__name",
        "id",
    )

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)
