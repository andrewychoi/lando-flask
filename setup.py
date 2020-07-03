import json

from lando import create_app

from lando.models import db, User


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
        with open("lando/user_fixtures.json") as infile:
            user_fixtures = json.load(infile)
            users = [User(**fixture) for fixture in user_fixtures]
            for user in users:
                db.session.add(user)
            db.session.commit()
