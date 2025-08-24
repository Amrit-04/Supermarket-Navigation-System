from sqlalchemy.orm import Session
from . import models

def get_item_by_name(db: Session, name: str):
    return db.query(models.Item).filter(models.Item.name.ilike(f"%{name}%")).first()

def update_stock(db: Session, item_id: int, stock: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        item.stock = stock
        db.commit()
        db.refresh(item)
    return item