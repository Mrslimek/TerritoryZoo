from .models import CartItem

def calculate_final_price(user):
    products = CartItem.objects.filter(user=user)

    total_price = 0

    for item in products:
        if item.product.promotion_set.exists():
            for promotion in item.product.promotion_set.all():
                total_price += promotion.discount * item.quantity
        else:
            total_price += item.product.price * item.quantity

    return total_price