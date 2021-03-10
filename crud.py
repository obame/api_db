from sqlalchemy.orm import Session
import models

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

