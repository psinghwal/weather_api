from django.db import models

class CityWeather(models.Model):
    city = models.CharField(max_length=100, unique=True)
    temperature = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city}: {self.temperature}°C"
