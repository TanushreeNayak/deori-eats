from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: int
    restaurant_id: int
    menu_item_id: int
    quantity: int