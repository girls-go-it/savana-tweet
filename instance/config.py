import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
SECRET_KEY = "megasecretkey"