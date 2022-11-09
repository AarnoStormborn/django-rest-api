from django.urls import path
from . import views

urlpatterns = [
    path('apihome', views.api_home, name='api_home'),
    path('apimodel', views.api_model, name='api_model')
]