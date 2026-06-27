from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.deps import get_db
from app.models.order import Order
from app.schemas.order import OrderCreate

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
def place_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):
    new_order = Order(
        restaurant_id=order.restaurant_id,
        user_id=order.user_id,
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
def get_all_orders(
    db: Session = Depends(get_db)
):
    return db.query(Order).all()


@router.get("/user/{user_id}")
def get_user_orders(
    user_id: int,
    db: Session = Depends(get_db)
):
    orders = (
        db.query(Order)
        .filter(Order.user_id == user_id)
        .all()
    )

    return orders


@router.get("/restaurant/{restaurant_id}")
def get_restaurant_orders(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    orders = (
        db.query(Order)
        .filter(Order.restaurant_id == restaurant_id)
        .all()
    )

    return orders


@router.put("/{order_id}/status")
def update_order_status(
    order_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order.status = status

    db.commit()
    db.refresh(order)

    return {
        "message": "Order status updated",
        "order": order
    }