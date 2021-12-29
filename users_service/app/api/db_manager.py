from users_service.app.api.db import database, users
from users_service.app.api.models import UserIn


async def add_user(user: UserIn):
    query = users.insert().values(**user.dict())
    return await database.execute(query=query)


async def get_all_users():
    query = users.select()
    return await database.fetch_all(query=query)


async def get_user(id):
    query = users.select(users.c.id==id)
    return await database.fetch_one(query=query)


async def delete_user(id: int):
    query = users.delete().where(users.c.id==id)
    return await database.execute(query=query)


async def update_user(id: int, user: UserIn):
    query = (
        users
        .update()
        .where(users.c.id == id)
        .values(**user.dict())
    )
    return await database.execute(query=query)
