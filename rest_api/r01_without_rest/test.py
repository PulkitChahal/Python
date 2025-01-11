import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijson2/'

response = requests.get(BASE_URL+ENDPOINT)
print(response.json())