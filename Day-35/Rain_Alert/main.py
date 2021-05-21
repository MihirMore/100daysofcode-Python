import requests

API_KEY = "6554b41110709f2e4202dfe6a4d35e7d"

parameters = {
    "lat": 19.075983,
    "lon": 72.877655,
    "exclude": "current,minutely,hourly",
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

