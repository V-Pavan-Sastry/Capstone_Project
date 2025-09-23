CREATE DATABASE capstone;

USE capstone;


CREATE TABLE inventory (
    inventory_id VARCHAR(10) PRIMARY KEY,
    product_id VARCHAR(10),
    warehouse_id VARCHAR(10),
    stock_level INT,
    reorder_level INT,
    last_restock_date DATE
);

CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    subcategory VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2),
    stock_level INT
);

CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    signup_date DATE,
    loyalty_status VARCHAR(50)
);

CREATE TABLE website_interactions (
    session_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    page_visited VARCHAR(50),
    time_spent_seconds INT,
    timestamp DATETIME,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    order_date DATETIME,
    quantity INT,
    unit_price DECIMAL(10,2),
    payment_method VARCHAR(50),
    delivery_status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


