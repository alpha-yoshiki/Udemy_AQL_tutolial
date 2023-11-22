from sqlalchemy.sql import delete
from models import engine, customers

conn = engine.connect()

query = delete(customers).where(customers.c.customer_id ==
                                "C010")

conn.execute(query)

conn.close()
