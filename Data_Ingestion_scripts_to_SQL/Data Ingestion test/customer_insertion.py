import pandas as pd

# Read CSV
df = pd.read_csv("customers.csv")

# Start SQL command
insert_sql = (
    "INSERT INTO customers (customer_id, name, email, city, state, country, signup_date, loyalty_status)\nVALUES\n"
)

# Build value rows
value_rows = []
for _, row in df.iterrows():
    customer_id = row['customer_id']
    name = row['name'].replace("'", "''")
    email = row['email'].replace("'", "''")
    city = row['city'].replace("'", "''")
    state = row['state'].replace("'", "''")
    country = row['country'].replace("'", "''")
    signup_date = row['signup_date']
    loyalty_status = row['loyalty_status'].replace("'", "''")

    value = (
        f"('{customer_id}', '{name}', '{email}', '{city}', '{state}', '{country}', '{signup_date}', '{loyalty_status}')"
    )
    value_rows.append(value)

# Join all values with commas and add semicolon at the end
insert_sql += ",\n".join(value_rows) + ";\n"

# Write to a .sql file
with open("bulk_insert_customers.sql", "w") as f:
    f.write(insert_sql)

print("Bulk SQL insert command saved to bulk_insert_customers.sql")
