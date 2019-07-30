from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class HandForm(FlaskForm):
    words = TextAreaField("输入单词", [validators.DataRequired("")])
    submit = SubmitField("提交")