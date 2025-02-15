#Django
from django.shortcuts import render
from django.http import HttpResponseRedirect
#Project
from catalog.models import Product, Article
from catalog.forms import SearchForm
from .models import CartItem


def basket(request):

    search_form = SearchForm()

    products = Product.objects.all()
    products_by_popularity = products.order_by('-popularity')
    products_by_date = products.order_by('-date_added')
    articles = Article.objects.all()
    
    user = request.user
    cart_items_count = 0
    cart_products = None

    if user.is_authenticated:
        cart_products = CartItem.objects.filter(user=request.user)
        cart_items_count = cart_products.count()
    

    context = {
        'search_form': search_form,
        'products_by_popularity': products_by_popularity,
        'products_by_date': products_by_date,
        'cart_products': cart_products,
        'articles': articles,
        'cart_items_count': cart_items_count
    }

    return render(request, 'basket.html', context)


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product, defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    # Перенаправление на ту же страницу 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def increase_quantity(request, cart_item_id):

    product = CartItem.objects.get(id=cart_item_id)
    product.quantity += 1
    product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) 


def decrease_quantity(request, cart_item_id):

    product = CartItem.objects.get(id=cart_item_id)
    product.quantity -= 1
    product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def remove_cart_product(request, cart_item_id):

    product = CartItem.objects.get(id=cart_item_id)
    product.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

