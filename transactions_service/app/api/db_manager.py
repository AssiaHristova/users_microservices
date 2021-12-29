from transactions_service.app.api.db import database, transactions
from transactions_service.app.api.models import TransactionIn


async def add_transaction(transaction: TransactionIn):
    attrs = transaction.dict()
    query = transactions.insert().values(**transaction.dict())
    return await database.execute(query=query)


async def get_transaction(id):
    query = transactions.select(transactions.c.id==id)
    return await database.fetch_one(query=query)


async def get_user_transactions(user_id):
    query = transactions.select().where(transactions.c.user_id==user_id)
    return await database.fetch_all(query=query)


async def get_all_transactions():
    query = transactions.select()
    return await database.fetch_all(query=query)


async def delete_transaction(id: int):
    query = transactions.delete().where(transactions.c.id==id)
    return await database.execute(query=query)


async def update_transaction(id: int, transaction: TransactionIn):
    query = (
        transactions
        .update()
        .where(transactions.c.id == id)
        .values(**transaction.dict())
    )
    return await database.execute(query=query)

