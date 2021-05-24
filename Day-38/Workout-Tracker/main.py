import requests
from datetime import datetime

APP_ID = "your_app_id"
APP_KEY = "your_app_key"
SHEETY_ENDPOINT = "your_sheety_url"

GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 178
AGE = 23

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

user_workout_details = input("What workout did you do? ")

EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
    "query": user_workout_details,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_URL, json=exercise_config, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


bearer_header = {
    "Authorization": "your_TOKEN"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_header)
    print(sheet_response.text)