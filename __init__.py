"""Import the libraries."""
import os
import requests
import json
from bs4 import BeautifulSoup
from flask import Flask
from .database import db
from dotenv import load_dotenv, dotenv_values

load_dotenv()
with open(file="headers.json", mode="r", encoding="utf-8") as file:
    HEADERS = json.load(file)

def create_app():
    """Initialize the flask application."""

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    db.init_app(app=app)

    return app

class WebScraping:

    def __init__(self):
        self.session = requests.Session()
        self.headers = HEADERS.get("headers")

    def get_beautiful(self, url: str):
        self.response = requests.get(url=url, headers=self.headers)
        self.response.raise_for_status()

        soup = BeautifulSoup(self.response.text, "html.parser")
        return soup
