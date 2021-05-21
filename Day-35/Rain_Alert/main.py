import requests

API_KEY = "6554b41110709f2e4202dfe6a4d35e7d"

parameters = {
    "lat": -29.758459,
    "lon": -57.096020,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:11]
# print(weather_slice[0]["weather"][0]["id"])

for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Please bring an umbrella")


