# 4_insert.py

import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "CRM.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

values = [
    ('S001','お茶',150),
    ('S002','おにぎり',100),
    ('S003','サンドイッチ',400),
]
for value in values:
    query = f"INSERT INTO items(item_id, item_name, price) VALUES{value}"
    cur.execute(query)

conn.commit()
conn.close()