from repositories.cart_repository import *
from flask import Blueprint, request
import json

cart_route = Blueprint('cart_route', __name__)

@cart_route.route("/carts", methods=['GET'])
def get_carts():
    carts = selectCarts()
    return carts

@cart_route.route("/carts/<cartId>", methods=['GET'])
def get_carts_by_cartId(cartId):
    cart = selectCartByCartId(cartId)
    return cart

@cart_route.route("/carts/<customerId>", methods=['GET'])
def get_carts_by_customerId(customerId):
    cart = selectCartByCustomerId(customerId)
    return cart

@cart_route.route("/carts", methods=['POST'])
def add_cart():
    cart = request.get_json()
    insertCart(cart)
    return cart

@cart_route.route("/carts", methods=['PUT'])
def modify_cart():
    modified_cart = request.get_json()
    updateCart(modified_cart)
    return modified_cart

@cart_route.route("/carts/<cartId>", methods=['DELETE'])
def delete_cart(cartId):
    deleteCartByCartId(cartId)
    return 'Sucessfully delete, check by getting all carts'
    