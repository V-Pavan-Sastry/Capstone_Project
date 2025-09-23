import pandas as pd

# Read CSV
df = pd.read_csv("inventory.csv")

# Start SQL command
insert_sql = (
    "INSERT INTO inventory (inventory_id, product_id, warehouse_id, stock_level, reorder_level, last_restock_date)\nVALUES\n"
)

# Build value rows
value_rows = []
for _, row in df.iterrows():
    inventory_id = row['inventory_id']
    product_id = row['product_id']
    warehouse_id = row['warehouse_id']
    stock_level = int(row['stock_level'])
    reorder_level = int(row['reorder_level'])
    last_restock_date = row['last_restock_date']

    value = f"('{inventory_id}', '{product_id}', '{warehouse_id}', {stock_level}, {reorder_level}, '{last_restock_date}')"
    value_rows.append(value)

# Join all values with commas and add semicolon at the end
insert_sql += ",\n".join(value_rows) + ";\n"

# Write to a .sql file
with open("bulk_insert_inventory.sql", "w") as f:
    f.write(insert_sql)

print("Bulk SQL insert command saved to bulk_insert_inventory.sql")
