from django.contrib import admin
from django.urls import include, path
from .views import *



urlpatterns = [
    path('', home),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:product_category_id>', catalog_filter_by_id, name='filtered_products'),
    path('details/<int:id>', card_product, name='card_product'),
    path('brands/', brands, name='brands'),
    path('basket/', basket, name='basket'),
    path('articles/', articles, name='articles'),
    path('full_article/<int:article_id>', get_full_article, name='full_article'),
    path('results/', search_products, name='search_results'),
    path('sales/', sales, name='sales'),
    # Действия с объектами в корзине
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('increase/<int:cart_item_id>', increase_quantity, name='increase_quantity'),
    path('decrease/<int:cart_item_id>', decrease_quantity, name='decrease_quantity'),
    path('remove/<int:cart_item_id>', remove_cart_product, name='remove_cart_product'),
]