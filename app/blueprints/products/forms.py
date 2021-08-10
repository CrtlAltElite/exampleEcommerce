from flask.app import Flask
from wtforms import SubmitField
from flask_wtf import FlaskForm

# Empty form provided to enable CSRF protection on product info page
class AddToCartForm(FlaskForm):
    submit = SubmitField()

# Empty form provided to enable CSRF protection on cart page
class CartForm(FlaskForm):
    remove_item = SubmitField()
    clear_cart = SubmitField()
    check_out = SubmitField()
