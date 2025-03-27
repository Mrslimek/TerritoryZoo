import os
from celery import shared_task


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

@shared_task
def clear_cart(user):
    for cartitem in user.cartitem_set.all():
        cartitem.delete()
    return f'Корзина пользователя {user} удалена'
