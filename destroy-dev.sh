#!/usr/bin/env bash
set -e
docker-compose -f stack-dev.yml down -v --rmi local