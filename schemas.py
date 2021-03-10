
#pydantic schemas

from typing import List, Optional
from pydantic import BaseModel

class Customer(BaseModel):

	customer_id: int 
	first_name: Optional[str] = None
	last_name: Optional[str] = None
	phone: Optional[str] = None
	email: Optional[str] = None
	street: Optional[str] = None
	city: Optional[str] = None
	state: Optional[str] = None
	zip_code: Optional[str] = None

#autorise l'application à récupérer l'objet ORM et de le transformer en objet automatiquement

	class Config:
		orm_mode = True