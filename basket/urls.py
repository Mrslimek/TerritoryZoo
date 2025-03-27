from django.contrib import admin
from django.urls import include, path
from .views import (
    basket,
    add_to_cart,
    increase_quantity,
    decrease_quantity,
    remove_cart_product,
)


urlpatterns = [
    path("", basket, name="basket"),
    path("add_to_cart/<int:product_id>", add_to_cart, name="add_to_cart"),
    path("increase/<int:cart_item_id>", increase_quantity, name="increase_quantity"),
    path("decrease/<int:cart_item_id>", decrease_quantity, name="decrease_quantity"),
    path("remove/<int:cart_item_id>", remove_cart_product, name="remove_cart_product"),
]
