from core.settings.base import *

import string
import random

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
chars = (
    "".join([string.ascii_letters, string.digits, string.punctuation])
    .replace("'", "")
    .replace('"', "")
    .replace("\\", "")
)
SECRET_KEY = "".join([random.SystemRandom().choice(chars) for i in range(50)])

# SECURITY WARNING: don't run with debug turned on in production!
if config("PROD", cast=bool):
    DEBUG = False
    ALLOWED_HOSTS = []
else:
    DEBUG = True
    ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),  # os.environ['DB_NAME'],
        "USER": config("DB_USER"),  # os.environ['DB_USER'],
        "PASSWORD": config("DB_PSRD"),  # os.environ['DB_PSRD'],
        "HOST": config("DB_HOST"),  # os.environ['DB_HOST'],
        "PORT": config("DB_PORT"),  # os.environ['DB_PORT'],
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

CELERY_BROKER_URL = config("REDIS_URL")  # os.environ['REDIS_URL']
CELERY_RESULT_BACKEND = config("REDIS_URL")  # os.environ['REDIS_URL']
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
}
