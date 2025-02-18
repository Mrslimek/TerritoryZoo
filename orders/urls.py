from django.urls import path
from .views import *

urlpatterns = [
    path('', make_order_items, name='make_order_items'),
]