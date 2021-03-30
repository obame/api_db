from sqlalchemy.orm import Session
import models
import database
from database import sale_collection

import motor.motor_asyncio

from bson import ObjectId


def get_customer(db: Session, customer_id: int):
	return db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()

def get_product(db: Session, product_id: int):
	return db.query(models.Product).filter(models.Product.product_id == product_id).first()

def get_order(db: Session, order_id: int):
	return db.query(models.Order).filter(models.Order.order_id == order_id).first()



def get_customers(db: Session, skip: int = 0, limit: int = 10):
	return db.query(models.Customer).offset(skip).limit(limit).all()

def get_products(db: Session, skip: int = 0, limit: int = 10):
	return db.query(models.Product).offset(skip).limit(limit).all()

def get_orders(db: Session, skip: int = 0, limit: int = 10):
	return db.query(models.Order).offset(skip).limit(limit).all()


#CRUD of mongodb 

#retrieve list of sales
async def get_sales():
	sales = []
	cursor = sale_collection.find({}).limit(10)
	async for sale in cursor:
		sales.append(sale)
	return str(sales)

#retrieve sale by id
async def get_sale(id: str) -> dict:
	sale = await sale_collection.find_one({ "_id": ObjectId(id)})
	if sale:
		return str(sale)
