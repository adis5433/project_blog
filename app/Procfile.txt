heroku ps:scale web=2
web: flask db upgrade; gunicorn blog:app



