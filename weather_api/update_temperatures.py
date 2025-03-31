import requests
from .models import CityWeather
from .key import api_key  # Create this file with your API key

cities = ["Dublin", "London", "Paris", "New York", "Berlin","Delhi","Mumbai"]

def fetch_and_update_weather():
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(url).json()
        temperature = response["main"]["temp"]

        CityWeather.objects.update_or_create(
            city=city,
            defaults={"temperature": temperature}
        )
