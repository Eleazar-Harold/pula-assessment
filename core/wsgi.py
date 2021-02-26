"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application

from core import Cling, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = Cling(get_wsgi_application())
