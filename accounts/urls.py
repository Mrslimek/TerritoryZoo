from django.urls import path
from .views import (
    profile,
    profile_account_data,
    profile_data,
    profile_address_data,
    register_user,
    login_user,
    logout_user,
    reset_password,
    delete_user_profile_address,
)


urlpatterns = [
    path("profile/", profile, name="profile"),
    path("profile/account_data/", profile_account_data, name="account_data"),
    path("profile/profile_data/", profile_data, name="profile_data"),
    path("profile/address_data/", profile_address_data, name="address_data"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("reset_form/", reset_password, name="reset_form"),
    path(
        "delete/<int:address_id>",
        delete_user_profile_address,
        name="delete_user_profile_address",
    ),
]
