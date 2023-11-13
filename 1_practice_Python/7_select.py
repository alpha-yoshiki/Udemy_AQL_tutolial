# 7_select.py

import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "sample.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "SELECT * FROM items"

cur.execute(query)
print(cur.fetchall())
conn.commit()
conn.close()