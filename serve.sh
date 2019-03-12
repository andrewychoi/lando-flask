#! /bin/bash

export FLASK_APP="lando"
export FLASK_ENV="development"

source venv/bin/activate
flask run
