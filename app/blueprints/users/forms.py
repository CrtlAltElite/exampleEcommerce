from flask_wtf import FlaskForm
from .models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError


class UserForm(FlaskForm):
    # Form to validate user registration information
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Shipping Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

    # Flask_WTForms runs this validation script automatically.
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(
                'This username is not available, please choose another')

    # Flask_WTForms runs this validation script automatically.
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
                'A user account already exists for this email address')


class UserUpdateForm(FlaskForm):
    # Form to update user registration information
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Shipping Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    submit = SubmitField('Submit')

    # Because we are trying to prevent duplicate accounts, validation below requires
    # the storage of what data is already in the form when it loads, if the user doesn't
    # change the data, don't validate it.  If the user does change it, make sure that
    # user name and e-mail isn't already taken by another user.
    def __init__(self, original_username, original_email, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    # Flask_WTForms runs this validation script automatically.
    def validate_username(self, username):
        print("test user")
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError(
                    'This username is not available, please choose another')

    # Flask_WTForms runs this validation script automatically.
    def validate_email(self, email):
        print("test email")
        if email.data != self.original_email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError(
                    'A user account already exists for this email address')


class LoginForm(FlaskForm):
    # Form to log users in
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ResetPasswordRequestForm(FlaskForm):
    # Form to request a passsword reset
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    # Form to reset the password, triggered from the reset email
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
