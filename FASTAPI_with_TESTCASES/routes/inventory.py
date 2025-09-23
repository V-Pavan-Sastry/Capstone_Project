# routes/inventory.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas.inventory import RestockRequest, InventoryResponse, LowStockResponse
from repositories import inventory as inventory_repo
from typing import List

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)

@router.post("/{inventory_id}/restock", response_model=InventoryResponse)
def restock_inventory(inventory_id: str, body: RestockRequest, db: Session = Depends(get_db)):
    return inventory_repo.restock_inventory(db, inventory_id, body.stock_level)

@router.get("/low-stock", response_model=List[LowStockResponse])
def low_stock_products(limit: int, db: Session = Depends(get_db)):
    return inventory_repo.get_low_stock_products(db, limit)
