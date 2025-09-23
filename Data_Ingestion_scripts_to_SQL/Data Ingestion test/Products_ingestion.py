import pandas as pd

# Read CSV
df = pd.read_csv("products.csv")

# Start SQL command
insert_sql = (
    "INSERT INTO products (product_id, product_name, category, subcategory, brand, price, stock_level)\nVALUES\n"
)

# Build value rows
value_rows = []
for _, row in df.iterrows():
    product_id = row['product_id']
    product_name = row['product_name'].replace("'", "''")  # Escape single quotes
    category = row['category'].replace("'", "''")
    subcategory = row['subcategory'].replace("'", "''")
    brand = row['brand'].replace("'", "''")
    price = float(row['price'])  # Ensures proper decimal formatting
    stock_level = int(row['stock_level'])

    value = (
        f"('{product_id}', '{product_name}', '{category}', '{subcategory}', '{brand}', {price}, {stock_level})"
    )
    value_rows.append(value)

# Join all values with commas and add semicolon at the end
insert_sql += ",\n".join(value_rows) + ";\n"

# Write to a .sql file
with open("bulk_insert_products.sql", "w") as f:
    f.write(insert_sql)

print("Bulk SQL insert command saved to bulk_insert_products.sql")
