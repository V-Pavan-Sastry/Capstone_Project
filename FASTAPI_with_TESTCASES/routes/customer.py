# routes/customer.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas.customer import LoyaltyStatusResponse
from repositories import customer as customer_repo

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)

@router.get("/{customer_id}/loyalty", response_model=LoyaltyStatusResponse)
def get_loyalty_status(customer_id: str, db: Session = Depends(get_db)):
    return customer_repo.get_loyalty_status_by_customer_id(db, customer_id)
