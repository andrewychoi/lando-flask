from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_login import login_required

bp = Blueprint("meetings", __name__,)

@bp.route("/", methods=["GET"])
@login_required
def hello():
    return "Meetings home for {}!".format("USER GOES HERE")


@bp.route("/<meeting_id>", methods=["GET"])
def meeting_detail(meeting_id):
    return "Showing meetings for id {}".format(meeting_id)


@bp.route("/", methods=["POST"])
def meeting_create():
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return "Creating meetings for id {}".format(meeting_id)
    # return user_schema.jsonify(user)
