import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from datetime import date
from main import app

client = TestClient(app)

mock_inventory = {
    "inventory_id": "INV001",
    "product_id": "PROD001",
    "stock_level": 100,
    "last_restock_date": str(date.today())
}

@patch("repositories.inventory.restock_inventory")
def test_restock_inventory(mock_restock):
    mock_restock.return_value = mock_inventory
    response = client.post("/inventory/INV001/restock", json={"stock_level": 100})
    assert response.status_code == 200
    data = response.json()
    assert data["inventory_id"] == "INV001"
    assert data["stock_level"] == 100

@patch("repositories.inventory.get_low_stock_products")
def test_get_low_stock_products(mock_low_stock):
    mock_low_stock.return_value = [{"product_id": "PROD002"}, {"product_id": "PROD003"}]
    response = client.get("/inventory/low-stock?limit=50")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["product_id"] == "PROD002"
