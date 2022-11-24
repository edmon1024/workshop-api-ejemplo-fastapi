from typing import List
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from . import services
from . import schemas
from .db import database
import logging
import settings


logging.basicConfig(filename='fastapi.log', level=logging.INFO)



app = FastAPI(
    title="Workshop FastAPI",
    version="0.1.0",
)


@app.on_event("startup")
async def startup_event():
    await database.connect() 
    logging.info(" Base iniciada.")


@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect() 


@app.get("/", response_model=List[schemas.SchemaCustomer])
async def get_customers():
    return await services.get_customers()


@app.get("/{customer_id}", response_model=schemas.SchemaCustomer)
async def get_customer(customer_id: int):
    item = await services.get_customer_by_id(customer_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

        
@app.delete("/{customer_id}", status_code=201)
async def delete_customer(customer_id: int):
    item = await services.get_customer_by_id(customer_id)
    if item:
        await services.delete_customer(customer_id)
        return {'message': "OK"}
    else:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")

        
@app.post("/{customer_id}", response_model=schemas.SchemaCustomer)
async def save_customer(customer_id: int, data: schemas.SchemaCustomerCreation):
    item = await services.get_customer_by_id(customer_id)
    if item:
        raise HTTPException(status_code=409, detail="Recurso existente")
    else:
        return await services.save_customer(customer_id, dict(data))
        
        
@app.put("/{customer_id}", response_model=schemas.SchemaCustomer)
async def update_customer(customer_id: int, data: schemas.SchemaCustomer):
    item = await services.get_customer_by_id(customer_id)
    if item:
        await services.delete_customer(customer_id)
        return await services.delete_customer(customer_id, dict(data))
    else:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    
    
