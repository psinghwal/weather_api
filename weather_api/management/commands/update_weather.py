from django.core.management.base import BaseCommand
from weather_api.update_temperatures import fetch_and_update_weather

class Command(BaseCommand):
    help = "Fetch and update temperatures for all cities"

    def handle(self, *args, **kwargs):
        fetch_and_update_weather()
        self.stdout.write(self.style.SUCCESS("✅ Weather data updated successfully."))
