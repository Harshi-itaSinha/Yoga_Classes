# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import main_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yoga_3pkn_user:3r2cqEhJ8H11kMBf6RSVYxG00VtEI381@dpg-clvjided3nmc738dnvu0-a.oregon-postgres.render.com/yoga_3pkn'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialize the db object with the app
    db.init_app(app)
    # with app.app_context():
    #     from .models import User  # Import your User model here


    # Additional configuration and extensions can be added here    # Register blueprints
    app.register_blueprint(main_bp)

    return app
