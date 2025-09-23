from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate
from fastapi import HTTPException

def get_all_products(db: Session, skip: int = 0, limit: int = 25):
    return db.query(Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: str):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: str, update_data: ProductUpdate):
    product = get_product_by_id(db, product_id)
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: str):
    product = get_product_by_id(db, product_id)
    db.delete(product)
    db.commit()
    return {"detail": f"Product {product_id} deleted"}
