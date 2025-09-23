# models/order.py

from sqlalchemy import Column, String, Integer, DECIMAL, DateTime, ForeignKey
from db import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(String(10), primary_key=True, index=True)
    customer_id = Column(String(10), ForeignKey("customers.customer_id"))
    product_id = Column(String(10), ForeignKey("products.product_id"))
    order_date = Column(DateTime)
    quantity = Column(Integer)
    unit_price = Column(DECIMAL(10, 2))
    payment_method = Column(String(50))
    delivery_status = Column(String(50))
