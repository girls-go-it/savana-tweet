from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)

db = SQLAlchemy(app)

from app import views, models

