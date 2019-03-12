from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    people = db.relationship("Person", back_populates="user")
    meetings = db.relationship("Meeting", back_populates="user")
    notes = db.relationship("Note", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.username


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    frequency = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", back_populates="people")

    meetings = db.relationship("Meeting", back_populates="person")
    notes = db.relationship("Note", back_populates="person")

    def __repr__(self):
        return '<Person %r>' % self.name


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", back_populates="meetings")
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    person = db.relationship("Person", back_populates="meetings")
    datetime = db.Column(db.DateTime)
    note = db.Column(db.String)

    def __repr__(self):
        return '<Meeting [%r] %r [%r]>' % (
            self.user, self.person, self.datetime.isoformat()
        )


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", back_populates="notes")
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    person = db.relationship("Person", back_populates="notes")

    datetime = db.Column(db.DateTime)
    text = db.Column(db.String)

    def __repr__(self):
        return '<Note [%r] %r [%r]>' % (
            self.user, self.person, self.datetime.isoformat()
        )
