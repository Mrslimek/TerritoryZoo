from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import *
from .models import *
from .services import (
    authenticate_and_login_user,
    create_user_and_user_profile,
    form_errors_to_messages,
)
from catalog.forms import SearchForm


@login_required
def profile(request):
    """
    Представление для перенаправления на разные формы
    для управления личным кабинетом пользователя
    """
    return render(request, "profile_menu.html")


@login_required
def profile_account_data(request):
    """
    Представление, отдает форму для изменения данных User
    """
    user = request.user
    form = CustomUserChangeForm(request.POST or None)
    context = {"form": form, "user": user}

    if request.method == "POST" and form.is_valid():
        form.save(instance=user)
        return render(request, "account_data.html", context)
    else:
        errors = form.errors
        form_errors_to_messages(request, errors)

    return render(request, "account_data.html", context)


@login_required
def profile_data(request):
    """
    Представление, возвращает форму для управления данными
    UserProfile
    """
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    form = UserProfileChangeForm(request.POST or None)
    context = {"form": form, "user_profile": user_profile}

    if request.method == "POST" and form.is_valid():
        form.save()
        return render(request, "profile_data.html", context)
    else:
        errors = form.errors
        form_errors_to_messages(request, errors)

    return render(request, "profile_data.html", context)


@login_required
def profile_address_data(request):
    """
    Представление, возвращает форму для управлеемя данными
    модели UserProfileAddress
    """
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    user_profile_address = UserProfileAddress.objects.filter(profile=user_profile) or [
        "Пока что нет адресов"
    ]
    form = UserProfileAddressForm(request.POST or None)

    context = {
        "form": form,
        "user_profile_address": user_profile_address,
        "profile": user_profile,
        "user": user,
    }

    if request.method == "POST" and form.is_valid():
        form.save(instance=user_profile)
        return render(request, "address_data.html", context)
    else:
        errors = form.errors
        form_errors_to_messages(request, errors)

    return render(request, "address_data.html", context)


def register_user(request):
    """
    Представление для регистрации пользователя
    """
    search_form = SearchForm()
    form = RegisterForm(request.POST or None)
    context = {"search_form": search_form, "form": form}

    if request.method == "POST" and form.is_valid():
        user_data = form.cleaned_data
        create_user_and_user_profile(user_data)
        return redirect("login")
    if request.method == "POST" and not form.is_valid():
        errors = form.errors
        form_errors_to_messages(request, errors)

    return render(request, "register.html", context)


def login_user(request):
    """
    Представление для осуществления аутентификации пользователя
    """
    search_form = SearchForm()
    form = LoginForm(request.POST or None)
    context = {"form": form, "search_form": search_form}

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        if authenticate_and_login_user(request, username, password):
            return redirect("home")

    return render(request, "login.html", context)


def logout_user(request):
    """
    Выход из системы
    """
    logout(request)
    return redirect("home")


def reset_password(request):
    """
    Представление для инициирования процесса смены пароля.
    Пока что не работает, стоят заглушки
    """
    search_form = SearchForm()
    form = ResetForm(request.POST or None)
    context = {"form": form, "search_form": search_form}

    # TODO Реализовать отправку письма пользователю на почту с ссылкой для восстановления пароля

    if request.method == "POST" and form.is_valid():
        email = form_data.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            message = (
                "На указанный адрес было отправлено письмо для восстановления пароля"
            )
        else:
            message = "Пользователя с таким email не существует"
            context["message"] = message

    return render(request, "reset_form.html", context)


def delete_user_profile_address(request, address_id):
    """
    Представление для удаления адреса
    пользоваля в личном кабинете
    """
    user_profile_address = UserProfileAddress.objects.get(id=address_id)
    user_profile_address.delete()

    # TODO: Разобраться в том, что происходит в этой функции
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
