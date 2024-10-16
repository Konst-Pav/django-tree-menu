import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from dotenv import load_dotenv

load_dotenv()

UserModel = get_user_model()

SUPERUSER_USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME', default='admin')
SUPERUSER_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL', default='admin@admin.mail')
SUPERUSER_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD', default='admin')


class Command(BaseCommand):
    help = 'Creates a superuser when the application is launched'

    _class = UserModel

    def handle(self, *args, **options):
        self._class.objects.create_superuser(
            username=SUPERUSER_USERNAME,
            email=SUPERUSER_EMAIL,
            password=SUPERUSER_PASSWORD,
        )
