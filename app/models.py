from app import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

class Animal(UserMixin, db.Model):
    __tablename__ = 'animal'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    fur_color = db.Column(db.String(255))
    animal_type = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    username = db.Column(db.String(80), unique=True)
    h_password = db.Column(db.String(1000))
    about_me = db.Column(db.String(500))

    # def __init__(self, email, name, username, fur_color, animal_type, password, image_url=''):
    #     self.email = email
    #     self.name = name
    #     self.username = username
    #     self.fur_color = fur_color
    #     self.animal_type = animal_type
    #     self.image_url = image_url
    #     self.set_password(password)
    def __init__(self, username, password):
        self.username = username
        self.h_password = generate_password_hash(password)

    def __repr__(self):
        return '<User %s>' % self.name

    def set_password(self, password):
        self.h_password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.h_password, password)


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Unicode(500))
    image_url = db.Column(db.String(255))
    likes = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now())
    animal_id = db.Column(db.Integer(), db.ForeignKey('animal.id'))
    animal = db.relationship('Animal')

    def __init__(self, content, animal_id, image_url=""):
        self.content = content
        self.animal_id = animal_id
        self.image_url = image_url

    def like(self):
        if not self.likes:
            self.likes = 1
        else:
            self.likes += 1
        self.save()

