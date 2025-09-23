import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, get_db
from main import app
from models.product import Product

# Use SQLite in-memory DB for testing
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"  # You can also use ":memory:" but `test.db` lets you inspect if needed

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apply the override
app.dependency_overrides[get_db] = override_get_db

# Create test client
client = TestClient(app)

# Setup test DB
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Test data
test_product = {
    "product_id": "TEST001",
    "product_name": "Test Product",
    "category": "Test Category",
    "subcategory": "Test Sub",
    "brand": "Test Brand",
    "price": 99.99,
    "stock_level": 10
}

updated_product = {
    "product_name": "Updated Product",
    "price": 79.99,
    "stock_level": 5
}

def test_create_product():
    response = client.post("/products/", json=test_product)
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == test_product["product_id"]
    assert data["product_name"] == test_product["product_name"]

def test_get_product_by_id():
    response = client.get(f"/products/{test_product['product_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["product_id"] == test_product["product_id"]

def test_get_all_products():
    response = client.get("/products?skip=0&limit=25")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(p["product_id"] == test_product["product_id"] for p in data)

def test_update_product():
    response = client.put(f"/products/{test_product['product_id']}", json=updated_product)
    assert response.status_code == 200
    data = response.json()
    assert data["product_name"] == updated_product["product_name"]
    assert float(data["price"]) == updated_product["price"]

def test_delete_product():
    response = client.delete(f"/products/{test_product['product_id']}")
    assert response.status_code == 200
    assert "deleted" in response.json()["detail"]

def test_get_deleted_product():
    response = client.get(f"/products/{test_product['product_id']}")
    assert response.status_code == 404
