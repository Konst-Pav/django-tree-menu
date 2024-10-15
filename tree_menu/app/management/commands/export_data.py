from django.core import serializers
from django.core.management.base import BaseCommand
from app.models import Menu


class Command(BaseCommand):
    help = 'Export data for an example'

    def handle(self, *args, **options):
        data = serializers.serialize("json", Menu.objects.all())
        with open("menu_data_example.json", "w") as out:
            out.write(data)
