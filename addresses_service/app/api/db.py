import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://root:root@localhost/users'
#DATABASE_URL = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

addresses = Table(
    'addresses',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer()),
    Column('address', String(50)),
)

database = Database(DATABASE_URL)
