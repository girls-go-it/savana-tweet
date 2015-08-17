from app import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from flask.ext.login import UserMixin

class Animal(UserMixin, db.Model):
    __tablename__ = 'animal'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    fur_color = db.Column(db.String(255))
    # animal_type = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    username = db.Column(db.String(80), unique=True)
    h_password = db.Column(db.String(1000))
    about_me = db.Column(db.String(500))

    def __repr__(self):
        return '<User %s>' % self.name

    def set_password(self, password):
        self.h_password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def likes_post(self, post):
        like = Like.query.filter_by(animal=self, post=post).first()
        return like is not None

    def check_password(self, password):
        return check_password_hash(self.h_password, password)

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Unicode(500))
    image_url = db.Column(db.String(255))
    likes = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    animal_id = db.Column(db.Integer(), db.ForeignKey('animal.id'))
    animal = db.relationship('Animal')
    likes = relationship('Like')

    def __repr__(self):
        return '<User %d>' % self.id

    def save(self):
        db.session.add(self)
        db.session.commit()


class Like(db.Model):
    __tablename__ = 'like'

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer(), db.ForeignKey('animal.id'))
    animal = db.relationship('Animal')
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
    post = db.relationship('Post')

    def __init__(self, animal, post):
        self.animal = animal
        self.post = post

    def __repr__(self):
        return '<Like %d>' % self.id

    def save(self):
        db.session.add(self)
        db.session.commit()

