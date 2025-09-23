# models/product.py
from sqlalchemy import Column, String, Integer, DECIMAL
from db import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(String(10), primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)
    category = Column(String(50))
    subcategory = Column(String(50))
    brand = Column(String(50))
    price = Column(DECIMAL(10, 2))
    stock_level = Column(Integer)
