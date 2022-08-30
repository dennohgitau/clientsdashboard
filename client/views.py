import json
from this import d
from django.shortcuts import render
import requests
from itertools import groupby

# Create your views here.
url = "https://app.mftfulfillmentcentre.com/api/orders"

payload={'email': 'info@2wtrade.com',
'password': 'S5E6mBRp'}
files=[

]
headers = {
'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiM2M0YjNmNzZmZDNhYmQ0OTZlZjNkOGU1ZTUwYzNhNzI0ZTNjYTE2OTQwOWZhNTQ2MTNiMGNlMDg3OWU5NDQwZmI3Y2E3OGQ1N2YwYzU0NzQiLCJpYXQiOjE2NTk0MjcyMzcuNDcyMTY3LCJuYmYiOjE2NTk0MjcyMzcuNDcyMTY4LCJleHAiOjE2OTA5NjMyMzcuNDcwMzE4LCJzdWIiOiIyIiwic2NvcGVzIjpbXX0.aUEzDXmSoTlyWCnJvU_mH9yqrb3lxcvUqtZv3SOYuZ15vkIA6DDZ3AXkWh-Icv1UxSuVgnHlcPGb8IDEWyxFJjthJCe2Abywlawuv8DuCx_iU2FZk0bJ_4EvjrVnKa52CfwCWVRvEXSPMm7JRlXwUXTuI2O29m_pG-lP8E6j91ddTXSLn_BTdO_8N11jknjfXfCq2QVCvHPmA4g_pvZPNzEJ3M4oS_tYL_xn5_C6CmuYFLSKQHM-JT8BFvCWIIckek4JZ9DS76TLn9og6PQBAJfRYOCuY95jA85IwJTO1SqfLrvm06NUL1pz4xFIHw-1dllWqWMEcWJvIrGnWcUywQzZK0IjsOVt7CALbthtzgC9CqbCnMsZIv13VCF0fLBr33cJ8TjUmoKCfvHveCMMcIpF-37mRi69SeUntZcbfM7iSaUkz1aSL6wPjXX6zpi5L1KAwUpTydYzDzLAum4CFEwbTjA-3vhShqlXPD1TQoblQ9lUNpeSffAV3wO-ddESRu7vt45AvCuWNezRjiOGO8SQPWZpjHssDFlMKhnTH1WTZy_caIB1spk7X8VvMZl6QTwzBy4PdUIDWXAGc5waioXm7Ff2QtGJ5pZuVOmuCO3c1UdFeOmeXNHKitbdcrvDBMViMvy4ybRImtPwI3UMK70vWp3lxEB10BbyqLZML0w',
'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)
response = response.json()
data =  response.get('data')
data1 = data[0]


def home(request):
    index = 0
    context_arr_scheduled = []
    context_arr_dispatched = []
    context_arr_delivered = []
    context_arr_returned = []
    scheduled = 'Scheduled'
    dispatched = 'Inprogress'
    delivered = 'Delivered'
    returned = 'Returned'

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
        total_index = index
        scheduled_index = 0
        delivered_index = 0
        returned_index = 0
        dispatched_index = 0
        for i in context1:
            if context1[i] == scheduled:
                context_arr_scheduled.append(context1)
            elif context1[i] == delivered:
                context_arr_delivered.append(context1)
            elif context1[i] == dispatched:
                context_arr_dispatched.append(context1)
            elif context1[i] == returned:
                context_arr_returned.append(context1)


            scheduled_index = len(context_arr_scheduled)
            delivered_index = len(context_arr_delivered)
            dispatched_index = len(context_arr_dispatched)
            returned_index = len(context_arr_returned)
            context = {
                'scheduled': scheduled_index,
                'delivered': delivered_index,
                'returned': returned_index,
                'dispatched': dispatched_index,
                'total': total_index,
                }   


    return render(request, 'index.html', context)
    

def returns(request):
    index = 0
    context_arr = []
    scheduled = 'Scheduled'
    

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
        for i in context1:
            if context1[i] == scheduled:
                # context_arr.clear()
                context_arr.append(context1)
                context = {
                    'data': context_arr,
                } 
                
        
                # print(len(context_arr))

    return render(request, 'returns.html', context)
   


def cash(request):
    index = 0
    for items in data:  
        price = items.get('total_price')
        price = float(price)
        context1 = {
            'price': price
        }
        
        index +=1
        
        context_arr = []
        context_arr.append(context1)
        price_dict = context_arr[0]
        total_cash = sum(price_dict.values())
        # total = total_cash + total_cash
        cash_arr = []
        cash_arr.append(total_cash)
        total = 0
        for ele in range(0, len(cash_arr)):
            total = total + cash_arr[ele]
        context = {
            'total': total
        }
    
    return render(request, 'cash.html', context)
    
def orders(request):
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

    return render(request, 'insights.html')
 



