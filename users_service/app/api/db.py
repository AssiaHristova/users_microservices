import os
import psycopg2
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)
import asyncpg
from databases import Database

DATABASE_URL = 'postgresql://root:root@localhost/users_service'

#DATABASE_URL = os.getenv('DATABASE_URL')
#DATABASE_URI = os.getenv('DATABASE_URI')

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
