import flask
import random

r = random
f = flask
app = flask.Flask(__name__)

name = "MENU"
mprice = 100
pizzas = [
    {"pname": "Pepperoni", "price": 79},
    {"pname": "Hawaii", "price": 99},
    {"pname": "4 Cheeses", "price": 59},
    {"pname": "Margarita", "price": 35}
    ]

@app.route("/menu/")
def results():
    context = {
               "title": " ",
               "pizzas": pizzas,
               "name": name,
               "mprice": mprice
               }
    return f.render_template("menu.html", **context)

@app.route("/")
def start():
    return f.render_template("something.html", title="Pizzaria")

app.run(port=11464, debug=True)