import logging
import pytest
import os
import tempfile

import lando
from lando.models import User


@pytest.fixture
def database():
    db_fd, lando.app.config['DATABASE'] = tempfile.mkstemp()
    lando.app.config['TESTING'] = True

    with lando.app.app_context():
        lando.init_db()

    yield database

    # teardown
    os.close(db_fd)
    os.unlink(lando.app.config['DATABASE'])


@pytest.fixture
def user_fixtures(database):
    from lando.models import db
    users = [User(username="andrew", email="andrew@choi.com")]
    for user in users:
        db.session.add(user)
    db.session.commit()

    yield

    # teardown
    for user in User.query.all():
        db.session.remove(user)
    db.session.commit()


def test_users(user_fixtures):
    logging.info(User.query.all())
