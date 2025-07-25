import os
import requests
from datetime import datetime

API_KEY = os.environ.get("api_key")
APP_ID = os.environ.get("app_id")
SHEETY_TOKEN = os.environ.get("sheety_token")
sheety_endpoint = "https://api.sheety.co/006e1efbc3067efc5d6911777a34fa02/workoutTracking/workouts"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# headers for authentication
headers_for_exercise = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_params = {
    "query": input("What exercise did you do today? "),
    "age": 18,
    "gender": "male",
    "weight_kg": 58,
    "height_cm": 168,
}

response = requests.post(exercise_endpoint, json=user_params, headers=headers_for_exercise)
workout_data = response.json()

# adding row data in the google sheets
today = datetime.now()
date = today.strftime("%Y/%m/%d")
time = today.strftime("%X")


# headers for authentication
headers_for_sheety = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

for exercise in workout_data["exercises"]: # returns a list that I can loop through
    row_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response_sheety = requests.post(sheety_endpoint, json=row_params, headers=headers_for_sheety)
    print(response_sheety.text)
