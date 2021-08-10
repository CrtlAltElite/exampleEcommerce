from app import create_app, db

# Launch App factory
app = create_app()




# The following code allows you to start the Flask shell with some items already imported and ready to run.
# It's primary purpose is to allow me to build the SQLite database during initial set up and testing. 
from app.blueprints.users.models import User
from app.blueprints.products.models import Product
from app.blueprints.products.db_init import populate_products


@app.shell_context_processor
def make_shell_context():
    return {'app': create_app, 'db': db, 'User': User, 'Product': Product, 'db_init': populate_products}
