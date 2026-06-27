from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from app.models.order import Order
from app.schemas.order import OrderCreate

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):

    new_order = Order(
        user_id=order.user_id,
        restaurant_id=order.restaurant_id,
        menu_item_id=order.menu_item_id,
        quantity=order.quantity
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "message": "Order placed successfully",
        "order_id": new_order.id
    }

@router.get("/")
def get_orders(
    db: Session = Depends(get_db)
):
    return db.query(Order).all()