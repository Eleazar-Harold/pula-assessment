#!/usr/bin/env bash
set -e
docker-compose -f stack-dev.yml build
docker-compose -f stack-dev.yml run app python manage.py test
docker-compose -f stack-dev.yml down # Remove possibly previous broken stacks left hanging after an error
docker-compose -f stack-dev.yml up