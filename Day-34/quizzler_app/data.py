import requests

parameters = {
    "amount": 10,
    "category": 9,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]
