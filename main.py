#!/Users/sergiuterman/stuff/projects/playground/savanna-tweet/venv/bin/python
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(debug=True)
