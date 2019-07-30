from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import TextField


class Form(FlaskForm):
    name = TextField("", [validators.DataRequired("")])
