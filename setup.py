from lando import create_app

from lando.models import db


if __name__ == "__main__":
    app = create_app()
    db.init_app(app)
    db.create_all()
