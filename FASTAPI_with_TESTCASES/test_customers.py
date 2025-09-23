# tests/test_customers.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

mock_response = {
    "customer_id": "CUST123",
    "loyalty_status": "Gold"
}

@patch("repositories.customer.get_loyalty_status_by_customer_id")
def test_get_loyalty_status_valid(mock_get_loyalty):
    mock_get_loyalty.return_value = mock_response

    response = client.get("/customers/CUST123/loyalty")
    assert response.status_code == 200
    data = response.json()
    assert data["customer_id"] == "CUST123"
    assert data["loyalty_status"] == "Gold"

@patch("repositories.customer.get_loyalty_status_by_customer_id")
def test_get_loyalty_status_invalid(mock_get_loyalty):
    from fastapi import HTTPException
    mock_get_loyalty.side_effect = HTTPException(status_code=404, detail="Customer not found")

    response = client.get("/customers/INVALID/loyalty")
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"
