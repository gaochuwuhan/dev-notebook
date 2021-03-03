#!/bin/bash

python manage.py runserver &
# celery beat -A celery_app.crontasks -l=info &
# celery worker -A celery_app.crontasks -l=info
cd celery_app && celery worker -A app -l=info