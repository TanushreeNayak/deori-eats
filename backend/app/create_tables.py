from app.database import Base, engine

from app.models.user import User
from app.models.restaurant import Restaurant
from app.models.menu_item import MenuItem
from app.models.order import Order

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done!")