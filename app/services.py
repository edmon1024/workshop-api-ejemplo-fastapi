from uuid import uuid4

from .db import database, t_customers
from . import schemas


async def get_customers() -> list:
    query = t_customers.select()
    return await database.fetch_all(query)


async def get_customer_by_id(customer_id: str) -> dict:
    query = t_customers.select().where(t_customers.c.id == customer_id)
    return await database.fetch_one(query=query)


async def save_customer(data: schemas.SchemaCustomerCreation) -> dict:
    query = t_customers.insert()
    data["id"] = str(uuid4())
    await database.execute(query=query, values=data)
    return data


async def update_customer(customer_id: str, data: schemas.SchemaCustomerUpdate) -> dict:
    query = t_customers.update().where(t_customers.c.id == customer_id)
    await database.execute(query=query, values=data.dict(exclude_none=True))
    return await get_customer_by_id(customer_id)


async def delete_customer(customer_id: str) -> bool:
    query = t_customers.delete().where(t_customers.c.id == customer_id)
    await database.execute(query=query)
    return True



