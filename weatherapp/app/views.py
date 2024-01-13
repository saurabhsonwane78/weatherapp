from django.http import JsonResponse
from django.views.decorators.http import require_GET
import requests
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


OPEN_METEO_API_URL = "https://api.open-meteo.com/v1/forecast"

@api_view(["GET"])
@csrf_exempt
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_historic_weather(request):
    try:
        # Get parameters from the request
        latitude = float(request.GET.get('latitude'))
        longitude = float(request.GET.get('longitude'))
        days_ago = int(request.GET.get('numberofdays'))

        # Calculate the date 'days_ago' days ago from today
        start_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
        end_date=datetime.now().strftime('%Y-%m-%d')

        # Make a request to Open Meteo API for historic weather data
        api_endpoint = f"{OPEN_METEO_API_URL}?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m&relative_humidity_2m,wind_speed_10m"
        response = requests.get(api_endpoint)
        weather_data = response.json()
        return JsonResponse(weather_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
