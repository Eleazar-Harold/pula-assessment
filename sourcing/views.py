from django.contrib.auth.models import User

from rest_framework import filters, viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from sourcing.models import Farm, Harvest, Resource
from sourcing.serializer import (
    FarmSerializer,
    HarvestSerializer,
    ResourceSerializer,
    RegistrationSerializer,
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


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = "username"
    serializer_class = RegistrationSerializer
    queryset = User.objects.none()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {
                "token": token.key,
                "user": UserSerializer(
                    serializer.data, context=self.get_serializer_context()
                ).data,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
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

    @detail_route(methods=["get"])
    def harvests(self, request, pk=None):
        queryset = Harvest.objects.filter(farm__pk=pk).order_by("-created")
        context = {"request": request}
        serializer = HarvestSerializer(queryset, context=context, many=True)

        return Response(serializer.data)


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

    @detail_route(methods=["get"])
    def resources(self, request, pk=None):
        queryset = Resource.objects.filter(harvest__pk=pk).order_by("-created")
        context = {"request": request}
        serializer = ResourceSerializer(queryset, context=context, many=True)

        return Response(serializer.data)


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
