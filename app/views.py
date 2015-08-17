from flask import render_template, request
from forms import LoginForm, ProfileForm
from werkzeug import secure_filename
from pprint import pprint
from flask import redirect, url_for
import os, sys
from flask import render_template, g, redirect, url_for
from .models import Animal
from app import app, login_manager
from flask.ext.login import current_user, login_user, login_required, logout_user
from sqlalchemy import desc
from app.models import Post
from app import db
from flask.ext import bcrypt

from app import app

app.secret_key = 'development key'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/posts/<int:post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    Post.query.get(post_id).like()
    return redirect(url_for('feed'))

@login_manager.user_loader
def load_animal(animal_id):
    return Animal.query.get(animal_id)

@app.before_request
def before_request():
    try:
        g.user = current_user
        print 'current user'
    except Exception:
        print "nobody logged in!"


@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user.username)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(sys.path[0], app.config['UPLOAD_FOLDER'], filename))
        print filename
        return render_template('profile.html', data={'photo':filename})

    form = LoginForm(request.form)
    return render_template('login.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = Animal.query.filter_by(username=form.username.data).first()
        login_user(user, remember=True)
        return redirect(url_for("index"))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template('base.html')

@app.route('/feed')
@login_required
def feed():
    posts = Post.query.order_by(desc(Post.created_at)).all()
    return render_template('feed.html', posts=posts)

@app.route('/profile', methods=['GET'])
@login_required
def profile_get():
    form = ProfileForm()
    return render_template('profile.html', data={'form':form,'photo':''})

@app.route('/profile', methods=['POST'])
@login_required
def profile_post():
    try:
        file = request.files['file']
    except KeyError:
        file = None

    form = ProfileForm(request.form)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(sys.path[0], app.config['UPLOAD_FOLDER'], filename))
        print filename
        return render_template('profile.html', data={'form':form,'photo':filename})

    return render_template('profile.html', data={'form':form})
