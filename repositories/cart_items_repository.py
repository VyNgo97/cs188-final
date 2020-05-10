import json

cartItems = [
    {
        'cartId': 'd83ff143-9f8b-445a-8d8f-b9b8fe0f9f21',
        'cartItemId': '983ff143-9f8b-445a-8d8f-b9b8fe0f9f23',
        'itemId': '683ff143-9f8b-445a-8d8f-b9b8fe0f9f28',
        'quantity': 2
    }
]

def selectCartItems():
    try:
        return json.dumps(cartItems, indent=4, separators=(',',':'))
    except: 
        print('There was an error')

def selectCartItemsByCartItemsId(cartItemId):
    cart = next((cartItem for cartItem in cartItems if cartItem['cartItemId'] == cartItemId),'No matches')
    return cart

def selectCartItemsByCartId(cartId):
    cart = next((cartItem for cartItem in cartItems if cartItem['cartId'] == cartId),'No matches')
    return cart

def insertCartItem(cartItem):
    cartItems.append(cartItem)

def deleteCartItemByCartItemId(cartItemId):
    cartItemsAfterDelete = [cartItems.remove(cartItem) for cartItem in cartItems if cartItem['cartItemId'] == cartItemId]
    return ''