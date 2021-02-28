from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


def base_exception_handler(exc, context):
    response = exception_handler(exc, context)

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
