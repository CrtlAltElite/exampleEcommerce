from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from time import time
from flask import current_app as app
import jwt


@login.user_loader
# Default user_loader function is provided by and required for Flask_Login to work
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(75), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(5), nullable=False)

    def __init__(self, username, password, email, address, city, state, zip_code):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return f'<User | {self.username}>'
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def update_user(self, username, email, address, city, state, zip_code):
        self.username = username
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        db.session.commit()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    #The next two methods provide a JSON Web Token (JWT) which is hashed
    # and allows for an email to be signed and sent.  The tokens are "fairly" secure
    # but should only be valid for a short period of time in case a user's e-mail
    # or traffic is compromised
    def get_reset_password_token(self, expires_in=600):
        # returns a jwt token object with a validity of 10 minutes (600 seconds)
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        # Verifies the jwt token is valid
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
