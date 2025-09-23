import pandas as pd

# Read CSV
df = pd.read_csv("orders.csv")

# Start SQL command
insert_sql = (
    "INSERT INTO orders (order_id, customer_id, product_id, order_date, quantity, unit_price, payment_method, delivery_status)\nVALUES\n"
)

# Build value rows
value_rows = []
for _, row in df.iterrows():
    order_id = row['order_id']
    customer_id = row['customer_id']
    product_id = row['product_id']
    order_date = row['order_date']
    quantity = int(row['quantity'])
    unit_price = float(row['unit_price'])  # ensure proper decimal formatting
    payment_method = row['payment_method'].replace("'", "''")
    delivery_status = row['delivery_status'].replace("'", "''")

    value = (
        f"('{order_id}', '{customer_id}', '{product_id}', '{order_date}', {quantity}, {unit_price}, '{payment_method}', '{delivery_status}')"
    )
    value_rows.append(value)

# Join all values with commas and add semicolon at the end
insert_sql += ",\n".join(value_rows) + ";\n"

# Write to a .sql file
with open("bulk_insert_orders.sql", "w") as f:
    f.write(insert_sql)

print("Bulk SQL insert command saved to bulk_insert_orders.sql")
