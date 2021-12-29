from datetime import datetime

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY, Float, DateTime)

from databases import Database

DATABASE_URL = 'postgresql://root:root@localhost/users_service'
#DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

transactions = Table(
    'transactions',
    metadata,
    Column('id', String(50), primary_key=True),
    Column('date_of_execution', String(50)),
    Column('user_id', Integer()),
    Column('amount', Float()),
)

database = Database(DATABASE_URL)
