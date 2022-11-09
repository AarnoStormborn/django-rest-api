from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from products.models import Product

def api_home(request, *args, **kwargs):

    body = request.body
    query = request.GET
    data = {}
    try:
        data = json.loads(body) # byte string of JSON data
    except:
        pass
    print(query)
    return JsonResponse(data)


def api_model(request, *args, **kwargs):
    
    db_data = Product.objects.all().order_by("?").first() # Get all objects and pick first
    data = {}
    if db_data:
        # Manual Serialization
        # Serialization: Model Instance => Python Dict
        
        # data['id'] = db_data.id
        # data['title'] = db_data.title
        # data['content'] = db_data.content
        # data['price'] = db_data.price

        data = model_to_dict(db_data)

    return JsonResponse(data)
