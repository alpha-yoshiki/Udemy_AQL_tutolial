# 4_insert.py

import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "CRM.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

customer_id = "C003"
date = "2022/01/03"
get_items = {
    "S004":1,
}
purchases_values = [
    (customer_id,date),
]
# insert purchases table
for value in purchases_values:
    query = f"INSERT INTO purchases(customer_id, date) VALUES{value}"
    cur.execute(query)

# insert purchase_details table

# get latest purchase_id
query = "SELECT * FROM purchases WHERE purchase_id = (select max(purchase_id) from purchases)"
cur.execute(query)
latest_purchase_id = cur.fetchone()[0]
for item_id, quantity in get_items.items():
    purchase_details_value = (latest_purchase_id, item_id, quantity)
    query = f"INSERT INTO purchase_details(purchase_id, item_id, quantity) VALUES{purchase_details_value}"
    cur.execute(query)


conn.commit()
conn.close()