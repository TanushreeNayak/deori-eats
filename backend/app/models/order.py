from sqlalchemy import Column, Integer, ForeignKey, String
from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))

    quantity = Column(Integer, nullable=False)

    status = Column(String, default="Pending")