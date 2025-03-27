from celery import shared_task
from orders.models import Order

# TODO: Это задача для celery beat, нужно будет его поставить, настроить и протестировать эту задачу
@shared_task
def clear_cart(user):
    orders = Order.objects.all()
    for order in orders:
        if order.status == 1 and order.date_created < (datetime.now() - timedelta(days=7)):
            order.delete()