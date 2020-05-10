import json
carts = [
    {
        'cart_id': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f21',
        'customer_id': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f28'
    },
    {
        'cart_id': '5581858f-a20e-4ada-9ccf-dd3e2cea0eb3',
        'customer_id': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f28'
    }
]

def selectCarts():
    try:
        return json.dumps(carts, indent=4, separators=(',',':'))
    except: 
        print('There was an error')

def selectCartByCartId(cartId):
    cart = next((cart for cart in carts if cart['cartId'] == cartId),'No matches')
    return cart

def selectCartByCustomerId(customerId):
    cart = next((cart for cart in carts if cart['customerId'] == customerId),'No matches')
    return cart

def insertCart(cart):
    carts.append(cart)

def updateCart(updatedCustomer):
    for cart in carts:
        if cart['cartId'] == updatedCustomer['cartId']:
            for keys in cart.keys():
                cart[keys] = updatedCustomer[keys]
    return carts

def deleteCartByCartId(cartId):
    cartsAfterDelete = [carts.remove(cart) for cart in carts if cart['cartId'] == cartId]
    return ''