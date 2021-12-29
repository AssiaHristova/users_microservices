from datetime import datetime
from pydantic import BaseModel


class TransactionIn(BaseModel):
    user_id: int
    amount: float


class TransactionOut(TransactionIn):
    id: str


class TransactionCreate(TransactionIn):
    id: str = None
    date_of_execution: datetime = None
    user_id: int
    amount: float


class TransactionUpdate(TransactionIn):
    amount: float
