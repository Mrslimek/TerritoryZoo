from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError
from django import forms
from .models import *


class RegisterForm(forms.Form):

    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"placeholder": "Ваше имя", "class": "register-form-field"}
        ),
    )

    email = forms.EmailField(
        label="Адрес электронной почты",
        widget=forms.TextInput(
            attrs={"placeholder": "Введите вашу почту", "class": "register-form-field"}
        ),
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Введите пароль", "class": "register-form-field"}
        ),
    )

    confirm_password = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Повторите пароль", "class": "register-form-field"}
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.pop("confirm_password")
        if User.objects.filter(username=username).exists():
            self.add_error("username", "Пользователь с таким username уже существует")
        if User.objects.filter(email=email).exists():
            self.add_error("email", "Пользователь с таким email уже существует")
        if password and confirm_password and password != confirm_password:
            self.add_error("password", "Пароли не совпадают")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"placeholder": "Введите ваше имя", "class": "login-form-field"}
        ),
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Введите пароль", "class": "login-form-field"}
        ),
    )


class ResetForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"placeholder": "Введите вашу почту", "class": "reset-form-field"}
        ),
    )


class CustomUserChangeForm(forms.Form):
    password = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput(
            attrs={"class": "input_field", "placeholder": "Введите пароль"}
        ),
        required=False,
    )
    confirm_password = forms.CharField(
        label="Подтвердите пароль",
        widget=forms.PasswordInput(
            attrs={"class": "input_field", "placeholder": "Подтвердите пароль"}
        ),
        required=False,
    )
    first_name = forms.CharField(
        label="Введите имя",
        widget=forms.TextInput(
            attrs={"class": "input_field", "placeholder": "Александр"}
        ),
        required=False,
    )
    last_name = forms.CharField(
        label="Введите фамилию",
        widget=forms.TextInput(attrs={"class": "input_field", "placeholder": "Пушкин"}),
        required=False,
    )
    email = forms.EmailField(
        label="Введите email",
        widget=forms.TextInput(
            attrs={"class": "input_field", "placeholder": "example@domain.com"}
        ),
        required=False,
    )

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, instance, commit=True):
        for key, value in self.cleaned_data.items():
            if key == "password":
                if value:
                    instance.set_password(value)
            else:
                if value:
                    setattr(instance, key, value)
        if commit:
            instance.save()
        return instance


class UserProfileChangeForm(forms.ModelForm):
    phone_number = forms.CharField(
        label="Номер телефона",
        widget=forms.TextInput(
            attrs={"class": "input_field", "placeholder": "+375#########"}
        ),
        required=False,
    )
    date_of_birth = forms.DateField(
        label="Дата рождения",
        widget=forms.TextInput(attrs={"class": "input_field", "type": "date"}),
        required=False,
    )

    class Meta:
        model = UserProfile
        fields = ["phone_number", "date_of_birth"]


class UserProfileAddressForm(forms.Form):
    city = forms.CharField(
        label="Город",
        widget=forms.TextInput(
            attrs={"class": "input_field", "placeholder": "г. Минск"}
        ),
    )
    street = forms.CharField(
        label="Улица/Переулок",
        widget=forms.TextInput(
            attrs={"class": "input_field", "placeholder": "Ул. Пушкина"}
        ),
    )
    house_num = forms.CharField(
        label="Номер дома",
        widget=forms.TextInput(attrs={"class": "input_field", "placeholder": "Д. 12"}),
    )
    entrance_num = forms.CharField(
        label="Номер подъезда",
        widget=forms.TextInput(attrs={"class": "input_field", "placeholder": "Под. 2"}),
    )
    apartment_num = forms.CharField(
        label="Номер квартиры",
        widget=forms.TextInput(attrs={"class": "input_field", "placeholder": "Кв. 35"}),
    )
    postal_code = forms.CharField(
        label="Почтовый индекс",
        widget=forms.TextInput(attrs={"class": "input_field", "placeholder": "220030"}),
    )

    def save(self, instance):

        profile_address = UserProfileAddress()
        for key, value in self.cleaned_data.items():
            if value:
                setattr(profile_address, key, value)

        setattr(profile_address, "profile_id", instance.id)
        profile_address.save()

        return profile_address
