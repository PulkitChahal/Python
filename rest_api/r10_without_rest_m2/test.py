import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id': id,
        }
    response = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(f'Response Code : {response.status_code}')
    print(response.json())


def create_resource():
    new_std = {
        'name': 'Mahesh',
        'rollno': 105,
        'marks': 81,
        'gf': 'Kareena',
        'bf': 'Prince'
    }
    response = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_std))
    print(f'Response Code : {response.status_code}')
    print(response.json())


def update_resource(id=None):
    new_data = {
        'id': id,
        'gf': 'Sakshi'
    }
    response = requests.put(BASE_URL + ENDPOINT, data=json.dumps(new_data))
    print(f'Response Code : {response.status_code}')
    print(response.json())


def delete_resource(id=None):
    data = {
        'id': id,
    }
    response = requests.delete(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(f'Response Code : {response.status_code}')
    print(response.json())


if __name__ == '__main__':
    print('#' * 60)

    # get_resource(30)
    # create_resource()
    # update_resource(4)
    delete_resource(4)

    print('#' * 60)
