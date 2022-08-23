from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import StringField,TextAreaField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from config import Config


class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    post_content = TextAreaField('content', validators=[DataRequired()])
    is_public = BooleanField('is public?')

class LoginForm(FlaskForm):

   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])

   def validate_username(self, field):
       if field.data != Config.ADMIN_USERNAME:
           raise ValidationError("Invalid username")
       return field.data

   def validate_password(self, field):
       if field.data != Config.ADMIN_PASSWORD:
           raise ValidationError("Invalid password")
       return field.data