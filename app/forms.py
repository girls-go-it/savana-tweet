from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, SubmitField, SelectField, FileField, PasswordField
from wtforms.validators import Required

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



class ProfileForm(Form):
    name = TextField("Name")
    fur_color = TextField("Fur color")
    email = TextField("Email")
    animal_type = SelectField('Type', choices=[('carnivor', 'Carnivor'), ('ierbivor','Ierbivor'), ('omnivor','Omnivor')])
    image_url = FileField('Photo'),
    submit = SubmitField("Save")


class PostForm(Form):
    content = TextField("Content")
    image_url = FileField("Photo")
    submit = SubmitField("Save")

