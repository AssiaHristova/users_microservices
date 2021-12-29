
from typing import List
from fastapi import APIRouter, HTTPException
from transactions_service.app.api import db_manager
from transactions_service.app.api.adapter import parse_transaction_info
from transactions_service.app.api.models import TransactionIn, TransactionOut, TransactionUpdate, TransactionCreate

transactions = APIRouter()


@transactions.get('/')
async def home():
    return "Hello Transactions"


@transactions.get('/all', response_model=List[TransactionOut])
async def get_all_transactions():
    return await db_manager.get_all_transactions()


@transactions.get("/all/{user_id}", response_model=List[TransactionOut])
async def get_user_transactions(user_id: int):
    return await db_manager.get_user_transactions(user_id)


@transactions.post('/', response_model=TransactionOut, status_code=201)
async def create_transaction(transaction: TransactionIn):
    id = parse_transaction_info()[0]
    date_of_execution = parse_transaction_info()[1]
    transaction_create = TransactionCreate(
        id=id, date_of_execution=date_of_execution, user_id=transaction.user_id, amount=transaction.amount)
    transaction_create.date_of_execution = transaction_create.date_of_execution.replace(tzinfo=None)
    transaction_id = await db_manager.add_transaction(transaction_create)
    response = {
        'id': transaction_create.id,
        "date_of_execution": transaction_create.date_of_execution,
        **transaction_create.dict()
        }
    return response


@transactions.get('/{id}/', response_model=TransactionOut)
async def get_transaction(id: str):
    transaction = await db_manager.get_transaction(id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@transactions.put('/{id}/', response_model=TransactionOut)
async def update_transaction(id: str, payload: TransactionUpdate):
    transaction = await db_manager.get_transaction(id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    update_data = payload.dict(exclude_unset=True)
    transaction_in_db = TransactionIn(**transaction)
    updated_transaction = transaction_in_db.copy(update=update_data)
    return await db_manager.update_transaction(id, updated_transaction)


@transactions.delete('/{id}', response_model=None)
async def delete_transaction(id: str):
    transaction = await db_manager.get_transaction(id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return await db_manager.delete_transaction(id)
