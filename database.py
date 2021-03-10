import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#On définit la connexion à la base de données en utilisant sqlachemy

SQLALCHEMY_DATABASE_URI = "mysql://root:1234@172.18.0.3/bikestore_db"

SQLALCHEMY_BINDS = { 'users': "sqlite:///./sql_app.db"}

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine )

Base = declarative_base()