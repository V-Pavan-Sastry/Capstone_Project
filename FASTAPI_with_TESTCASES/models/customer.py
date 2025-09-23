from sqlalchemy import Column, String, Date
from db import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(String(10), primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    signup_date = Column(Date)
    loyalty_status = Column(String(50))
