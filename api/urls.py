from django.urls import path
from .views import *



urlpatterns = [
    path('products_paginated/', get_products_paginated, name='api_get_all_products'),
    path('filtered_products/', get_products_filtered, name='api_filter_products'),
    path('search/', search_products, name='api_search'),
]