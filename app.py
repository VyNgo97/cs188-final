from flask import Flask

app = Flask(__name__)

from services.cart_service import cart_route
from services.customer_service import customer_route
from services.cart_item_service import cart_item_route
from services.item_service import item_route

app.register_blueprint(cart_item_route)
app.register_blueprint(customer_route)
app.register_blueprint(item_route)
app.register_blueprint(cart_route)