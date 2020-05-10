from repositories.items_repository import *
from flask import Blueprint, request
import json

item_route = Blueprint('item_route', __name__)

@item_route.route("/items", methods=['GET'])
def get_items():
    items = selectItems()
    return items

@item_route.route("/items/<itemId>", methods=['GET'])
def get_items_by_id(itemId):
    item = selectItembyItemId(itemId)
    return item

