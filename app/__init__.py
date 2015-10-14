from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('default_config')
# This envar should be set to the production config path
# during the deployment process.
# TODO: change to a less generic name, 
# as soon as one has been found for this package.
app.config.from_envvar('BLOG_APP_CONFIG', silent=True)


# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import modules/components using their blueprint handler variables
# TODO: try this at the beginning and see if it still works (circular deps?!)
# from app.auth.controllers import auth as auth
# ..

# Register blueprint(s)
# app.register_blueprint(auth)
# ..

# Build the database:
db.create_all()
# TODO: We also need a manager (from flask-script)
# for setting up the database with persistent data (independent from the app-session),
# e.g. creating admins, standard roles, etc.
