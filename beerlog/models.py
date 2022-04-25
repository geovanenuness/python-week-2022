from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select

class Beer(SQLModel, table=True):
  id: Optional[int] = Field(primary_key=True, default=None)
  name: str
  style: str
  flavor: int
  image: int
  cost: int

brewdog = Beer(name="Breawdog", style="NEIPA", flavor=4, image=5, cost=5)
