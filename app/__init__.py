from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, current_user
from config import Config
from app.tmdb import fetch_popular_movies
import random as rand

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))


    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/random')
    def random():
        movies = fetch_popular_movies()
        random_movie = rand.choice(movies) if movies else None
        print(random_movie)
        return render_template('random.html', movie=random_movie)

    @app.route('/profile')
    @login_required
    def profile():

        return render_template('profile.html')



    return app