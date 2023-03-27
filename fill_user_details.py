import requests
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY_USERS_ENDPOINT = os.getenv('SHEETY_USERS_ENDPOINT')
SHEETY_USERNAME = os.getenv('SHEETY_USERNAME')
SHEETY_PASSWORD = os.getenv('SHEETY_PASSWORD')

print("Welcome to Siddharth's Flight Club.")
print("We find the best flight deals and email you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")

while input("Enter your email again.\n") != email:
    print("Email ID don't match. Please check if you have entered your email correctly.")

query = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}

response = requests.put(url=SHEETY_USERS_ENDPOINT, json=query, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
print(response.text)
