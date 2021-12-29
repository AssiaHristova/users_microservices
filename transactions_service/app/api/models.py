from typing import Optional

from pydantic import BaseModel, Field


class TransactionIn(BaseModel):
    id: str
    date_of_execution: str
    user_id: int
    amount: float


class TransactionOut(TransactionIn):
    id: str


class TransactionCreate(TransactionIn):
    id: str
    date_of_execution: str
    user_id: int
    amount: float


class TransactionUpdate(TransactionIn):
    amount: float
