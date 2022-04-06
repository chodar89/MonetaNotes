import os

from flask_openapi3 import Info, OpenAPI

from src.api import ping_bp
from src.extensions import db, jwt


def create_app(script_info=None):
    info = Info(title="MonetaNotes", version="1.0.0")

    # instantiate the app
    app = OpenAPI(__name__, info=info)

    # set flask app config
    app.config.from_object(os.getenv("APP_SETTINGS"))

    # init extensions with flask app
    db.init_app(app)
    jwt.init_app(app)

    # register blueprints
    app.register_api(ping_bp)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
