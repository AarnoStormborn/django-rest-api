from django.urls import path

from . import views

urlpatterns = [

    # api/products/
    # Class Based API view
    path('', views.product_create_view),
    path('list/', views.product_list_create_view),
    path('<int:pk>/', views.product_retrieve_view),
    path('update/<int:pk>', views.product_update_view),
    path('delete/<int:pk>', views.product_destroy_view),
    path('mixinlist/', views.product_mixin_view),
    path('mixinlist/<int:pk>', views.product_mixin_view),


    # Function Based API view
    path('alt/', views.product_alt_view),
    path('alt/<int:pk>', views.product_alt_view),
    

]