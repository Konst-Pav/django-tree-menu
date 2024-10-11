#!/bin/bash

if ! [ -f ".env" ]; then
  cat .env.example > .env
fi

while IFS='=' read -r key value; do
	export "$key"="$value"
done < ".env"


python manage.py makemigrations
python manage.py migrate
python manage.py create_superuser
