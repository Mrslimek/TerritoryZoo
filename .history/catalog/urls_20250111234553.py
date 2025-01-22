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
    remove_cart_product,)



urlpatterns = [
    path('', home),
    path('profile/', profile, name='profile'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:product_category_id>', catalog_filter_by_id, name='filtered_products'),
    path('details/<int:id>', card_product, name='card_product'),
    path('brands/', brands, name='brands'),
    path('basket/', basket, name='basket'),
    path('articles/', articles, name='articles'),
    path('results/', search_products, name='search_results'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user),
    path('logout/', logout_user),
    path('reset_form/', reset_password),
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('increase/<int:cart_item_id>', increase_quantity, name='increase_quantity'),
    path('decrease/<int:cart_item_id>', decrease_quantity, name='decrease_quantity'),
    path('remove/<int:cart_item_id>', remove_cart_product, name='remove_cart_product'),
    path('api/products/', get_products),
    path('api/filtered_products/', get_products_filtered),
]