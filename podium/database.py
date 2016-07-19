from podium import app, meetup_blueprint
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_dance.contrib.meetup import meetup
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, UserMixin

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    """
    This is our user model. maybe this should be profile?
    """
    id = db.Column(db.Integer, primary_key=True)
    meetup_id = db.Column(db.Integer, unique=True)


class Oauth(db.Model, OAuthConsumerMixin):
    """
    This model handles our Oauth2 Logins
    """
    user_id = db.Column(db.Integer, db.ForeignKey(User.meetup_id))
    user = db.relationship(User)

    def __init__(self):
        resp = meetup.get('members/self')
        assert resp.ok
        self.user_id = resp.json()['id']


meetup_blueprint.backend = SQLAlchemyBackend(Oauth, db.session, user=current_user)


class Event(db.Model):
    """
    Refers to a Meetup.com Event.
    Placeholder for more information in the future.
    """

    id = db.Column(db.Integer, primary_key=True)
    meetup_id = db.Column(db.Integer)

    def __init__(self, meetup_id):
        self.meetup_id = meetup_id


class Presentation(db.Model):
    """
    Presentations. Will refer to an Event and a User.
    """

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User,
                           backref=db.backref('presentations', lazy='dynamic'))
    event_id = db.Column(db.Integer, db.ForeignKey(Event.id))
    event = db.relationship(Event,
                            backref=db.backref('presentations', lazy='dynamic'))
    title = db.Column(db.String)