from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, SubmitField, SelectField, FileField
from wtforms.validators import Required
 
from app import app

class LoginForm(Form):
    username = TextField("Username")
    password = TextField("Password")
    submit = SubmitField("Log in")

class ProfileForm(Form):
    name = TextField("Name")
    fur_color = TextField("Fur color")
    email = TextField("Email")
    animal_type = SelectField('Type', choices=[('carnivor', 'Carnivor'), ('ierbivor','Ierbivor'), ('omnivor','Omnivor')])
    image_url = FileField('Photo'),
    submit = SubmitField("Save")
