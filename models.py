
# sqlalchemy

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from database import Base


# on définit les classes qui représentent les tables  de la BDD bikestore_db

class Customer(Base):
	__tablename__ = "customers"

	customer_id = Column(Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String )
	phone = Column(String)
	email = Column(String)
	street = Column(String)
	city = Column(String)
	state = Column(String)
	zip_code = Column(String)


class Product(Base):
	__tablename__ = 'products'

	product_id = Column(Integer, primary_key=True)
	product_name = Column(String)
	brand_id = Column(Integer)
	category_id = Column(Integer)
	model_year = Column(Integer)
	list_price = Column(Float)


class Order(Base):
	__tablename__ = 'orders'

	order_id = Column(Integer, primary_key=True)
	customer_id = Column(Integer)
	order_status = Column(Integer)
	order_date = Column(String)
	required_date = Column(String)
	shipped_date = Column(String)
	store_id = Column(Integer)
	staff_id = Column(Integer)



class Order_item(Base):
	__tablename__ = 'order_item'
	
	order_id = Column(Integer, primary_key=True)
	item_id = Column(Integer, primary_key=True)
	product_id = Column(Integer)
	quantity = Column(Integer)
	list_price = Column(Integer)
	discount = Column(Integer)


class Store(Base):
	__tablename__ = 'stores'

	store_id = Column(Integer, primary_key=True)
	store_name = Column(String)
	phone = Column(String)
	email = Column(String)
	street = Column(String)
	city = Column(String)
	state = Column(String)
	zip_code = Column(String)



