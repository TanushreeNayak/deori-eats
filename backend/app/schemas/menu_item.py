from pydantic import BaseModel

class MenuItemCreate(BaseModel):
    restaurant_id: int
    name: str
    description: str
    price: float
    category: str