#!/bin/bash

ENV_FILE=.env

if ! [ -f "$ENV_FILE" ]; then
  cat .env.example > $ENV_FILE
fi

while IFS='=' read -r key value; do
	export "$key"="$value"
done < "$ENV_FILE"


python manage.py makemigrations
python manage.py migrate
python manage.py create_superuser
