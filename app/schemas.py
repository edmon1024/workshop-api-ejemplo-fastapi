import pydantic
from pydantic import validator
import typing
from uuid import UUID, uuid4


class SchemaCustomer(pydantic.BaseModel):
    id: str
    name: str
    last_name: str
    email: pydantic.EmailStr
    age: pydantic.PositiveInt

    @validator('id', pre=True, always=True)
    def convert_id_to_str(cls, v):
        return str(v)

class SchemaCustomerCreation(pydantic.BaseModel):
    name: str
    last_name: str
    email: pydantic.EmailStr
    age: pydantic.PositiveInt


class SchemaCustomerUpdate(pydantic.BaseModel):
    name: typing.Union[str, None]
    last_name: typing.Union[str, None]
    email: typing.Union[pydantic.EmailStr, None]
    age: typing.Union[pydantic.PositiveInt, None]



