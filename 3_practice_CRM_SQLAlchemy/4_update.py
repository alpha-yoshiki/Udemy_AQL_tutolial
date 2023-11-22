from sqlalchemy.sql import update
from models import engine, customers

conn = engine.connect()

query = update(customers).where(customers.c.customer_id ==
                                "C002").values(customer_name="鈴木Z子")

conn.execute(query)

conn.close()
