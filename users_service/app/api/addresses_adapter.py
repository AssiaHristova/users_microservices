import json
import os

import httpx

ADDRESSES_SERVICE_HOST_URL = 'http://localhost:8002/all/'
url = os.environ.get('ADDRESSES_SERVICE_HOST_URL') or ADDRESSES_SERVICE_HOST_URL


def get_user_addresses(user_id: int):
    response = httpx.get(f'{url}{user_id}')
    return json.loads(response.text)


def create_address(user_id: int):
    pass