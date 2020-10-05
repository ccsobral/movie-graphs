import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE='/home/csobral/MovieGraphs/moviegraphs.db'
    )

    from . import api
    app.register_blueprint(api.bp)

    return app