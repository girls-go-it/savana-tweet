#!/Users/sergiuterman/stuff/projects/playground/savanna-tweet/venv/bin/python
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask import render_template
from models import db
app = Flask(__name__)
bootstrap = Bootstrap()

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/feed')
def feed():
    return render_template('feed.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
bootstrap.init_app(app)
db.init_app(app)

def create_all():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
