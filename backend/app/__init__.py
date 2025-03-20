from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from app.routes import product_routes

#instantiates the extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

#Creates ans configures the Flask Application
def create_app():
    #Flask Instance
    app = Flask(__name__)

    #Loading settings from file 'config.py'
    app.config.from_object('app.config.Config')

    #Connects SQLAlchemy to the Flask Application
    db.init_app(app)
    #Allow databases migration
    migrate.init_app(app, db)
    #Enable JWT for authentication
    jwt.init_app(app)
    #allow communication with frontend
    CORS(app)

    #Add the routes to the app
    app.register_blueprint(product_routes.blueprint)

    return app