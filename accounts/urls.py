from django.urls import path
from .views import *


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('reset_form/', reset_password, name='reset_form'),
    path('delete/<int:address_id>', delete_user_profile_address, name='delete_user_profile_address'),
]