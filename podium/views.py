# Put all Flask views in here, as suggested by:
# http://flask.pocoo.org/docs/0.11/patterns/packages/
from podium import app
from flask import render_template, redirect, url_for
from flask_dance.contrib.meetup import meetup
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from flask_login import current_user


@app.errorhandler(TokenExpiredError)
def handle_tokenexpired(e):
    return redirect(url_for('login/meetup'))


@app.context_processor
def inject_meetup_user():
    """
    Allows templates to get the current user information. This is done specifically so
    the layout template can access this information.

    :return:
    """
    meetup_user = None
    cur_user = current_user()
    if meetup.authorized:
        resp = meetup.get("member/self")
        assert resp.ok
        meetup_user = resp.json()
        if cur_user.meetup_id != meetup_user['id']:
            return redirect(url_for('login/register'))

    return dict(meetup_user=meetup_user)


@app.route('/')
def index():
    """
    Index view. This will be the primary page people see.
    :return:
    """
    return render_template("index.html")
