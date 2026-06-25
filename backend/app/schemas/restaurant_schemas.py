from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    name: str
    owner_name: str
    phone: str
    address: str