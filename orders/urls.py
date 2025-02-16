from django.urls import path
from .views import *

urlpatterns = [
    path('', make_order, name='make_order'),
]