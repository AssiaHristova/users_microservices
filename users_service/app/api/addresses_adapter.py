import json
import os

import httpx
import requests

from addresses_service.app.api.models import AddressIn

ADDRESSES_SERVICE_HOST_URL = 'http://localhost:8002/'
url = os.environ.get('ADDRESSES_SERVICE_HOST_URL') or ADDRESSES_SERVICE_HOST_URL


def get_user_addresses(user_id: int):
    response = httpx.get(f'{url}all/{user_id}')
    return json.loads(response.text)


def create_addresses(addresses: list[AddressIn]):
    for address in addresses:
        response = httpx.post(url, json=address.dict())
        return response.status_code
