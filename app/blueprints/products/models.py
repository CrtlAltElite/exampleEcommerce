from app import db

# Manages all the products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    sm_image_url = db.Column(db.String(250), nullable=False)
    lg_image_url = db.Column(db.String(250), nullable=False)

    def __init__(self, name, desc, price, sm_image_url, lg_image_url,):
        self.name = name
        self.desc = desc
        self.price = price
        self.sm_image_url = sm_image_url
        self.lg_image_url = lg_image_url

# Join table the manages the relationship between an individual user and an individual product
# qty is currently set with 1 via the Add to Cart button on the Product page.  Future implementation 
# for Javascript
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, product_id, qty, user_id):
        self.product_id = product_id
        self.qty = qty
        self.user_id = user_id
