from app.models.user import User
from app.models.restaurant import Restaurant
from app.database import Base, engine

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done!")