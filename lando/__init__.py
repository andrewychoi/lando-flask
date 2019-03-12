from flask import Flask

from lando.models import db


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config:
        app.config.from_object(test_config)
    else:
        app.config.from_mapping(
            # a default secret that should be overridden by instance config
            SECRET_KEY='dev',
            SQLALCHEMY_DATABASE_URI="sqlite:////tmp/test.db"
        )

    # quiet error messages on startup
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def hello():
        return "Hello World!"

    return app
