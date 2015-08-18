from flask import render_template, request
from forms import LoginForm, ProfileForm, PostForm, SignupForm
from werkzeug import secure_filename
import os, sys
from flask import render_template, redirect, url_for
from app.models import Animal, Post, Like
from app import app, login_manager
from flask.ext.login import current_user, login_user, login_required, logout_user
from sqlalchemy import desc
from time import time

from app import db
from app import app

from pprint import pprint

app.secret_key = 'development key'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/posts/<int:post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get(post_id)
    Like(animal=current_user, post=post).save()
    return redirect(url_for('feed'))

@app.route('/posts/<int:post_id>/unlike', methods=['POST'])
@login_required
def unlike_post(post_id):
    like = Like.query.filter_by(animal=current_user, post_id=post_id).first()
    db.session.delete(like)
    db.session.commit()
    return redirect(url_for('feed'))

@login_manager.user_loader
def load_animal(animal_id):
    return Animal.query.get(animal_id)

@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user.username)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_animal = Animal(username=form.username.data, email=form.email.data)
        new_animal.set_password(form.password.data)
        new_animal.save()
        login_user(new_animal, remember=True)
        return redirect(url_for("index"))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

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
    form = PostForm(request.form)
    posts = Post.query.order_by(desc(Post.created_at)).all()
    for post in posts:
        post.date = {
            'fullDate' : str(post.created_at),
            'day'      : str(post.created_at.day),
            'month'    : str(post.created_at.month),
            'year'     : str(post.created_at.year),
            'time'     : ((str(post.created_at)).split(' ')[1]).split('.')[0]
        }
        post.date['fullDate'] = post.date['fullDate'].split(' ')[0]
    months = {'1':'Ian', '2':'Feb', '3':'Mar', '4':'Apr', '5':'Mai', '6':'Iun', '7':'Iul', '8':'Aug', '9':'Sep', '10':'Oct', '11':'Noi', '12':'Dec'}
    return render_template('feed.html', form=form, posts=posts, months=months)

@app.route('/profile', methods=['GET'])
@login_required
def profile_get():
    form = ProfileForm()
    form.name.data = current_user.name
    form.about_me.data = current_user.about_me
    form.fur_color.data = current_user.fur_color
    form.email.data = current_user.email
    form.animal_type.data = current_user.animal_type
    return render_template('profile.html', form = form, photo = '')

@app.route('/profile', methods=['POST'])
@login_required
def profile_post():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.about_me = form.about_me.data
        current_user.fur_color = form.fur_color.data
        current_user.email = form.email.data
        current_user.animal_type = form.animal_type.data

        if form.image.data:
            image = 'images/'+secure_filename(str(time())+form.image.data.filename)
            form.image.data.save(app.config['UPLOADS'] + image)
            current_user.image_url = image

        current_user.save()
        return redirect(url_for("index"))
    return render_template('profile.html', form=form)



@app.route('/create-feed', methods=['POST'])
@login_required
def created_feed():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data, animal=current_user)
        if form.image.data:
            image = 'images/'+secure_filename(str(time())+form.image.data.filename)
            form.image.data.save(app.config['UPLOADS'] + image)
            post.image_url = image

        post.save()
    return redirect(url_for('feed'))
