#!/bin/bash

if ! [ -f ".env" ]; then
  cat .env.example > .env
fi

python manage.py makemigrations
python manage.py migrate
python manage.py create_superuser
