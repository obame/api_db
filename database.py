import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


import motor.motor_asyncio
from bson import ObjectId


# Connexion à la base de données MongoDB
MONGO_DETAILS = "mongodb://172.18.0.4:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.db_supply
sale_collection = database.get_collection("sales")




#On définit la connexion à la base de données en utilisant sqlachemy

SQLALCHEMY_DATABASE_URI = "mysql://root:1234@172.18.0.2/bikestore_db"

SQLALCHEMY_BINDS = { 'users': "sqlite:///./sql_app.db"}

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine )

Base = declarative_base()