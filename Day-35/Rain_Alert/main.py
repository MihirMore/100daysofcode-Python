import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "6554b41110709f2e4202dfe6a4d35e7d"
account_sid = "AC446baf82e5cca3dbae630af5116cd96a"
auth_token = "ad9ddf0446645abac71122180526b9e8"

parameters = {
    "lat": 46.811131,
    "lon": -101.832603,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:11]
weather_id = weather_slice[0]["weather"][0]["id"]

for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"It's going to rain today. Remember to bring an umbrella. Weather id: {weather_id}",
        from_='+16503977270',
        to='+91 90824 90234'
    )
    print(message.status)
