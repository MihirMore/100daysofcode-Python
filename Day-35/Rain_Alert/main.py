import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "OWM_API_KEY"
account_sid = "Twilio account id"
auth_token = "Twilio auth token"

parameters = {
    "lat": 46.8150051,
    "lon": -101.829877,
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
print(weather_id)

for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"It's going to rain today. Remember to bring an umbrella. Weather id: {weather_id}",
        from_='twilio_number',
        to='my_number'
    )
    print(message.status)
