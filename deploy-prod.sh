#!/usr/bin/env bash
set -e
docker-compose -f stack-prod.yml build
docker-compose -f stack-prod.yml down # Remove possibly previous broken stacks left hanging after an error
docker-compose -f stack-prod.yml up