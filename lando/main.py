from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint("main", __name__,)


@bp.route("/")
def hello():
    return "Hello World!"


@bp.route("/login", methods=["GET"])
def login():
    return "Needs to login"

@bp.route("/login", methods=["POST"])
def login():
    return "Needs to login"


@bp.route("/home")
def home():
    td = {
        "tabs": {
            "friends": "Lando helps you keep up with friends!",
            "family": "Lando helps you keep up with family!",
            "colleagues": "Lando helps you keep up with colleagues!",
            "mentors": "Lando helps you keep up with mentors!",
        },
        "test": {}
    }
    return render_template("home.html", **td)
