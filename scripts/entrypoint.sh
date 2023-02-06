#!/bin/sh

python manage.py collectstatic --no-input
gunicorn snapy.wsgi:application --bind 0.0.0.0:8000

