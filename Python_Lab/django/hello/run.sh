#!/bin/bash

python manage.py runserver 0.0.0.0:8008
# # celery beat -A celery_app.crontasks -l=info &
# # celery worker -A celery_app.crontasks -l=info
cd celery_app && celery worker -A app -l=info