from . import db
import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),  nullable=False, unique=True)
    post_content = db.Column(db.String(100),  nullable=False)
    pub_date = db.Column(db.DateTime(),  nullable=False, default=datetime.datetime.utcnow)
    is_public = db.Column(db.Boolean(),  default=False)
