import os
from typing import List

import httpx
from pydantic import BaseModel

USERS_SERVICE_HOST_URL = 'http://localhost:8081/users/'
url = os.environ.get('USERS_SERVICE_HOST_URL') or USERS_SERVICE_HOST_URL


def is_user_present(user_id: int):
    r = httpx.get(f'{url}{user_id}')
    return True if r.status_code == 200 else False


class Address(BaseModel):
    id: int
    user_id: int
    address: str


class UserFilter(BaseModel):
    user_id: int
    user_addresses: List[Address]


class AddressesStorage:
    def add_user_address(self, user_id, address):
        if is_user_present(user_id):
            return UserFilter.user_addresses.insert(address, user_id)

    def get_user_addresses(self, filters: UserFilter) -> List[Address]:
        return UserFilter.user_addresses


class UserAddressesList:
    def __init__(self, repo: AddressesStorage):
        self.repo = repo

    def show_user_addresses(self, filters: UserFilter) -> List[Address]:
        user_addresses = self.repo.get_user_addresses(filters=filters)
        return user_addresses

    def add_user_address(self, user_id, address):
        return self.repo.add_user_address(user_id, address)
