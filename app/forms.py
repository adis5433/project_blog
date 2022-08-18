from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, BooleanField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    post_content = TextAreaField('content', validators=[DataRequired()])
    is_public = BooleanField('is public?')

