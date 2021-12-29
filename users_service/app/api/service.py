import json
import os
import httpx
from typing import Optional, List
from pydantic import BaseModel

from users_service.app.api import db_manager

ADDRESSES_SERVICE_HOST_URL = 'http://localhost:8002/all/'
url = os.environ.get('ADDRESSES_SERVICE_HOST_URL') or ADDRESSES_SERVICE_HOST_URL


def is_address_present(address_id: int):
    r = httpx.get(f'{url}{address_id}')
    return True if r.status_code == 200 else False









