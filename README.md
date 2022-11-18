# Getting started with REST APIs/ Django REST Framework

### Setting up the Workspace
* Create Virtual Environment with specific Python Version
* Add packages to requirements.txt and install them in pipenv
* Save workspace (Optional)
* Create two directories
> **Backend**
>> This is where we create the API using DJANGO. All the backend logic will stored here
> **Client**
>> The client that will use the API. Could be another API, React/Vue Application or simple JavaScript client

## Create a basic python client

Using Requests library, perform a **GET** request to an endpoint. If..
* The endpoint points to an actual page, it returns HTML source code
* The endpoint points elsewhere, it returns a JSON object => REST API

## Working with Django endpoints

Start by creating a standard django project. Create a simple app and define urls. Define a view which returns a 'JsonResponse'.
In the basic.py client file, use the localhost:8000/{your_view_url} as endpoint
Use the params and json parameters of `requests.get()` to send data to backend. Manually Serailize this data and send it back through `JsonResponse()`. This will create an echo which shows that the requests-django api cycle is working correctly

## Integrate Django Models in the API cycle

Create a simple Django Model. Create a few objects and migrate the changes. Using the standard method, retrieve all the objects. We can't send this data directly in the JsonResponse because...
* The model instance is a QuerySet. It cannot be sent as a JSON response. 
* Therefore we need to serialize this data to convert it from a QuerySet to Python Dictionary. This is done in 2 ways:
> 1. Manual Serialization: Extract each field from queryset and store it in a dictionary
> 2. Using Serailizers library: Python module Serializers to serialize data

## Bringing Django Rest Framework into the picture

**from rest_framework.decorators import api_view**  
`api_view()`  
api_view is a decorator that can turn a standard django view into a DRF API view. It takes as parameters a list of strings, which are the acceptable requests that can be made to this view

**Note**: Add 'rest_framework' to installed apps in the Django settings

### Create an API response

Create a **serializers.py** file in the app directory. Serializer models work very similar to DB models and Model Forms.  
Import the serializer in the views and serialize the data object retrieved from database. Use `Response()` method from rest_framework to render API response on the view endpoint. 

## Generics and Class Based views

rest framework also has generic class based views, just like standard django. The most common ones used for CRUD operations are:
* `generics.RetrieveAPIView` => Read of CRUD, gives detailed view of each object
* `generics.CreateAPIView`
* `generics.ListAPIView` => List all objects of queryset
* `generics.ListCreateAPIView` => List all objects in post request
* `generics.`