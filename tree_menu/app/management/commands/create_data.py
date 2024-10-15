import os

from django.core.management.base import BaseCommand
from django.core.serializers import deserialize
from dotenv import load_dotenv


load_dotenv()

FIXTURE_FILE = os.getenv('FIXTURE_FILE')


class Command(BaseCommand):
    help = 'Creates data for an example'

    def handle(self, *args, **options):
        with open(FIXTURE_FILE, "r") as data:
            for deserialized_object in deserialize("json", data):
                deserialized_object.save()
