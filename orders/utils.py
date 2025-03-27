from django.utils.crypto import get_random_string
from .models import Order


def create_order(user):
    order_num = get_random_string(length=10)

    new_order = Order.objects.create(
        user=user,
        order_num=order_num,
        status=1,  # Статус 'Создан'
    )
    return new_order
