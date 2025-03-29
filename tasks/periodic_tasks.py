import os
from celery import shared_task
from orders.models import Order

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


@shared_task
def delete_abandoned_orders():
    """
    Задача для celery для удаления заброшенных заказов.
    Заброшенный заказ - объект Order со статусом 1
    и временем создания > 7 дней
    """
    orders = Order.objects.all()
    for order in orders:
        if order.status == 1 and order.date_created < (
            datetime.now() - timedelta(days=7)
        ):
            order.delete()
        return "Заброшенные заказы были удалены"
    return "Произошла непредвиденая ошибка"
