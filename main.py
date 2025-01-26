from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
import bleach
from .forms import LoginForm, RegisterForm
from .__init__ import create_app
from .database import db
from .database_objects import Users

app = create_app()
bootstrap = Bootstrap5(app=app)

with app.app_context():
    db.create_all()

@app.route('/', methods=["GET", "POST"])
def landing_page():
    """This will be the landing page when users navigate to the site. A login page."""

    form = LoginForm()
    if form.validate_on_submit():
        email = db.session.execute(db.select(Users).where(Users.email == form.email.data)).scalar()
        if not email:
            flash("Sorry, we could not find an account. Please create an account instead.")
            return redirect(url_for("register"))
        else:
            if email:
                return "hello"
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    """This will handle the user registration."""

    form = RegisterForm()
    if form.validate_on_submit():
        email = db.session.execute(db.select(Users).where(Users.email == form.email.data)).scalar()
        if email:
            flash("You've already signed up with that email. Please login instead.")
            return redirect(url_for("landing_page"))
        else:
            password = generate_password_hash(bleach.clean(form.password.data), method="pbkdf2:sha256", salt_length=16)
            user = Users(bleach.clean(form.email.data), password, bleach.clean(form.username.data))
            db.session.add(user)
            db.session.commit()
            login_user(user=user)
            return redirect(url_for("landing_page"))
        
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
