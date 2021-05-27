from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "YOUR URL"
SHEETY_USERS_ENDPOINT = "YOUR URL"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

    def update_customer_emails(self, f_name, l_name, email):
        parameters = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=parameters)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
