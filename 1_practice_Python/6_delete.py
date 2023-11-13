# 6_delete.py
import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "sample.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "DELETE FROM items WHERE item_id=3"

cur.execute(query)
conn.commit()
conn.close()