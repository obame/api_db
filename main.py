from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models
from database import SessionLocal, engine

#Permet de se passer de Pydantic. On récupère les objets en les formattant directement en JSON
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dépendences
def get_db():
	db = SessionLocal()
	try:
#On utilise yield au lieu de return
		yield db

	finally:
		db.close()

#le endpoint racine "/" redirige ves la documentation de l'API
@app.get("/")
def main():
	return RedirectResponse(url="/docs")


#endpoint pour la création d'un user de l'API
@app.post("v1/bike/users")
def create_user():

	return JSONResponse(content= "Comming soon")


#endpoint pour l'authentification d'un user de l'API
@app.post("v1/bike/user/{user_token}")
def get_user():
	return JSONResponse(content= "Comming soon")


# endpoint qui renvoie 10 customers
@app.get("/v1/bike/customers")
def list_customers(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
	customers = crud.get_customers(db, skip=skip, limit=limit)
	json_compatible_customers_data = jsonable_encoder(customers)
	return JSONResponse(content=json_compatible_customers_data)

#endpoint qui renvoie le customer selon le custoemr_id fourni
@app.get("/v1/bike/customers/{customer_id}")
def read_customer(customer_id: int, db: Session = Depends(get_db)):
	db_customer = crud.get_customer(db, customer_id = customer_id)
	if db_customer is None:
		raise HTTPException(status_code=404, detail="Client non trouvé")
	json_compatible_customer_id_data = jsonable_encoder(db_customer)
	return JSONResponse(content=json_compatible_customer_id_data)

# endpoint qui renvoie 10 produits
@app.get("/v1/bike/products")
def list_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
	products = crud.get_products(db, skip=skip, limit=limit)
	json_compatible_products_data = jsonable_encoder(products)
	return JSONResponse(content=json_compatible_products_data)

#endpoint qui renvoie le produit selon le product_id fourni
@app.get("/v1/bike/products/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
	db_product = crud.get_product(db, product_id = product_id)
	if db_product is None:
		raise HTTPException(status_code=404, detail="Produit non trouvé")
	json_compatible_product_id_data = jsonable_encoder(db_product)
	return JSONResponse(content=json_compatible_product_id_data)

#endpoint qui renvoie 10 commandes
@app.get("/v1/bike/orders")
def list_orders(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
	orders = crud.get_orders(db, skip=skip, limit=limit)
	json_compatible_orders_data = jsonable_encoder(orders)
	return JSONResponse(content=json_compatible_orders_data)

#endpoint qui renvoie la commande selon l'id de la commande
@app.get("/v1/bike/orders/{order_id}")
def read_order(order_id: int, db: Session = Depends(get_db)):
	db_order = crud.get_order(db, order_id = order_id)
	if db_order is None:
		raise HTTPException(status_code=404, detail="Commande non trouvée")
	json_compatible_order_id_data = jsonable_encoder(db_order)
	return JSONResponse(content= json_compatible_order_id_data)