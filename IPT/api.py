from flask import Flask, make_response, request, jsonify
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET
import xmltodict
import functools


app = Flask(__name__)
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "zhar"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"


def security(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        a = request.authorization
        if a and a.username == "zhar" and a.password == "2564":
            return f(*args, **kwargs)
        return make_response(
            "Could not verify your login!",
            401,
            {"WWW-Authenticate": 'Basic realm="Login"'},
        )

    return decorated


mysql = MySQL(app)


@app.route("/")
@security
def hello_world():
    return "<p>Hello, World!</p>"


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.route("/tables", methods=["GET"])
def show_tables():
    return make_response(jsonify(data_fetch("show tables")), 200)


@app.route("/tables/<string:table>", methods=["GET"])
def select_table(table):
    return make_response(jsonify(data_fetch(f"select * from {table}")))


@app.route("/tables/<string:table>/<int:id>", methods=["GET"])
def select_table_id(table, id):
    return make_response(jsonify(data_fetch(f"select * from {table} where id='{id}'")))


@app.route("/tables/<string:table>/<int:id>", methods=["POST"])
def add_entries(table, id):
    cur = mysql.connection.cursor()
    info = request.get_json()

    if table == "users":
        username = info["username"]
        password = info["password"]
        query = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
        cur.execute(query, (id, username, password))
        mysql.connection.commit()

    elif table == "products":
        name = info["name"]
        price = info["price"]
        category_id = info["category_id"]
        query = "INSERT INTO products (id, name, price, category_id) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (id, name, price, category_id))
        mysql.connection.commit()

    elif table == "orders":
        user_id = info["user_id"]
        product_id = info["product_id"]
        query = "INSERT INTO orders (id, user_id, product_id) VALUES (%s, %s, %s)"
        cur.execute(query, (id, user_id, product_id))
        mysql.connection.commit()

    elif table == "categories":
        name = info["name"]
        query = "INSERT INTO categories (id, name) VALUES (%s, %s)"
        cur.execute(query, (id, name))
        mysql.connection.commit()

        cur.close()
    return make_response(jsonify({"Message": "Successfully Added"}))


@app.route("/tables/<string:table>/<int:id>", methods=["PUT"])
def update_entry(table, id):
    cur = mysql.connection.cursor()
    info = request.get_json()

    if table == "users":
        username = info["username"]
        password = info["password"]
        query = "UPDATE users SET username=%s, password=%s WHERE id=%s"
        cur.execute(query, (id, username, password))
        mysql.connection.commit()

    elif table == "products":
        name = info["name"]
        price = info["price"]
        category_id = info["category_id"]
        query = "UPDATE products SET name=%s, price=%s, category_id=%s WHERE id=%s"
        cur.execute(query, (id, name, price, category_id))
        mysql.connection.commit()

    elif table == "orders":
        user_id = info["user_id"]
        product_id = info["product_id"]
        query = "UPDATE orders SET user_id=%s, product_id=%s WHERE id=%s"
        cur.execute(query, (id, user_id, product_id))
        mysql.connection.commit()

    elif table == "categories":
        name = info["name"]
        query = "UPDATE categories SET name=%s WHERE id=%s"
        cur.execute(query, (id, name))
        mysql.connection.commit()

        cur.close()
    return make_response(jsonify({"Message": "Successfully Updated"}))


@app.route("/tables/<string:table>/<int:id>", methods=["DELETE"])
def delete_by_id(table, id):
    cur = mysql.connection.cursor()

    if table == "users":
        query = "DELETE FROM users WHERE id = %s"
        cur.execute(query, (id,))
        mysql.connection.commit()

    elif table == "products":
        query = "DELETE FROM products WHERE id = %s"
        cur.execute(query, (id,))
        mysql.connection.commit()

    elif table == "orders":
        query = "DELETE FROM orders WHERE id = %s"
        cur.execute(query, (id,))
        mysql.connection.commit()

    elif table == "categories":
        query = "DELETE FROM categories WHERE id = %s"
        cur.execute(query, (id,))
        mysql.connection.commit()

        cur.close()
    return make_response(jsonify({"Message": "Successfully Deleted"}))


if __name__ == "__main__":
    app.run(debug=True)
