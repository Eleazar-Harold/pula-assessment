from django.http import JsonResponse

from rest_framework.exceptions import (
    ValidationError,
)
from rest_framework.views import exception_handler


def handle_auth_error(exc, context, response):
    response.data = {"error": "authorization token required to handle this request."}
    return response


def handle_generic_error(exc, context, response):
    if isinstance(exc, ValidationError):
        if response.data.get("username", None):
            response.data = response.data["username"][0]
        elif response.data.get("password", None):
            response.data = response.data["password"][0]
        elif response.data.get("email", None):
            response.data = response.data["email"][0]
        elif response.data.get("last_name", None):
            response.data = response.data["last_name"][0]
        elif response.data.get("first_name", None):
            response.data = response.data["first_name"][0]
        elif response.data.get("name", None):
            response.data = response.data["name"][0]
        elif response.data.get("size", None):
            response.data = response.data["size"][0]
        elif response.data.get("crop", None):
            response.data = response.data["crop"][0]
        elif response.data.get("town", None):
            response.data = response.data["town"][0]
        elif response.data.get("owner", None):
            response.data = response.data["owner"][0]
        elif response.data.get("harvest_weight", None):
            response.data = response.data["harvest_weight"][0]
        elif response.data.get("dry_weight", None):
            response.data = response.data["dry_weight"][0]
        elif response.data.get("farm", None):
            response.data = response.data["farm"][0]
        elif response.data.get("image", None):
            response.data = response.data["image"][0]
        elif response.data.get("harvest", None):
            response.data = response.data["harvest"][0]

    return response


def base_exception_handler(exc, context):
    handlers = {
        "ValidationError": handle_generic_error,
        "Http404": handle_generic_error,
        "PermissionDenied": handle_generic_error,
        "NotAuthenticated": handle_auth_error,
    }
    response = exception_handler(exc, context)
    exception = exc.__class__.__name__

    if exception in handlers:
        return handlers[exception](exc, context, response)
    return response


def error404(request):
    message = "The endpoint does not exist"
    response = JsonResponse(
        data={
            "message": message,
            "status_code": 404,
        }
    )
    return response


def error500(request):
    message = "This error is on us, we'll get back to you after resolving it."
    response = JsonResponse(
        data={
            "message": message,
            "status_code": 500,
        }
    )
    return response
