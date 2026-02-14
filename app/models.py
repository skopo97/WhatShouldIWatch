from app import db

from datetime import datetime
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'User {self.username}'

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.columng(db.Integer)
    genre = db.Column(db.String)
    imdb_rating = db.Column(db.Float)
    description = db.Column(db.String)

    def __repr__(self):
        return f'Movie {self.title}'
