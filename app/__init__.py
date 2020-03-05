import os

from flask import Flask

from app.providers.kubemq import KubeMQProvider
from app.providers.qldb import QLDBProvider


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/version')
    def version():
        return 'SQIP v-0.0.1'

    @app.route('/health')
    def health():
        return 'OKAY'

    qldb_provider = QLDBProvider.as_view("qldb_provider")
    app.add_url_rule('/qldb/', defaults={}, view_func=qldb_provider, methods=['GET', ])
    app.add_url_rule('/qldb/', defaults={}, view_func=qldb_provider, methods=['POST', ])

    kubemq_provider = KubeMQProvider.as_view("kubemq_provider")
    app.add_url_rule('/kubemq/', defaults={}, view_func=kubemq_provider, methods=['GET', ])
    app.add_url_rule('/kubemq/', defaults={}, view_func=kubemq_provider, methods=['POST', ])

    return app
