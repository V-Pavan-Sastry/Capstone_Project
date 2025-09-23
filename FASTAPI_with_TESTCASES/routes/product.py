# routes/product.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db import get_db
from schemas.product import ProductCreate, ProductResponse, ProductUpdate
from repositories import product as product_repo

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/", response_model=List[ProductResponse])
def list_products(skip: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    return product_repo.get_all_products(db, skip=skip, limit=limit)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: str, db: Session = Depends(get_db)):
    return product_repo.get_product_by_id(db, product_id)

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_repo.create_product(db, product)

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: str, product: ProductUpdate, db: Session = Depends(get_db)):
    return product_repo.update_product(db, product_id, product)

@router.delete("/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    return product_repo.delete_product(db, product_id)
