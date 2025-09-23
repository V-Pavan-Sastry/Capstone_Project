import pandas as pd

# Read CSV
df = pd.read_csv("website_interactions.csv")

# Start SQL command
insert_sql = (
    "INSERT INTO website_interactions (session_id, customer_id, page_visited, time_spent_seconds, timestamp)\nVALUES\n"
)

# Build value rows
value_rows = []
for _, row in df.iterrows():
    session_id = row['session_id']
    customer_id = row['customer_id']
    page_visited = row['page_visited'].replace("'", "''")
    time_spent = int(row['time_spent_seconds'])
    timestamp = row['timestamp']

    value = (
        f"('{session_id}', '{customer_id}', '{page_visited}', {time_spent}, '{timestamp}')"
    )
    value_rows.append(value)

# Join all values with commas and add semicolon at the end
insert_sql += ",\n".join(value_rows) + ";\n"

# Write to a .sql file
with open("bulk_insert_website_interactions.sql", "w") as f:
    f.write(insert_sql)

print("Bulk SQL insert command saved to bulk_insert_website_interactions.sql")
