from flask import Flask

from lando.models import db


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
        # quiet error message
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_DATABASE_URI="sqlite:////tmp/test.db"
    )

    db.init_app(app)

    @app.route("/")
    def hello():
        return "Hello World!"

    return app
