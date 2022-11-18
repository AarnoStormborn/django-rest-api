from django.urls import path
from . import views

urlpatterns = [
    path('apihome', views.api_home, name='api_home'),
    path('apimodel', views.api_model, name='api_model'),
    path('restapiview', views.restapi_view, name='restapiview'),
    path('restapipost', views.restapi_post, name='restapipost')
]