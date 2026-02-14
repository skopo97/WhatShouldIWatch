import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TMDB_API = os.environ.get('TMDB_API')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///picktowatch.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
