from flask import Flask, render_template, request
from models import app, Customer, db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("1_index.html")


@app.route("/item/")
def item():
    return render_template("2_item.html")

# 機能系


@app.route("/add_customer", methods=["POST"])
def add_customer():
    customer_id = request.form["input-customer-id"]
    customer_name = request.form["input-customer-name"]
    age = request.form["input-age"]
    gender = request.form["input-gender"]

    customer = Customer(customer_id, customer_name, age, gender)
    db.session.add(customer)
    db.session.commit()

    print(customer_id)
    print(customer_name)
    print(age)
    print(gender)
    return customer_id


if __name__ == "__main__":
    app.run(debug=True)
