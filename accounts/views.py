#Django
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
#Project
from .forms import *
from .models import *
from catalog.forms import SearchForm


@login_required
def profile(request):
    context = {}
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    user_profile_address = UserProfileAddress.objects.filter(profile=user_profile) or ['Пока что нет адресов']

    user_change_form = CustomUserChangeForm()
    user_profile_change_form = UserProfileChangeForm()
    user_profile_address_form = UserProfileAddressForm()

    if request.method == 'POST':
        if 'user_change' in request.POST:
            user_change_form = CustomUserChangeForm(request.POST)
            if user_change_form.is_valid():
                user_change_form.save(instance=user)
                return redirect('profile')
            else:
                context['password_message'] = user_change_form.errors

        elif 'profile_change' in request.POST:
            user_profile_change_form = UserProfileChangeForm(request.POST, instance=user_profile)
            if user_profile_change_form.is_valid():
                user_profile_change_form.save()
                return redirect('profile')

        elif 'user_profile_address_add' in request.POST:
            user_profile_address_form = UserProfileAddressForm(request.POST)
            if user_profile_address_form.is_valid():
                address = user_profile_address_form.save(instance=user_profile)
                address.profile = user_profile
                address.save()
                return redirect('profile')

    context.update({
        'user_change_form': user_change_form,
        'user_profile_change_form': user_profile_change_form,
        'user_profile_address_form': user_profile_address_form,
        'user_profile_address': user_profile_address,
        'profile': user_profile,
        'user': user,
    })

    return render(request, 'profile.html', context)


def register_user(request):

    search_form = SearchForm()
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.create(user = user)
            return redirect('login')
        if form.errors:
            form = form

    context = {
        'search_form': search_form,
        'form': form
    }

    return render(request, 'register.html', context)

def login_user(request):

    search_form = SearchForm()
    form = LoginForm()

    if request.method == 'POST':
        form_data = LoginForm(data=request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/')
        else:
            form = form_data
    
    context = {
        'form': form,
        'search_form': search_form
        }

    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')

def reset_password(request):

    search_form = SearchForm()
    form = ResetForm()
    context = {
        'form': form,
        'search_form': search_form
        }

    if request.method == 'POST':
        form_data = ResetForm(request.POST)
        if form_data.is_valid():
            email = form_data.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                message = 'На указанный адрес было отправлено письмо для восстановления пароля'
                context['message'] = message
            else:
                message = 'Пользователя с таким email не существует'
                context['message'] = message

    return render(request, 'reset_form.html', context)

def delete_user_profile_address(request, address_id):

    user_profile_address = UserProfileAddress.objects.get(id=address_id)
    user_profile_address.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))