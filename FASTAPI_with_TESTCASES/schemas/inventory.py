# schemas/inventory.py

from pydantic import BaseModel
from datetime import date
from typing import List

class RestockRequest(BaseModel):
    stock_level: int

class InventoryResponse(BaseModel):
    inventory_id: str
    product_id: str
    stock_level: int
    last_restock_date: date

    class Config:
        orm_mode = True

class LowStockResponse(BaseModel):
    product_id: str
