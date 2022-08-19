from flask import Flask, render_template, request, flash
from app import app
from app.models import Post, db
from app import forms




app.config["SECRET_KEY"] = "nininini"


@app.route("/")
def homepage():
    all_posts = Post.query.filter_by(is_public=True).order_by(Post.pub_date.desc())
    return render_template("main_page.html", all_posts=all_posts)



@app.route("/edit-post/<post_id>", methods = ["GET", "POST"])
def edit_and_add_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    form = forms.PostForm(obj=post)
    errors = None
    if request.method == "POST":
        if form.validate_on_submit():
            if post_id == 'new_id':
                new_post = Post(
                    title=form.title.data,
                    post_content=form.post_content.data,
                    is_public=form.is_public.data
                )
                db.session.add(new_post)
                flash(f"Wpis o tytule {form.title.data} został opublikowany")
            elif post_id == str(post.id):
                print("final up")
                form.populate_obj(post)
                db.session.commit()
                flash(f"Wpis o tytule {form.title.data} został zmodyfikowany")
            db.session.commit()
        else:
            errors = form.errors
    return render_template("post_form.html", form=form, errors=errors)

