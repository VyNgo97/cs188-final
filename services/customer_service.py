from repositories.customer_repository import *
# from flask import Flask

# app = Flask(__name__)

# @app.route("/", methods=['GET'])
def hello():
    return selectCustomers()

print(hello())