from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Config
from app.models.models import db
from app.auth.routes import auth_bp
from app.tasks.routes import tasks_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/api')

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
