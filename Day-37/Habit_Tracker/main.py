import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = "your generated token"

user_params = {
    "token": PIXELA_TOKEN,
    "username": "your_id",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)
