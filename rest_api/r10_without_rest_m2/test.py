import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'


def get_resource(id=None)
    data = {}
    if id is not None:
        data = {
            'id': id,
        }
    response = requests.get(BASE_URL + ENDPOINT, data=json.dumps(data))
    print(f'Response Code : {response.status_code}')
    print(response.json())


if __name__ == '__main__':
    print('#' * 60)

    get_resource(1)
