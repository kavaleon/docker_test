from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_redis import FlaskRedis
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
redis_store = FlaskRedis()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    redis_store.init_app(app)

    from app import routes
    app.register_blueprint(routes.bp)

    return app