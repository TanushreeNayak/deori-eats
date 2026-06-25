from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantCreate
from app.deps import get_db

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)


@router.post("/")
def create_restaurant(
    restaurant: RestaurantCreate,
    db: Session = Depends(get_db)
):

    new_restaurant = Restaurant(
        name=restaurant.name,
        owner_name=restaurant.owner_name,
        phone=restaurant.phone,
        address=restaurant.address
    )

    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)

    return {
        "message": "Restaurant created successfully",
        "restaurant_id": new_restaurant.id
    }


@router.get("/")
def get_restaurants(db: Session = Depends(get_db)):

    restaurants = db.query(Restaurant).all()

    return restaurants