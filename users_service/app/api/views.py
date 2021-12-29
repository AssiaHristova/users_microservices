import json
from typing import List
from fastapi import APIRouter, HTTPException

from users_service.app.api.models import UserOut, UserIn, UserUpdate, UserDTOCls
from users_service.app.api import db_manager
from users_service.app.api.addresses_adapter import get_user_addresses
from users_service.app.api.transactions_adapter import get_user_transactions
from users_service.app.api.models import UserDTO

users = APIRouter()


@users.post('/', response_model=UserOut, status_code=201)
async def create_user(payload: UserIn):
    user_id = await db_manager.add_user(payload)
    response = {
        'id': user_id,
        **payload.dict()
    }
    return response


@users.get('/', response_model=List[UserOut])
async def get_all_users():
    return await db_manager.get_all_users()


@users.get('/{id}/')
async def get_user(id: int):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_addresses = get_user_addresses(id)
    user_transactions = get_user_transactions(id)
    results = {"user": user, "addresses": user_addresses, "transactions": user_transactions}
    return results


@users.put('/{id}/', response_model=UserOut)
async def update_user(id: int, payload: UserUpdate):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = payload.dict(exclude_unset=True)
    user_in_db = UserIn(**user)
    updated_user = user_in_db.copy(update=update_data)
    return await db_manager.update_user(id, updated_user)


@users.delete('/{id}', response_model=None)
async def delete_user(id: int):
    user = await db_manager.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await db_manager.delete_user(id)
