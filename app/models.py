from app import db

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
    tmdb_id = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    overview = db.Column(db.Text)
    release_date = db.Column(db.Date)
    year = db.Column(db.Integer)
    poster_path = db.Column(db.String(255))
    backdrop_path = db.Column(db.String(255))
    genre_ids = db.Column(db.String(50))
    def __repr__(self):
        return f'Movie {self.title}'
