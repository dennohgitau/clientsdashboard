import json
from this import d
from django.shortcuts import render
import requests
from itertools import groupby

# Create your views here.
url = "https://app.mftfulfillmentcentre.com/api/orders"
url_returns = "https://app.mftfulfillmentcentre.com/api/orders_status/Returned"
url_delivered = "https://app.mftfulfillmentcentre.com/api/orders_status/Delivered"
url_cash = "https://app.mftfulfillmentcentre.com/api/cash"
url_products = "https://app.mftfulfillmentcentre.com/api/products"


payload={'email': 'info@2wtrade.com',
'password': 'S5E6mBRp'
}
files=[

]
headers = {
'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiM2M0YjNmNzZmZDNhYmQ0OTZlZjNkOGU1ZTUwYzNhNzI0ZTNjYTE2OTQwOWZhNTQ2MTNiMGNlMDg3OWU5NDQwZmI3Y2E3OGQ1N2YwYzU0NzQiLCJpYXQiOjE2NTk0MjcyMzcuNDcyMTY3LCJuYmYiOjE2NTk0MjcyMzcuNDcyMTY4LCJleHAiOjE2OTA5NjMyMzcuNDcwMzE4LCJzdWIiOiIyIiwic2NvcGVzIjpbXX0.aUEzDXmSoTlyWCnJvU_mH9yqrb3lxcvUqtZv3SOYuZ15vkIA6DDZ3AXkWh-Icv1UxSuVgnHlcPGb8IDEWyxFJjthJCe2Abywlawuv8DuCx_iU2FZk0bJ_4EvjrVnKa52CfwCWVRvEXSPMm7JRlXwUXTuI2O29m_pG-lP8E6j91ddTXSLn_BTdO_8N11jknjfXfCq2QVCvHPmA4g_pvZPNzEJ3M4oS_tYL_xn5_C6CmuYFLSKQHM-JT8BFvCWIIckek4JZ9DS76TLn9og6PQBAJfRYOCuY95jA85IwJTO1SqfLrvm06NUL1pz4xFIHw-1dllWqWMEcWJvIrGnWcUywQzZK0IjsOVt7CALbthtzgC9CqbCnMsZIv13VCF0fLBr33cJ8TjUmoKCfvHveCMMcIpF-37mRi69SeUntZcbfM7iSaUkz1aSL6wPjXX6zpi5L1KAwUpTydYzDzLAum4CFEwbTjA-3vhShqlXPD1TQoblQ9lUNpeSffAV3wO-ddESRu7vt45AvCuWNezRjiOGO8SQPWZpjHssDFlMKhnTH1WTZy_caIB1spk7X8VvMZl6QTwzBy4PdUIDWXAGc5waioXm7Ff2QtGJ5pZuVOmuCO3c1UdFeOmeXNHKitbdcrvDBMViMvy4ybRImtPwI3UMK70vWp3lxEB10BbyqLZML0w',
'Accept': 'application/json'
}




def home(request):

    index = 0
    responses = []
    urls = []
    url_returned = "https://app.mftfulfillmentcentre.com/api/orders_status/Returned?count=True"
    url_scheduled = "https://app.mftfulfillmentcentre.com/api/orders_status/Scheduled?count=True"
    url_delivered = "https://app.mftfulfillmentcentre.com/api/orders_status/Delivered?count=True"
    url_cancelled = "https://app.mftfulfillmentcentre.com/api/orders_status/Cancelled?count=True"
    url_dispatched = "https://app.mftfulfillmentcentre.com/api/orders_status/Dispatched?count=True"
    url_pending = "https://app.mftfulfillmentcentre.com/api/orders_status/Pending?count=True"

    urls.append(url_returned)
    urls.append(url_scheduled)
    urls.append(url_delivered)
    urls.append(url_cancelled)
    urls.append(url_dispatched)
    urls.append(url_pending)
    for url in urls:
        payload={'email': 'info@2wtrade.com',
        'password': 'S5E6mBRp'}
        files=[

        ]
        headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiM2M0YjNmNzZmZDNhYmQ0OTZlZjNkOGU1ZTUwYzNhNzI0ZTNjYTE2OTQwOWZhNTQ2MTNiMGNlMDg3OWU5NDQwZmI3Y2E3OGQ1N2YwYzU0NzQiLCJpYXQiOjE2NTk0MjcyMzcuNDcyMTY3LCJuYmYiOjE2NTk0MjcyMzcuNDcyMTY4LCJleHAiOjE2OTA5NjMyMzcuNDcwMzE4LCJzdWIiOiIyIiwic2NvcGVzIjpbXX0.aUEzDXmSoTlyWCnJvU_mH9yqrb3lxcvUqtZv3SOYuZ15vkIA6DDZ3AXkWh-Icv1UxSuVgnHlcPGb8IDEWyxFJjthJCe2Abywlawuv8DuCx_iU2FZk0bJ_4EvjrVnKa52CfwCWVRvEXSPMm7JRlXwUXTuI2O29m_pG-lP8E6j91ddTXSLn_BTdO_8N11jknjfXfCq2QVCvHPmA4g_pvZPNzEJ3M4oS_tYL_xn5_C6CmuYFLSKQHM-JT8BFvCWIIckek4JZ9DS76TLn9og6PQBAJfRYOCuY95jA85IwJTO1SqfLrvm06NUL1pz4xFIHw-1dllWqWMEcWJvIrGnWcUywQzZK0IjsOVt7CALbthtzgC9CqbCnMsZIv13VCF0fLBr33cJ8TjUmoKCfvHveCMMcIpF-37mRi69SeUntZcbfM7iSaUkz1aSL6wPjXX6zpi5L1KAwUpTydYzDzLAum4CFEwbTjA-3vhShqlXPD1TQoblQ9lUNpeSffAV3wO-ddESRu7vt45AvCuWNezRjiOGO8SQPWZpjHssDFlMKhnTH1WTZy_caIB1spk7X8VvMZl6QTwzBy4PdUIDWXAGc5waioXm7Ff2QtGJ5pZuVOmuCO3c1UdFeOmeXNHKitbdcrvDBMViMvy4ybRImtPwI3UMK70vWp3lxEB10BbyqLZML0w',
        'Accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        response = response.text
        responses.append(response)
        index += 1

    context = {
        'returned': responses[0],
        'scheduled': responses[1],
        'delivered': responses[2],
        'cancelled': responses[3],
        'dispatched': responses[4],
        'pending': responses[5]

    
    }
    return render(request, 'index.html', context)
    

