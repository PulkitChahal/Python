import json

import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api_data/'


def get_resource():
    id = '2'
    response = requests.get(BASE_URL + ENDPOINT + id + '/')
    print(f'Response Code : {response.status_code}')
    data = response.json()
    print(data)


def get_all():
    response = requests.get(BASE_URL + ENDPOINT)
    print(f'Response Code : {response.status_code}')
    data = response.json()
    print(data)


def create_resource():
    new_emp = {
        'eno': 600,
        'ename': 'Mandy',
        'esal': 30000,
        'eaddr': 'Pune',
    }
    response = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(f'Response Code : {response.status_code}')
    print(response.json())


def update_resource(id):
    new_emp = {
        # 'eno': 600,
        'ename': 'Candy',
        'esal': 40000,
        # 'eaddr': 'Pune',
    }
    response = requests.put(BASE_URL + ENDPOINT + str(id) + '/', data=json.dumps(new_emp))
    print(f'Response Code : {response.status_code}')
    print(response.json())


def delete_resource(id):
    response = requests.delete(BASE_URL + ENDPOINT + str(id) + '/')
    print(f'Response Code : {response.status_code}')
    print(response.json())


def get_resource_2():
    data = {}
    if id is not None:
        data = {
            'id': id,
        }
    response = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(f'Response Code : {response.status_code}')
    data = response.json()
    print(data)


if __name__ == '__main__':
    print('#' * 60)

    # get_resource()
    # get_all()
    # create_resource()
    # update_resource('2')
    # delete_resource('2')
    get_resource_2()

    print('#' * 60)
