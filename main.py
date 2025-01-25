from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm
from database_objects import db


app = Flask(__name__)
app.config['SECRET_KEY'] = "afdsf4ds56f41ds6f1ds5f"
bootstrap = Bootstrap5(app=app)

@app.route("/", methods=["GET"])
def landing_page():
    form = LoginForm()
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
