from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')


# Bootstrap instantiation for the app
bootstrap = Bootstrap(app)

# Database Connection instantiation
db = SQLAlchemy(app)

# Login Manager stuff
lm = LoginManager(app)
lm.login_view = 'login'
lm.login_message = 'Please consider logging in. You don\'t have access here!'



from app import views, models

