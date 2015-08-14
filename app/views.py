from flask import render_template, request
from forms import LoginForm, ProfileForm
from werkzeug import secure_filename
from pprint import pprint
from flask import redirect, url_for
import os, sys

from sqlalchemy import desc
from app.models import Post
from app import db

from app import app 


app.secret_key = 'development key'

def allowed_file(filename):
    return '.' in filename and \
        	filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    Post.query.get(post_id).like()
    return redirect(url_for('feed'))

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/login', methods=['GET'])
def login_get():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/login', methods=['POST'])
def login_post():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(sys.path[0], app.config['UPLOAD_FOLDER'], filename))
        print filename
        return render_template('profile.html', data={'photo':filename})

    form = LoginForm(request.form)
    return render_template('login.html', form=form)

@app.route('/feed')
def feed():
    posts = Post.query.order_by(desc(Post.created_at)).all()
    return render_template('feed.html', posts=posts)

@app.route('/profile', methods=['GET'])
def profile_get():
    form = ProfileForm()

    return render_template('profile.html', data={'form':form,'photo':''})

@app.route('/profile', methods=['POST'])
def profile_post():
    file = request.files['file']
    print file
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(sys.path[0], app.config['UPLOAD_FOLDER'], filename))
        print filename

    form = ProfileForm(request.form)
    return render_template('profile.html', data={'form':form,'photo':filename})
