from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
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

    @app.route('/login')
    def login():

        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.form == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')

            from app.models import User
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                flash('Username already exists')
                return redirect(url_for('register'))

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            flash('Registration completed. You may now login.')
            return redirect(url_for('login'))


        return render_template('register.html')


    return app