from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, String, Text
from .database import db


# CREATE DATABASE
class Base(DeclarativeBase):
    """Needed when creating sqlalchemy."""
    pass

class Users(db.Model):
    """Create users table."""

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    username: Mapped[str] = mapped_column(String(250), nullable=False)

    def __init__(self, email, password, username):
        super().__init__()
        self.email = email
        self.password = password
        self.username = username
