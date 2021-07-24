import requests
from datetime import datetime
import os


today = datetime.now()
now_time = today.strftime("%X")
today_formatted = today.strftime("%d/%m/%Y")

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
AUTH_TOKEN_SHEETY = os.environ["AUTH_TOKEN_SHEETY"]
sheety_headers = {"Authorization": f"Bearer {AUTH_TOKEN_SHEETY}"}

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/e51125c3926939b4cba8b276d19b4fce/kopieVonMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {"x-app-id": APP_ID,
           "x-app-key": APP_KEY
           }

parameters = {"query": exercise_text,
              "gender": "male",
              "weight_kg": 80,
              "height_cm": 175,
              "age": 25}

response = requests.post(url=nutrition_endpoint, json=parameters, headers=headers)
result = response.json()["exercises"]
activity_kind = result[0]["name"]
activity_calories = result[0]["nf_calories"]
activity_duration = result[0]["duration_min"]


row_parameters = {"workout": {"date": today_formatted,
                              "time": now_time,
                              "exercise": activity_kind,
                              "duration": str(activity_duration),
                              "calories": activity_calories
                              }}


response_sheety = requests.post(url=sheety_endpoint, json=row_parameters, headers=sheety_headers)
response_sheety.raise_for_status()
print(response_sheety)
