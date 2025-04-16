from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from .forms import OrderForm
from .models import Product, OrderItem, User
from .utils import create_order
from tasks.tasks import clear_cart


@login_required
def make_order_items(request):
    """
    Страница создания заказа с использованием формы заказа
    """
    context = {}
    order_form = OrderForm()
    user = request.user

    # cart_items = list(user.cartitem_set.all())
    # if not cart_items:
    #     return HttpResponse('Ошибка, корзина пустая. Это заглушка')

    # with transaction.atomic():
    #     new_order = create_order(user=user)
        
    #     # Создаем элементы заказа на основе элементов из корзины
    #     order_item_list = [
    #         OrderItem.objects.create(
    #             order=new_order,
    #             product=item.product,
    #             quantity=item.quantity,
    #             # TODO: обратить внимание на эту функцию
    #             price=item.cart_item_price(),
    #         ) for item in cart_items
    #     ]
        
    #     # Пересчитываем итоговую сумму заказа
    #     new_order.order_sum = sum(item.price for item in order_item_list)
    #     new_order.save()
        
    #     # Планируем задачу очистки корзины после успешного коммита транзакции
    #     transaction.on_commit(lambda: clear_cart.delay(user))

    # # Обновляем контекст с данными о новом заказе и его элементах
    # context.update({
    #     "order": new_order,
    #     "order_item_list": order_item_list,
    # })


    with transaction.atomic():
        if user.cartitem_set.exists():
            new_order = create_order(user=user)
            order_item_list = []

            for item in user.cartitem_set.all():
                order_item = OrderItem.objects.create(
                    order=new_order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.cart_item_price(),
                )
                order_item_list.append(order_item)
            # Отправляем задачу на очистку корзины пользователя
            # после создания заказа и связывания товаров из корзины с заказом
            clear_cart.delay(user)

            order_sum = sum([item.price for item in order_item_list])
            new_order.order_sum = order_sum
            new_order.save()
            context.update(
                {
                    "order": new_order,
                    "order_item_list": order_item_list,
                }
            )

    if request.method == "POST":
        pass

    context.update(
        {
            "order_form": order_form,
        }
    )
    return render(request, "order.html", context)
