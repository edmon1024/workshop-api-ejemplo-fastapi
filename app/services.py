from .db import database, t_customers
from . import schemas


async def get_customers() -> list:
    query = t_customers.select()
    return await database.fetch_all(query)


async def get_customer_by_id(customer_id: int) -> dict:
    query = t_customers.select().where(t_customers.c.id == customer_id)
    return await database.fetch_one(query=query)


async def save_customer(customer_id: int, data: schemas.SchemaCustomerCreation) -> dict:
    data['id'] = customer_id
    query = t_customers.insert()
    await database.execute(query=query, values=data)
    return data


async def delete_customer(customer_id: int) -> bool:
    query = t_customers.delete().where(t_customers.c.id == customer_id)
    await database.execute(query=query)
    return True



