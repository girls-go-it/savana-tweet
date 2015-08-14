from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, SubmitField, SelectField, FileField
from wtforms.validators import Required
 
from app import app
from app.models import Animal

class LoginForm(Form):
    username = TextField("Username")
    password = TextField("Password")
    submit = SubmitField("Log in")

    def validate(self):

        user = Animal.query.filter_by(username = self.username.data.lower()).first()
        if not user:
            self.username.errors.append("That username does not exist!")
            return False
        else:
            return True

    def validate_on_submit(self):

        user = Animal.query.filter_by(username = self.username.data.lower()).first()
        if user is not None:
            self.username.errors.append("That username is already taken!")
            return False
        else:
            return True

class ProfileForm(Form):
    name = TextField("Name")
    fur_color = TextField("Fur color")
    email = TextField("Email")
    animal_type = SelectField('Type', choices=[('carnivor', 'Carnivor'), ('ierbivor','Ierbivor'), ('omnivor','Omnivor')])
    image_url = FileField('Photo'),
    submit = SubmitField("Save")