def returns(request):
    response = requests.request("GET", url_returns, headers=headers, data=payload, files=files)
    response = response.json()
    data =  response.get('data')
    data1 = data[0]
    index = 0
    context_arr = []
    for items in data:
        client = items.get('client')
        products = data[0].get('products')
            
        created_at = client.get('created_at')
        order_no = items.get('order_no')
        name = client.get('name')
        client_phone = client.get('phone')
        client_address = client.get('address')
        product_name = products[0].get('product_name')  
        delivery_status = items.get('delivery_status')
        status = items.get('status')
        delivery_date = items.get('delivery_date')
        total_price = items.get('total_price')
        confirmed = items.get('confirmed')
        context1 = {
            'created_at' : created_at,
            'order_no': order_no,
            'name': name,
            'client_phone': client_phone,
            'client_address': client_address,
            'product_name': product_name,
            'delivery_status': delivery_status,
            'status': status,
            'delivery_date': delivery_date,
            'total_price': total_price,
            'confirmed': confirmed,
            'index': index,
        }
        index += 1
        context_arr.append(context1)
        context = {'data': context_arr}
    return render(request, 'returns.html', context)
   

def cash(request):
    #cash variables
    cash_response = requests.request("GET", url_cash, headers=headers, data=payload, files=files)
    cash_response = cash_response.json()
    cash_data =  cash_response.get('data')
    total = cash_data.get('total')
    remmited = cash_data.get('remmited')
    pending = cash_data.get('pending')

    #Delivered Variables
    delivered_response = requests.request("GET", url_delivered, headers=headers, data=payload, files=files)
    delivered_response = delivered_response.json()
    delivered_data =  delivered_response.get('data')
    index = 0
    context_arr = []
    for items in delivered_data:
        client = items.get('client')
        products = delivered_data[0].get('products')
            
        created_at = client.get('created_at')
        order_no = items.get('order_no')
        name = client.get('name')
        client_phone = client.get('phone')
        client_address = client.get('address')
        product_name = products[0].get('product_name')  
        delivery_status = items.get('delivery_status')
        status = items.get('status')
        delivery_date = items.get('delivery_date')
        total_price = items.get('total_price')
        confirmed = items.get('confirmed')
        context1 = {
            'created_at' : created_at,
            'order_no': order_no,
            'name': name,
            'client_phone': client_phone,
            'client_address': client_address,
            'product_name': product_name,
            'delivery_status': delivery_status,
            'status': status,
            'delivery_date': delivery_date,
            'total_price': total_price,
            'confirmed': confirmed,
            'index': index,
            
        }
       
        index += 1
        context_arr.append(context1)
        context2 = {'data': context_arr}
    context = {
            'total': total,
            'remmited': remmited,
            'pending': pending
        }
    context2.update(context)
        

    # print(context2)
     

    return render(request, 'cash.html', context2)
    
