from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth import authenticate


# TODO: Разобраться, используется ли этот файл где-то

def username_validator(value):
    """
    Валидатор логина.
    Проверяет, что логин уникален и существует в БД.
    """
    if not User.objects.filter(username=value).exists():
        raise ValidationError("Логин или пароль не действительны.")
