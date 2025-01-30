from django.contrib import admin
from django.urls import include, path
from .views import get_products, get_products



urlpatterns = [
    path('api/products/', get_products),
    path('api/filtered_products/', get_products_filtered),
]