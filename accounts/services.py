from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .models import UserProfile
from django.db import transaction


def authenticate_and_login_user(request, username, password):
    """
    Аутентифицирует пользователя,
    добавляет сообщение об ошибке в ином случае
    """
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    else:
        messages.error(request, "Имя пользователя или пароль не действительны")
        return None


def create_user_and_user_profile(user_data):
    """
    Создает объект User
    и объект профиля для него - UserProfile
    """
    with transaction.atomic():
        user = User.objects.create_user(**user_data)
        user_profile = UserProfile.objects.create(user=user)
        return user, user_profile


def form_errors_to_messages(request, errors):
    """
    Создает messages на основе исключений при валидации
    """
    for field, errors in errors.items():
        for error in errors:
            messages.error(request, f"{error}")