#!/bin/bash

python manage.py makemigrations
python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser --noinput
fi
