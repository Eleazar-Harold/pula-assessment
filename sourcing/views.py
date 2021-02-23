from django.contrib.auth.models import User
from django.shortcuts import (
    get_object_or_404,
    render,
)


from rest_framework import (
    viewsets,
    status,
    filters,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from rest_framework.authtoken.models import Token
from sourcing.models import (
    Farm,
    Harvest,
    Resource,
)
from sourcing.serializer import (
    UserSerializer,
    FarmSerializer,
    HarvestSerializer,
    ResourceSerializer,
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

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


"""
class that creates, updates and gets farms against api-key/auth-token for use by other services
"""


class FarmViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = FarmSerializer
    queryset = Farm.objects.none()
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "name",
        "crop",
        "town",
        "farms",
    )

    def list(self, request):
        queryset = Farm.objects.all()
        serializer = FarmSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        queryset = Farm.objects.all()
        farm = get_object_or_404(queryset, pk=pk)
        serializer = FarmSerializer(farm)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


"""
class that creates, updates and gets harvests against api-key/auth-token for use by other services
"""


class HarvestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = HarvestSerializer
    queryset = Harvest.objects.none()
    filter_backends = (filters.SearchFilter,)

    def list(self, request):
        queryset = Harvest.objects.all()
        serializer = HarvestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        queryset = Harvest.objects.all()
        harvest = get_object_or_404(queryset, pk=pk)
        serializer = HarvestSerializer(farm)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
