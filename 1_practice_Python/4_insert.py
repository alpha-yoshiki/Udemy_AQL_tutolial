# 4_insert.py

import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "sample.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# query = "INSERT INTO items(item_id, item_name, price) VALUES(1, 'おにぎり', 100)"
query = "INSERT INTO items(item_name, price) VALUES('いくらおにぎり', 250)"
# query = "INSERT INTO items(item_name) VALUES('鮭おにぎり')"

cur.execute(query)
conn.commit()
conn.close()