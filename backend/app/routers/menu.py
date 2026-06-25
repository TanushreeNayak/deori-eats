from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from app.models.menu_item import MenuItem
from app.schemas.menu_item import MenuItemCreate

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)


@router.post("/")
def create_menu_item(
    item: MenuItemCreate,
    db: Session = Depends(get_db)
):

    new_item = MenuItem(
        restaurant_id=item.restaurant_id,
        name=item.name,
        description=item.description,
        price=item.price,
        category=item.category
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return {
        "message": "Menu item created successfully",
        "menu_item_id": new_item.id
    }


@router.get("/")
def get_all_menu_items(
    db: Session = Depends(get_db)
):
    return db.query(MenuItem).all()


@router.get("/{restaurant_id}")
def get_restaurant_menu(
    restaurant_id: int,
    db: Session = Depends(get_db)
):

    items = (
        db.query(MenuItem)
        .filter(MenuItem.restaurant_id == restaurant_id)
        .all()
    )

    return items