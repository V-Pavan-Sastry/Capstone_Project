# schemas/order.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    customer_id: str
    product_id: str
    order_date: datetime
    quantity: int
    unit_price: float
    payment_method: Optional[str] = None
    delivery_status: Optional[str] = None

class OrderResponse(OrderBase):
    order_id: str

    class Config:
        orm_mode = True
