from flask import Flask, render_template, request, flash , session, url_for, redirect
from app import app
from app.models import Post, db
from app import forms
from app.forms import LoginForm
import functools
import config

app.config["SECRET_KEY"] = "nininini"

def login_required(view_func):
   @functools.wraps(view_func)
   def check_permissions(*args, **kwargs):
       if session.get('logged_in'):
           return view_func(*args, **kwargs)
       return redirect(url_for('login', next=request.path))
   return check_permissions

@app.route("/")
def homepage():
    all_posts = Post.query.filter_by(is_public=True).order_by(Post.pub_date.desc())
    return render_template("main_page.html", all_posts=all_posts)



@app.route("/edit-post/<post_id>", methods = ["GET", "POST"])
@login_required
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
                if new_post.is_public:
                    flash(f"Wpis o tytule {form.title.data} został opublikowany")
                else:
                    flash(f"Wpis o tytule {form.title.data} został zapisany do zakładki Niepubliczne wpisy")
            elif post_id == str(post.id):
                form.populate_obj(post)
                flash(f"Wpis o tytule {form.title.data} został zmodyfikowany")
            db.session.commit()
        else:
            errors = form.errors
    return render_template("post_form.html", form=form, errors=errors)


@app.route("/login/", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   errors = None
   next_url = request.args.get('next')
   if request.method == 'POST':
       if form.validate_on_submit():
           session['logged_in'] = True
           session.permanent = True  # Use cookie to store session.
           flash(f'użytkowniku {form.username.data} zostałeś pomyślnie zalogowany.', 'success')
           return redirect(next_url or url_for('homepage'))
       else:
           errors = form.errors
   return render_template("login_form.html", form=form, errors=errors)

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
   if request.method == 'POST':
       session.clear()
       flash('Zostałeś pomyślnie wylogowany.', 'success')
   return redirect(url_for('homepage'))



@app.route("/unpublic")
@login_required
def list_drafts():
    unpublic_posts = Post.query.filter_by(is_public=False).order_by(Post.pub_date.desc())
    return render_template("drafts.html", all_posts=unpublic_posts)


@app.route("/delete-post/<post_id>", methods = [ "POST"])
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id)
    post.delete()
    db.session.commit()
    return redirect(url_for('homepage'))

