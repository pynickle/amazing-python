from wtforms import validators
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField


class SpiderForm(FlaskForm):
    page_number_begin = IntegerField("输入开始页数", [validators.DataRequired()])
    page_number_all = IntegerField("输入爬取页数", [validators.DataRequired(), validators.Length(1, 2240)])
    submit = SubmitField("开始", render_kw = {"class": "button is-link is-outlined is-rounded"})
