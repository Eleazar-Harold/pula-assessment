#!/usr/bin/env bash
set -e
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate --noinput
exec gunicorn --bind=0.0.0.0:80 core.wsgi --workers=10 --log-level=info --log-file=---access-logfile=- --error-logfile=- --timeout 30000 --reload
