#!/usr/bin/env bash
celery -A core worker -c 5 -l info
celery -A core beat -l info