from repositories.cart_items_repository import *
from flask import request, Blueprint
import json

cart_item_route = Blueprint('cart_item', __name__)

@cart_item_route.route("/cartItems", methods=['GET'])
def get_cart_items():
    cart_items = selectCartItems()
    return cart_items

@cart_item_route.route("/cartItems/<cartItemId>", methods=['GET'])
def get_cart_items_by_cart_items_id(cartItemId):
    cart_item = selectCartItemsByCartItemsId(cartItemId)
    return cart_item

@cart_item_route.route("/carts/<cartsId>/cartItems", methods=['GET'])
def get_cart_items_by_cart_id(cartId):
    cart_items = selectCartItemsByCartId(cartId)
    return cart_items

@cart_item_route.route("/cartItems", methods=['POST'])
def add_cartItem():
    cartItem = request.get_json()
    insertCartItem(cartItem)
    return cartItem

@cart_item_route.route("/cartItems/<cartItemId>", methods=['DELETE'])
def delete_cartItem(cartItemId):
    deleteCartItemByCartItemId(cartItemId)
    return 'Sucessfully delete, check by getting all customers'