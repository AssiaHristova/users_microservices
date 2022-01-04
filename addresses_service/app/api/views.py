from typing import List

from fastapi import APIRouter, HTTPException

from addresses_service.app.api.models import AddressOut, AddressIn, AddressUpdate
from addresses_service.app.api import db_manager


addresses = APIRouter()


@addresses.get('/')
async def home():
    return "Hello Addresses"


@addresses.get('/all', response_model=List[AddressOut])
async def get_all_addresses():
    return await db_manager.get_all_addresses()


@addresses.get("/all/{user_id}", response_model=List[AddressOut])
async def get_user_addresses(user_id: int):
    return await db_manager.get_user_addresses(user_id)


@addresses.post('/', response_model=AddressOut, status_code=201)
async def create_address(address: AddressIn):
    address_id = await db_manager.add_address(address)
    response = {
        'id': address_id,
        **address.dict()
        }
    return response


@addresses.get('/{id}/', response_model=AddressOut)
async def get_address(id: int):
    address = await db_manager.get_address(id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@addresses.put('/{id}/', response_model=AddressOut)
async def update_address(id: int, payload: AddressUpdate):
    address = await db_manager.get_address(id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    update_data = payload.dict(exclude_unset=True)
    address_in_db = AddressIn(**address)
    updated_address = address_in_db.copy(update=update_data)
    return await db_manager.update_address(id, updated_address)


@addresses.delete('/{id}', response_model=None)
async def delete_address(id: int):
    address = await db_manager.get_address(id)
    if not address:
        raise HTTPException(status_code=404, detail="User not found")
    return await db_manager.delete_address(id)
