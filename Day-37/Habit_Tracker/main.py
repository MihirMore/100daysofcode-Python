import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = "your_token"
USERNAME = "your_username"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# API call to create user
user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(user_response.text)

# API call to create graph for habit
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)

UPDATE_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

update_pixel = {
    "date": "20210524",
    "quantity": "300"
}

response = requests.post(url=UPDATE_GRAPH_ENDPOINT, json=update_pixel, headers=headers)
print(response.text)