#!/bin/bash

if ! [ -f ".env" ]; then
  cat .env.example > .env
fi

python tree_menu/manage.py makemigrations
python tree_menu/manage.py migrate
python tree_menu/manage.py create_superuser
python tree_menu/manage.py collectstatic --no-input
