import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = "63"
HEIGHT_CM = "158"
AGE = "22"

APP_ID="b532e230"
API_KEY="a4fa427ee5a5b2bb72f8975e960f2aed"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint ="https://api.sheety.co/8a4f24f1d409b942bb693e6f0abceced/exercise/sheet1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_token={
        "Authorization":"Basic Z3VyYW1yaXRwYW5kaGVyOmxvdmV1ZGFkZHU="
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs,headers=bearer_token)

    print(sheet_response.text)


