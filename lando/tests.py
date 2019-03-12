import logging

from flask_testing import TestCase

from lando.models import db, User
from lando import create_app


class UserTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/lando.db"
    TESTING = True

    def create_app(self):
        app = create_app(self)
        return app

    def setUp(self):
        db.init_app(self.app)
        db.drop_all()
        db.create_all()

        users = [User(username="andrew", email="andrew@choi.com")]
        for user in users:
            db.session.add(user)
        db.session.commit()

    def test_users(self):
        logging.error(User.query.all())

    def tearDown(self):
        for user in User.query.all():
            db.session.delete(user)
        db.session.commit()
