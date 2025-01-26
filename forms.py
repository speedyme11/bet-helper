from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, Label
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(message="This field can not be left blank.")])
    password = PasswordField("Password", validators=[DataRequired(message="This field can not be left blank.")])
    submit = SubmitField("Sign In")

class RegisterForm(FlaskForm):
    username = StringField("Create username", validators=[DataRequired(), Length(min=2, max=100,
                                                                                 message="Field must be between %(min)d characters and %(max)d characters.")])
    email = EmailField("Enter email", validators=[DataRequired()])
    password = PasswordField("Create password", validators=[DataRequired(), EqualTo('confirm_password', message='Passwords must match.')])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Create Account")