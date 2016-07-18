from wtforms import (
    BooleanField,
    TextField,
    TextAreaField,
    PasswordField,
    validators,
    SubmitField,
    FileField,
    IntegerField
)
from wtforms.fields.html5 import EmailField
from flask.ext.wtf import Form


class RegisterForm(Form):
    email = TextField('Email', [validators.Length(min=4, max=35)])
    first_name = TextField('First Name', [validators.Length(min=4, max=35)]) 
    last_name = TextField('Last Name', [validators.Length(min=4, max=35)])
    password = PasswordField('Choose Password', [
        validators.Required(),
        validators.EqualTo('password_confirm', message='Passwords must match')
    ])
    password_confirm = PasswordField('Repeat Password')
    submit = SubmitField('Register')

class LoginForm(Form):
    email = EmailField('Email', [validators.Length(min=4, max=35)])
    password = PasswordField('Password', [validators.Length(min=4, max=35)])
    remember_me = BooleanField('Remember me')
    remember_my_password = BooleanField('Remember my password')
    sign_me_in_automatically = BooleanField('Sign me in automatically')
    submit = SubmitField('Login')
