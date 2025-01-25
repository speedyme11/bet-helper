from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(message="This field can not be left blank.")])
    password = PasswordField("Password", validators=[DataRequired(message="This field can not be left blank.")])
    submit = SubmitField("Sign In")