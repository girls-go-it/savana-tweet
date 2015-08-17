from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, BooleanField, SubmitField, SelectField, FileField, PasswordField
from wtforms.fields import TextField, BooleanField, SubmitField, SelectField, FileField, PasswordField
from wtforms.validators import Required, EqualTo
from flask.ext.wtf.html5 import EmailField

from app import app
from app.models import Animal

class LoginForm(Form):
    username = TextField("Username", [Required()])
    password = PasswordField("Password", [Required()])
    submit = SubmitField("Log in")

    def validate(self):
        if not Form.validate(self):
            return False

        user = Animal.query.filter_by(username = self.username.data).first()
        if user is None:
            self.username.errors.append("That username does not exist!")
            return False
        if not user.check_password(self.password.data):
            self.password.errors.append("The password is incorrect!")
            return False
        return True

class SignupForm(Form):
    username = TextField("Username", [Required()])
    email = EmailField("Email", [Required()])
    password = PasswordField("Password", [Required()])
    password_confirmation = PasswordField("Password Confirmation", [Required(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Sign up")

    def validate(self):
        if not Form.validate(self):
            return False

        user = Animal.query.filter_by(username=self.username.data).first()
        if user is not None:
            self.username.errors.append("Username " + self.username.data + " already exist")
            return False

        user = Animal.query.filter_by(email=self.email.data).first()
        if user is not None:
            self.email.errors.append("Email " + self.email.data + " already exist")
            return False

        return True

class ProfileForm(Form):
    name = TextField("Name")
    about_me = TextAreaField("Tell us about yourself")
    fur_color = TextField("Fur color")
    email = TextField("Email")
    # animal_type = SelectField('Type', choices=[('carnivor', 'Carnivor'), ('ierbivor','Ierbivor'), ('omnivor','Omnivor')])
    # image_url = FileField('Photo'),
    submit = SubmitField("Save")


class PostForm(Form):
    content = TextField("Content")
    image_url = FileField("Photo")
    submit = SubmitField("Save")

