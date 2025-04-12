# app/__init__.py
import os
from flask import Flask
from config import Config
from .extensions import db, login_manager

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass # Already exists

    # Initialize Flask extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Configure Flask-Login
    login_manager.login_view = 'auth.login' # The blueprint name and function name
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info" # Optional: category for flashed message

    # Register Blueprints
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .main import bp as main_bp
    app.register_blueprint(main_bp) # No prefix for main routes like '/'

    from .feature_one import bp as feature_one_bp
    app.register_blueprint(feature_one_bp, url_prefix='/feature1')

    # --- Database Creation Command ---
    # This allows you to run `flask init-db` from the command line
    @app.cli.command('init-db')
    def init_db_command():
        """Clear existing data and create new tables."""
        with app.app_context():
            db.drop_all() # Be careful with this in production!
            db.create_all()
            print('Initialized the database.')

    # --- Simple Test Route (optional) ---
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

