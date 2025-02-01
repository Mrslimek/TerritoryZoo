from django.contrib import admin
from django.urls import include, path
from .views import get_products_paginated, get_products_filtered



urlpatterns = [
    path('products/', get_products),
    path('filtered_products/', get_products_filtered),
]