import requests

API_KEY = "6554b41110709f2e4202dfe6a4d35e7d"

parameters = {
    "lat": 19.075983,
    "lon": 72.877655,
    "exclude": "minutely",
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data)