def orders(request):
    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    response = response.json()
    data =  response.get('data')
    data1 = data[0]
    index = 0
    context_arr = []
    for items in data:
        client = items.get('client')
        products = data[0].get('products')
            
        created_at = client.get('created_at')
        order_no = items.get('order_no')
        name = client.get('name')
        client_phone = client.get('phone')
        client_address = client.get('address')
        product_name = products[0].get('product_name')  
        delivery_status = items.get('delivery_status')
        status = items.get('status')
        delivery_date = items.get('delivery_date')
        total_price = items.get('total_price')
        confirmed = items.get('confirmed')
        context1 = {
            'created_at' : created_at,
            'order_no': order_no,
            'name': name,
            'client_phone': client_phone,
            'client_address': client_address,
            'product_name': product_name,
            'delivery_status': delivery_status,
            'status': status,
            'delivery_date': delivery_date,
            'total_price': total_price,
            'confirmed': confirmed,
            'index': index,
        }
        index += 1
        context_arr.append(context1)
        context = {'data': context_arr} 
    
    return render(request, 'orders.html', context)

def insights(request):
    index = 0
    responses = []
    urls = []
    url_returned = "https://app.mftfulfillmentcentre.com/api/orders_status/Returned?count=True"
    url_scheduled = "https://app.mftfulfillmentcentre.com/api/orders_status/Scheduled?count=True"
    url_delivered = "https://app.mftfulfillmentcentre.com/api/orders_status/Delivered?count=True"
    url_cancelled = "https://app.mftfulfillmentcentre.com/api/orders_status/Cancelled?count=True"
    url_dispatched = "https://app.mftfulfillmentcentre.com/api/orders_status/Dispatched?count=True"
    url_pending = "https://app.mftfulfillmentcentre.com/api/orders_status/Pending?count=True"

    urls.append(url_returned)
    urls.append(url_scheduled)
    urls.append(url_delivered)
    urls.append(url_cancelled)
    urls.append(url_dispatched)
    urls.append(url_pending)
    for url in urls:
        payload={'email': 'info@2wtrade.com',
        'password': 'S5E6mBRp'}
        files=[

        ]
        headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiM2M0YjNmNzZmZDNhYmQ0OTZlZjNkOGU1ZTUwYzNhNzI0ZTNjYTE2OTQwOWZhNTQ2MTNiMGNlMDg3OWU5NDQwZmI3Y2E3OGQ1N2YwYzU0NzQiLCJpYXQiOjE2NTk0MjcyMzcuNDcyMTY3LCJuYmYiOjE2NTk0MjcyMzcuNDcyMTY4LCJleHAiOjE2OTA5NjMyMzcuNDcwMzE4LCJzdWIiOiIyIiwic2NvcGVzIjpbXX0.aUEzDXmSoTlyWCnJvU_mH9yqrb3lxcvUqtZv3SOYuZ15vkIA6DDZ3AXkWh-Icv1UxSuVgnHlcPGb8IDEWyxFJjthJCe2Abywlawuv8DuCx_iU2FZk0bJ_4EvjrVnKa52CfwCWVRvEXSPMm7JRlXwUXTuI2O29m_pG-lP8E6j91ddTXSLn_BTdO_8N11jknjfXfCq2QVCvHPmA4g_pvZPNzEJ3M4oS_tYL_xn5_C6CmuYFLSKQHM-JT8BFvCWIIckek4JZ9DS76TLn9og6PQBAJfRYOCuY95jA85IwJTO1SqfLrvm06NUL1pz4xFIHw-1dllWqWMEcWJvIrGnWcUywQzZK0IjsOVt7CALbthtzgC9CqbCnMsZIv13VCF0fLBr33cJ8TjUmoKCfvHveCMMcIpF-37mRi69SeUntZcbfM7iSaUkz1aSL6wPjXX6zpi5L1KAwUpTydYzDzLAum4CFEwbTjA-3vhShqlXPD1TQoblQ9lUNpeSffAV3wO-ddESRu7vt45AvCuWNezRjiOGO8SQPWZpjHssDFlMKhnTH1WTZy_caIB1spk7X8VvMZl6QTwzBy4PdUIDWXAGc5waioXm7Ff2QtGJ5pZuVOmuCO3c1UdFeOmeXNHKitbdcrvDBMViMvy4ybRImtPwI3UMK70vWp3lxEB10BbyqLZML0w',
        'Accept': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        response = response.text
        responses.append(response)
        index += 1

    context = {
        'returned': responses[0],
        'scheduled': responses[1],
        'delivered': responses[2],
        'cancelled': responses[3],
        'dispatched': responses[4],
        'pending': responses[5]

    
    }

    return render(request, 'insights.html', context)
 
def inventory(request):
    response = requests.request("GET", url_products, headers=headers, data=payload, files=files)
    response = response.json()
    data =  response.get('data')
    data1 = data[0]
    index = 0
    context_arr = []
    
    for items in data:
        id = items.get('id')
        product_name = items.get('product_name')
        sku_no = items.get('sku_no') 
        available = items.get('available_for_sale')
        commited = items.get('commited')
        onhand = items.get('onhand')

        context1 = {
            'id': id,
            'product_name': product_name,
            'sku_no': sku_no,
            "available_for_sale": available,
            "commited": commited,
            "onhand": onhand,
        }

        index += 1
        context_arr.append(context1)
        context = {'data': context_arr}

    return render(request, 'inventory.html', context)


