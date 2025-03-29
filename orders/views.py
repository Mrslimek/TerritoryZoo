from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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
