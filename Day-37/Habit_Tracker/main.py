import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = "hwbehcvabefb&#$%^janwd"

user_params = {
    "token": PIXELA_TOKEN,
    "username": "mihirqd6345",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)
