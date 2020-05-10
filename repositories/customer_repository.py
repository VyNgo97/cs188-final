import json
customers = [
    {
        'customerId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f28',
        'email': 'jason.bradley@drake.edu',
        'firstName': 'Jason',
        'lastName': 'Bradley'
    },
    {
        'customerId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f30',
        'email': 'vy.ngo@drake.edu',
        'firstName': 'Vy',
        'lastName': 'Ngo'
    }
]


def selectCustomers():
    try:
        return json.dumps(customers, indent=4, separators=(',',':'))
    except: 
        print('There was an error')

def selectCustomerByCustomerId(customerId):
    customer = next((customer for customer in customers if customer['customerId'] == customerId),'No matches')
    return customer

def insertCustomer(customer):
    customers.append(customer)

def updateCustomer(updatedCustomer):
    for customer in customers:
        if customer['customerId'] == updatedCustomer['customerId']:
            for keys in customer.keys():
                customer[keys] = updatedCustomer[keys]
    return customers

def deleteCustomerByCustomerId(customerId):
    customersAfterDelete = [customers.remove(customer) for customer in customers if customer['customerId'] == customerId]
    return ''
