from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators


class ContactForm(Form):
    name = StringField("Name",  [validators.InputRequired("Please enter your name.")])
    email = StringField("Email",  [validators.InputRequired("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    message = TextAreaField("Message",  [validators.InputRequired("Please enter a message.")])
    submit = SubmitField("Send")
