from django.shortcuts import render
from .forms import OrderForm
from .models import Product, OrderItem, User
from .utils import create_order


def make_order_items(request):
    context = {}
    order_form = OrderForm()
    if request.user.cartitem_set.exists():
        new_order = create_order(user=request.user)
        order_item_list = []

        for item in request.user.cartitem_set.all():
            order_item = OrderItem.objects.create(
                order=new_order,
                product=item.product,
                quantity=item.quantity,
                price=item.cart_item_price(),
            )
            order_item_list.append(order_item)

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
