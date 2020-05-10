from repositories.customer_repository import *
from flask import request, Blueprint
import json

customer_route = Blueprint('customer', __name__)

@customer_route.route("/customers", methods=['GET'])
def get_customers():
    customers = selectCustomers()
    return customers

@customer_route.route("/customers/<customerId>", methods=['GET'])
def get_customers_by_id(customerId):
    customer = selectCustomerByCustomerId(customerId)
    return customer

@customer_route.route("/customers", methods=['POST'])
def add_customer():
    customer = request.get_json()
    insertCustomer(customer)
    return customer

@customer_route.route("/customers", methods=['PUT'])
def modify_customer():
    modified_customer = request.get_json()
    updateCustomer(modified_customer)
    return modified_customer

@customer_route.route("/customers/<customerId>", methods=['DELETE'])
def delete_customer(customerId):
    deleteCustomerByCustomerId(customerId)
    return 'Sucessfully delete, check by getting all customers'
    