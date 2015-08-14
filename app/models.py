from app import db

class Animal(db.Model):
    __tablename__ = 'animal'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    fur_color = db.Column(db.String(255))
    animal_type = db.Column(db.String(255))
    image_url = db.Column(db.String(255))

    def __init__(self, email, name, fur_color, animal_type, image_url=''):
        self.email = email
        self.name = name
        self.fur_color = fur_color
        self.animal_type = animal_type
        self.image_url = image_url

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Unicode(500))
    image_url = db.Column(db.String(255))
    likes = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), default=db.func.now())
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
