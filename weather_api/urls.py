from django.urls import path
from .views import  get_all_weather
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    path('weather/', get_all_weather, name="get_all_weather"),
    # path('social_links', views.social_links),
]
