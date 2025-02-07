from django.urls import path, include
from rest_framework import routers

from product import viewsets

routers = routers.SimpleRouter()
routers.register(r'product', viewsets.ProductViewSet, basename='product')  
routers.register(r'category', viewsets.CategoryViewSet, basename='category') 

urlpatterns = [
    path('', include(routers.urls)),
]
