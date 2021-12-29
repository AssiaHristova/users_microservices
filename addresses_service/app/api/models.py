from pydantic import BaseModel, Field, constr


class AddressCls:
    def __init__(self, *, id: int, user_id: int, address: str):
        self.id = id
        self.user_id = user_id
        self.addresses = address


class AddressIn(BaseModel):
    id: int
    user_id: int
    address: constr(max_length=50)


class AddressOut(AddressIn):
    id: int


class AddressUpdate(AddressIn):
    address: constr(max_length=50)


