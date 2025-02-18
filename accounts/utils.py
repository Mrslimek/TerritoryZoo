from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth import authenticate

def username_validator(value):
    if not User.objects.filter(username=value).exists():
        raise ValidationError('Логин или пароль не действительны.')
    