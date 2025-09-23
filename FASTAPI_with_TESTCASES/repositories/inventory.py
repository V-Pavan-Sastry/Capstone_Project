# repositories/inventory.py

from sqlalchemy.orm import Session
from models.inventory import Inventory
from fastapi import HTTPException
from datetime import date

def restock_inventory(db: Session, inventory_id: str, stock_level: int):
    inventory = db.query(Inventory).filter(Inventory.inventory_id == inventory_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory item not found")

    inventory.stock_level = stock_level
    inventory.last_restock_date = date.today()
    db.commit()
    db.refresh(inventory)
    return inventory

def get_low_stock_products(db: Session, limit: int):
    items = db.query(Inventory).filter(Inventory.stock_level < limit).all()
    return [{"product_id": item.product_id} for item in items]
