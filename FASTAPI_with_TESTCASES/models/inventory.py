# models/inventory.py

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from db import Base

class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(String(10), primary_key=True, index=True)
    product_id = Column(String(10))  # Can add ForeignKey("products.product_id") if needed
    warehouse_id = Column(String(10))
    stock_level = Column(Integer)
    reorder_level = Column(Integer)
    last_restock_date = Column(Date)
