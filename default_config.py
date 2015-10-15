import os

# TODO: Introduce configuration classes for more flexibility

class Config:
    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2
    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True
    # Use a secure, unique and absolutely secret key for
    # signing the data. 
    CSRF_SESSION_KEY = "secret"
    # Secret key for signing cookies
    SECRET_KEY = "secret"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(BASE_DIR, 'app-dev.db')
    DATABASE_CONNECT_OPTIONS = {}


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}


config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,

        'default': DevelopmentConfig
        }
