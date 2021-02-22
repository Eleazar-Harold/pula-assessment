from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authtoken.models import Token

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
