"""Import the libraries."""
import os
from flask import Flask
from .database import db
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def create_app():
    """Initialize the flask application."""

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    db.init_app(app=app)

    return app
