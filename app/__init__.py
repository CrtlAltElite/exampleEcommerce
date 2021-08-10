from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

# Initialize package instances
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()

# Create the application using app factory pattern, 
# create from confit file
def create_app(config_class=Config):
    # Create Flask app
    app = Flask(__name__)
    # configure Flask app
    app.config.from_object(config_class)
    # attach package instances to application
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    # Flask login config options
    login.login_view = 'users.login'
    login.login_message = 'Please login to access the shopping cart'
    login.login_message_category = 'warning'
    # register blueprints with Flask app
    with app.app_context():
        from app.blueprints.users import bp as users
        app.register_blueprint(users)

        from app.blueprints.main import bp as main
        app.register_blueprint(main)

        from app.blueprints.products import bp as main
        app.register_blueprint(main)
    # return fully configured app instance to app.py 
    return app
