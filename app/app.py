import os

from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from app.extensions import db
from app.views.plate_view import PlatesView, PlateSearchView

load_dotenv()


def register_extensions(app):
    """Register Flask Extensions."""
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.getenv('SECRET_KEY')
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)
    return None


def create_app():
    app = Flask(__name__)
    register_extensions(app)
    return app


application = create_app()

api = Api(application)
api.add_resource(PlatesView, '/api/v1/plate')
api.add_resource(PlateSearchView, '/api/v1/search-plate')
