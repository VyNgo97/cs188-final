import json
items = [
    {
        'itemId': '683ff143-9f8b-445a-8d8f-b9b8fe0f9f28',
        'image': 'https://i.pinimg.com/236x/35/64/dd/3564dd865f999c14ada858fd088b9dad--heather-grey-bulldog.jpg',
        'description': 'Drake Sweater',
        'price': 45.00
    },
    {
        'itemId': '783ff143-9f8b-445a-8d8f-b9b8fe0f9f30',
        'image': 'https://d3qsmzzpeeacu6.cloudfront.net/all/LXG_CER1%20MUG_CER1-BLK-DRAKE-L1B-LRG_1_800x800.jpg',
        'description': 'Drake Mug',
        'price': 20.00
    }
]


def selectItems():
    try:
        return json.dumps(items, indent=4, separators=(',',':'))
    except: 
        print('There was an error')

def selectItembyItemId(itemId):
    item = next((item for item in items if item['itemId'] == itemId),'No matches')
    return items
