# main.py
from fastapi import FastAPI
from routes import product,order,customer,inventory

app = FastAPI(title="Capstone API")

# Register routers
app.include_router(product.router)
app.include_router(order.router)
app.include_router(customer.router) 
app.include_router(inventory.router)