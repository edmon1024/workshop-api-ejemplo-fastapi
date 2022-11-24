import pydantic


class SchemaCustomer(pydantic.BaseModel):
    id: int
    name: str
    last_name: str
    email: pydantic.EmailStr
    age: pydantic.PositiveInt
        

class SchemaCustomerCreation(pydantic.BaseModel):
    name: str
    last_name: str
    email: pydantic.EmailStr
    age: pydantic.PositiveInt


