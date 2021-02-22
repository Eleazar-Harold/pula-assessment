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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("PG_DB"),
        "USER": config("PG_USER"),
        "PASSWORD": config("PG_PASSWORD"),
        "HOST": config("RDS_HOST"),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
AWS_ACCESS_KEY_ID = "aws_s3_access_key_id"
AWS_SECRET_ACCESS_KEY = "aws_s3_secret_access_key"
AWS_STORAGE_BUCKET_NAME = ""
AWS_S3_CUSTOM_DOMAIN = ""
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = ""
AWS_DEFAULT_ACL = None

STATIC_URL = ""
STATICFILES_STORAGE = ""

CELERY_BROKER_URL = config("REDIS_URL")
CELERY_RESULT_BACKEND = config("REDIS_URL")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",  # <-- And here
    ],
}
