from django.urls import path
from .views import make_order_items

urlpatterns = [
    path("", make_order_items, name="make_order_items"),
]
