from flask import Flask, render_template, request
from app import app
from app.models import Post, db
from app import forms




app.config["SECRET_KEY"] = "nininini"


@app.route("/")
def homepage():
    all_posts = Post.query.filter_by(is_public=True).order_by(Post.pub_date.desc())
    return render_template("main_page.html", all_posts=all_posts)


@app.route("/post/", methods=["GET","POST"])
def add_post():
    form = forms.PostForm()
    errors = None
    if request.method == "POST":
        if form.validate_on_submit():
            new_post = Post(
                form.title.data,
                form.post_content.data,
                is_public=form.is_public.data
            )
            db.session.add(new_post)
            db.session.commit()
        else:
            errors = form.errors
    return render_template("post_form.html", form=form, errors=errors)



