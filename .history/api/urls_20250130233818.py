from django.contrib import admin
from django.urls import include, path
from .views import (
    home, catalog, card_product, brands,
    basket, articles, register_user, login_user,
    reset_password, catalog_filter_by_id,
    get_products, get_products_filtered,
    logout_user, search_products,
    profile, add_to_cart,
    increase_quantity, decrease_quantity,
    remove_cart_product, get_full_article,
    sales)



urlpatterns = [
    path('api/products/', get_products),
    path('api/filtered_products/', get_products_filtered),
]