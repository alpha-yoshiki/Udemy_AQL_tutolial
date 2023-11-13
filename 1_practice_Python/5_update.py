# 5_update.py

# 4_insert.py

import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "sample.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "UPDATE items SET price=150 WHERE item_id=2"

cur.execute(query)
conn.commit()
conn.close()