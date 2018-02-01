from flask import Flask
from model import db

import api_1_0


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object("config")
    db.init_app(app)
    app.register_blueprint(api_1_0.bp, url_prefix='/api/1_0')
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
