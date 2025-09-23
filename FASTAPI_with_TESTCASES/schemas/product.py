# schemas/product.py
from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    product_name: str
    category: Optional[str] = None
    subcategory: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[float] = 0.0
    stock_level: Optional[int] = 0

class ProductCreate(ProductBase):
    product_id: str  # Required for primary key

class ProductUpdate(ProductBase):
    pass  # All fields optional for PATCH

class ProductResponse(ProductCreate):
    class Config:
        orm_mode = True
