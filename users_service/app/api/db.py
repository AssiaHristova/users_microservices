import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://root:root@localhost/users'

#DATABASE_URL = os.getenv('DATABASE_URL')


engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(50)),
    Column('last_name', String(50)),
)

database = Database(DATABASE_URL)
