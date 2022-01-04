from addresses_service.app.api.models import AddressIn
from addresses_service.app.api.db import addresses, database


async def add_address(address: AddressIn):
    query = addresses.insert().values(**address.dict())
    return await database.execute(query=query)


async def get_address(id):
    query = addresses.select(addresses.c.id==id)
    return await database.fetch_one(query=query)


async def get_user_addresses(user_id):
    query = addresses.select().where(addresses.c.user_id==user_id)
    return await database.fetch_all(query=query)


async def get_all_addresses():
    query = addresses.select()
    return await database.fetch_all(query=query)


async def delete_address(id: int):
    query = addresses.delete().where(addresses.c.id==id)
    return await database.execute(query=query)


async def update_address(id: int, address: AddressIn):
    query = (
        addresses
        .update()
        .where(addresses.c.id == id)
        .values(**address.dict())
    )
    return await database.execute(query=query)

