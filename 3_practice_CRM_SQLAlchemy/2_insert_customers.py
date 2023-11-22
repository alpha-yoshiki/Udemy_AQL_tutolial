from sqlalchemy.sql import insert
from models import engine, customers
import sqlalchemy

values = [
    {
        "customer_id": 'C001',
        "customer_name": '佐藤A子',
        "age": 64,
        "gender": '女'
    },
    {
        "customer_id": 'C002',
        "customer_name": '鈴木B子',
        "age": 34,
        "gender": '女'
    },
    {
        "customer_id": 'C003',
        "customer_name": '斎藤C男',
        "age": 21,
        "gender": '男'
    },
    {
        "customer_id": 'C010',
        "customer_name": '斎藤M男',
        "age": 2100,
        "gender": '男'
    },
]

for value in values:
    query = customers.insert().values(value)

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
