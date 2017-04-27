from flask_wtf import Form
from wtforms import StringField, SubmitField

class SignupForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')
    submit = SubmitField('Sign up')
