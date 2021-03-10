
#pydantic schemas

from typing import List, Optional
from pydantic import BaseModel

class Customer(BaseModel):

#autorise l'application à récupérer l'objet ORM et de le transformer en objet automatiquement

	class Config:
		orm_mode = True