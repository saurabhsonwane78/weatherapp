from django.urls import include, path
from . import views

urlpatterns = [
    path('historic-weather/', views.get_historic_weather, name='get_historic_weather'),
]