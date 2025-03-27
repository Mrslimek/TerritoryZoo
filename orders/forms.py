from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    city = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "г. Минск"}), label="Город*"
    )
    street = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Ул. Пушкина"}), label="Улица*"
    )
    house_num = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Д. 12"}), label="Номер дома*"
    )
    entrance_num = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Под. 2"}), label="Номер подъезда"
    )
    apartment_num = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Кв. 35"}), label="Номер квартиры"
    )
    postal_code = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "220030"}),
        label="Почтовый индекс*",
    )

    class Meta:
        model = Order
        exclude = [
            "products",
            "order_num",
            "user",
            "receipt",
            "order_sum",
            "status",
            "show_order_to_user",
        ]
