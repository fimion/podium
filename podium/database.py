from podium import app, meetup_blueprint
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy(app)


class User(db.Model, OAuthConsumerMixin):
    """
    Our User model.
    """

    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(60))
    github_name = db.Column(db.String(60))




meetup_blueprint.backend = SQLAlchemyBackend(User, db.session)

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