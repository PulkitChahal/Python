import requests
import json

# Create your tests here.
base_url = 'http://127.0.0.1:8000/'
endpoint = 'emp/'

url = f'{base_url}{endpoint}'


def get_record(id=None):
    data = {}
    if id is not None:
        data = {'id': id, }
    json_data = json.dumps(data)
    r = requests.get(url, data=json_data)
    print(f'Response Code : {r.status_code}')
    data = r.json()
    print(data)


# get_record(1)
# get_record()


def post_record():
    data = {
        'name': 'rajni',
        'address': 'chennai',
        'mail': 'rajni@gmail.com',
        'age': 40
    }
    json_data = json.dumps(data)
    r = requests.post(url, data=json_data)
    data = r.json()
    print(data)


# post_record()


def update_record():
    data = {
        'id': 1,
        'name': 'pawan',
        'address': 'punjab',
        'mail': 'pawan@gmail.com',
        'age': 32
    }
    json_data = json.dumps(data)
    r = requests.put(url, data=json_data)
    data = r.json()
    print(data)

# update_record()