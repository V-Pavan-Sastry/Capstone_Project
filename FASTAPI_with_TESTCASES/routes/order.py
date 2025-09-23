# routes/order.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas.order import OrderResponse
from typing import List
from repositories import order as order_repo

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("/customer/{customer_id}", response_model=List[OrderResponse])
def get_orders_by_customer(customer_id: str, db: Session = Depends(get_db)):
    return order_repo.get_orders_by_customer_id(db, customer_id)
