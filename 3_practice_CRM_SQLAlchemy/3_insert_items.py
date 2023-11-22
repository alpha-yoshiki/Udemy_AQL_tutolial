from sqlalchemy.sql import insert
from models import engine, customers, items
import sqlalchemy

values = (
    {
        "item_id": 'S001',
        "item_name": 'お茶',
        "price": 150,
    },
    {
        "item_id": 'S002',
        "item_name": 'おにぎり',
        "price": 100,
    },
    {
        "item_id": 'S003',
        "item_name": 'サンドイッチ',
        "price": 400,
    },
)

query = items.insert().values(values)

conn = engine.connect()
try:
    result = conn.execute(query)
    if result.is_insert:
        print("insert成功")
        print("inserted_primary_key{}".format(
            result.inserted_primary_key[0]))
    print(result.is_insert)
except sqlalchemy.exc.IntegrityError:
    print("unique違反でinsert失敗")


conn.close()
