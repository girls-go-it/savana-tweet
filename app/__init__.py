from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/feed')
def feed():
    return render_template('feed.html')
