import logging
import os

from flask import Flask
from flask_restx import Api

from app.SQIP import SqipApi


def create_app(test_config=None):
    # create and configure the app
    flask_app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        flask_app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        flask_app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(flask_app.instance_path)
    except OSError:
        pass

    return flask_app


app = create_app()
api = Api(version="0.0.1", title="SQIP API", description="An API for SQIP")
api.add_namespace(SqipApi)
api.init_app(app)

