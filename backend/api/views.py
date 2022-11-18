from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(["GET"])
def restapi_view(request, *args, **kwargs):

    """
    Django Rest Framework View
    """

    items = Product.objects.all()
    data = {}
    
    if items:
        
        data = ProductSerializer(items, many=True).data

    return Response(data)

@api_view(["GET","POST"])
def restapi_post(request, *args, **kwargs):
    """
    Django Rest Framework View: POST request
    """

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        data = serializer.data
        return Response(data)
    
    else: return JsonResponse({"problem":"did not work"})
