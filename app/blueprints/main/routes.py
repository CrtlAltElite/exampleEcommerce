from flask.globals import request
from . import bp as main
from flask import render_template, current_app as app, url_for
from app.blueprints.products.routes import is_empty
from ..products.models import Product

##################################################################
############### MAIN INDEX PAGE  ########################
##################################################################


@main.route('/')
@main.route('/index')
# The main route for Scamazon, expected URL entry point.
def index():
    # Paginate the index page
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(
        page, app.config['ITEMS_PER_PAGE'], False)
    next_url = url_for('main.index', page=products.next_num) \
        if products.has_next else None
    prev_url = url_for('main.index', page=products.prev_num) \
        if products.has_prev else None
    # Validate if there are items in the cart to determine which cart icon to display
    cart_empty = is_empty()
    return render_template('index.html', products=products.items, next_url=next_url,
                           prev_url=prev_url, cart_empty=cart_empty)
