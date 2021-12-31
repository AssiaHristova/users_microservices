from pydantic import BaseModel


class AddressIn(BaseModel):
    id: int
    user_id: int
    address: str


class AddressOut(AddressIn):
    id: int


class AddressUpdate(AddressIn):
    address: str


