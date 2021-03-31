import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config["DEBUG"] = os.getenv("DEBUG")
app.config["TESTING"] = os.getenv("TESTING")
app.config["FLASK_ENV"] = os.getenv("FLASK_ENV")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")

db.init_app(app=app)

from app.models.users.user import UserModel


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def hello_world():

    user = UserModel.find_by_username(username="hhjj")

    if user:
        user.delete_from_db()

    UserModel(
        phone="",
        email="hhhh",
        username="hhjj",
    ).save_to_db()

    user = UserModel.find_by_username(username="hhjj")

    if not user:
        return jsonify({"message": "Not found"}), 404

    return jsonify({"user": user.json()}), 200


@app.route("/home")
def home():
    return jsonify({"message": "Hello"}), 200
