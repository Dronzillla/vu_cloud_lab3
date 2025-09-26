from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Dependency injection
db = SQLAlchemy()


def create_app(config_class="config.config.DevelopmentConfig"):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)

    # Set up db
    db.init_app(app)

    # Import and register all blueprints
    from blueprintapp.blueprints.core.routes import core
    from blueprintapp.blueprints.todos.routes import todos
    from blueprintapp.blueprints.api.routes import api

    # Register blueprints
    app.register_blueprint(core, url_prefix="/")
    app.register_blueprint(todos, url_prefix="/todos")
    app.register_blueprint(api, url_prefix="/api")

    migrate = Migrate(app, db)
    # To create db go to blueprintapp folder where app.py is
    # flask db init
    # flask db migrate
    # flask db upgrade

    return app
