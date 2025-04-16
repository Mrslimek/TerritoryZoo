# from django.contrib.auth.models import User 
# from django.contrib.auth import authenticate 
# from django.contrib import messages


# # TODO: Разобраться с тем, стоит ли использовать эту штуку, как валидатор
# # Потому что она не вызывает исключение, а дает ошибку

# def username_validator(value):
#     """
#     Валидатор логина.
#     Проверяет, что логин уникален и существует в БД.
#     """
#     if not User.objects.filter(username=value).exists():
#         messages.error(request, "Логин или пароль не действительны")
