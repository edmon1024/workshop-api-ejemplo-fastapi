import pydantic
import typing


class SchemaCustomer(pydantic.BaseModel):
    id: int
    name: str
    last_name: str
    email: pydantic.EmailStr
    age: pydantic.PositiveInt
        

class SchemaCustomerCreation(pydantic.BaseModel):
    id: int
    name: str
    last_name: str
    email: pydantic.EmailStr
    age: pydantic.PositiveInt


class SchemaCustomerUpdate(pydantic.BaseModel):
    name: typing.Union[str, None]
    last_name: typing.Union[str, None]
    email: typing.Union[pydantic.EmailStr, None]
    age: typing.Union[pydantic.PositiveInt, None]



