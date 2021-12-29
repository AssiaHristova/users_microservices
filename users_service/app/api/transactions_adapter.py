import json
import os

import httpx

TRANSACTION_SERVICE_HOST_URL = 'http://localhost:8003/all/'
url = os.environ.get('TRANSACTION_SERVICE_HOST_URL') or TRANSACTION_SERVICE_HOST_URL


def get_user_transactions(user_id: int):
    response = httpx.get(f'{url}{user_id}')
    return json.loads(response.text)

