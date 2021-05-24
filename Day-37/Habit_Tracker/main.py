import requests
from datetime import datetime

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

# API call to create pixel in our graph
CREATE_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

today = datetime.now()

create_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "300"
}

response = requests.post(url=CREATE_GRAPH_ENDPOINT, json=create_pixel, headers=headers)
print(response.text)

# API call to update your pixels
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/20210523"

update_pixel = {
    "quantity": "330"
}

response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel, headers=headers)
print(response.text)

# API call to delete pixels in our graph
DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/20210523"

response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
print(response.text)


