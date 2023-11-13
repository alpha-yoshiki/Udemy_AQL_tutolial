import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "sample.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "CREATE TABLE items(\
        item_id INTEGER PRIMARY KEY, \
        item_name STRING, \
        prince INTEGER\
    )"

cur.execute(query)
conn.commit()
conn.close()