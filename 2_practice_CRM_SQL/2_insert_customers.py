# 4_insert.py

import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "CRM.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

values = [
    ('C001','佐藤A子',64,'女'),
    ('C002','鈴木B子',34,'女'),
    ('C003','斎藤C男',21,'男'),
]
for value in values:
    query = f"INSERT INTO customers(customer_id, customer_name, age, gender) VALUES{value}"
    cur.execute(query)

conn.commit()
conn.close()