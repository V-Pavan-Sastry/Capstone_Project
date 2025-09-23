# repositories/order.py

from sqlalchemy.orm import Session
from models.order import Order
from fastapi import HTTPException

def get_orders_by_customer_id(db: Session, customer_id: str):
    orders = db.query(Order).filter(Order.customer_id == customer_id).all()
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this customer")
    return orders
