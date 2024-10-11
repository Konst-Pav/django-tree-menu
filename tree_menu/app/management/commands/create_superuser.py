import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


UserModel = get_user_model()

SUPERUSER_USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME')
SUPERUSER_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL')
SUPERUSER_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD')


class Command(BaseCommand):
    help = 'Creates a superuser when the application is launched'

    _class = UserModel

    def handle(self, *args, **options):
        self._class.objects.create_superuser(
            SUPERUSER_USERNAME,
            SUPERUSER_EMAIL,
            SUPERUSER_PASSWORD,
        )
