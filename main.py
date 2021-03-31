import os

from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = os.getenv("DEBUG")
app.config["TESTING"] = os.getenv("TESTING")
app.config["FLASK_ENV"] = os.getenv("FLASK_ENV")


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/home")
def home():
    return {"message": "Hello"}, 200
