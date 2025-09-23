from pydantic import BaseModel

class LoyaltyStatusResponse(BaseModel):
    customer_id: str
    loyalty_status: str

    class Config:
        orm_mode = True
