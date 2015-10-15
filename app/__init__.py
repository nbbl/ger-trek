from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from default_config import config


db = SQLAlchemy()

def create_app(config_name):
    # Define the WSGI application object
    app = Flask(__name__)
    
    # Configurations
    app.config.from_object(config[config_name])
    config[config_name].init_app(app) 
    
    # Define the database object which is imported
    # by modules and controllers
    db.init_app(app)

    return app
    
    # Import modules/components using their blueprint handler variables
    # TODO: try this at the beginning and see if it still works (circular deps?!)
    # from app.auth.controllers import auth as auth
    # ..
    
    # Register blueprint(s)
    # app.register_blueprint(auth)
    # ..

# Build the database:
# This is being done in manage.py
#db.create_all()
# TODO: We also need a manager (from flask-script)
# for setting up the database with persistent data (independent from the app-session),
# e.g. creating admins, standard roles, etc.
