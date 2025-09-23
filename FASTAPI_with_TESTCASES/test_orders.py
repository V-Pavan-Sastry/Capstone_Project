
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from datetime import datetime

client = TestClient(app)

# Mock order response
mock_order = {
    "order_id": "ORD123",
    "customer_id": "CUST001",
    "product_id": "PROD001",
    "order_date": datetime.utcnow().isoformat(),
    "quantity": 2,
    "unit_price": 49.99,
    "payment_method": "Credit Card",
    "delivery_status": "Pending"
}

@patch("repositories.order.get_orders_by_customer_id")
def test_get_orders_by_customer(mock_get_orders):
    mock_get_orders.return_value = [mock_order]
    response = client.get("/orders/customer/CUST001")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["order_id"] == "ORD123"
    assert data[0]["customer_id"] == "CUST001"

@patch("repositories.order.get_orders_by_customer_id")
def test_get_orders_by_invalid_customer(mock_get_orders):
    from fastapi import HTTPException
    mock_get_orders.side_effect = HTTPException(status_code=404, detail="No orders found for this customer")

    response = client.get("/orders/customer/INVALID")
    assert response.status_code == 404
    assert response.json()["detail"] == "No orders found for this customer"
