from flask import Flask, request, Blueprint
from .book.controller import books
from .extension import db
from .models import *

def create_app(config_file= "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(books)
    return app