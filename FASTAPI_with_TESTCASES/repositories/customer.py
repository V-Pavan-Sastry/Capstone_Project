# repositories/customer.py

from sqlalchemy.orm import Session
from models.customer import Customer
from fastapi import HTTPException

def get_loyalty_status_by_customer_id(db: Session, customer_id: str):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {
        "customer_id": customer.customer_id,
        "loyalty_status": customer.loyalty_status
    }
