from flask.ext.bootstrap import Bootstrap
from flask import render_template

from app import app

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
