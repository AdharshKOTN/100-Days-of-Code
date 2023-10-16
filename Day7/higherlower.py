import requests
from dotenv import load_dotenv
import os

load_dotenv()

print(
    f"""  /\  /(_) __ _| |__   ___ _ __ 
 / /_/ / |/ _` | '_ \ / _ \ '__|
/ __  /| | (_| | | | |  __/ |   
\/ /_/ |_|\__, |_| |_|\___|_|   
          |___/                 
   __                           
  / /  _____      _____ _ __    
 / /  / _ \ \ /\ / / _ \ '__|   
/ /__| (_) \ V  V /  __/ |      
\____/\___/ \_/\_/ \___|_|  """
)

client_id = os.getenv("CLIENT_ID")
api_secret = os.getenv("API_SECRET")

# Define your access token here
access_token = os.getenv("I_TOKEN")
user_id = "vineetaaaah"

# Define the endpoint to get your media
endpoint = f"https://graph.instagram.com/v12.0/{user_id}/media"

# Define parameters for the request
params = {
    "fields": "id",
    "access_token": access_token,
}

# Make the API request
response = requests.get(endpoint, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    for media in data["data"]:
        print(media)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")

# url = "https://api.instagram.com/oauth/authorize"
# body = {
#     "client_id": "{client_id}",
#     "client_secret": "{api_secret}",
#     "code": "",
#     "grant_type": "",
#     "redirect_uri": "",
# }
# req = requests.post(url)
