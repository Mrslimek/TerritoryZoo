import os
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import SearchForm
from .models import ProductCategory, ProductType, Product, Brand, Article, Sale
from basket.models import CartItem


def home(request):
    """
    Представление для домашней страницы
    """
    search_form = SearchForm()

    product_categories = ProductCategory.objects.all()
    products = Product.objects.all()
    products_by_date = products.order_by("-date_added")
    products_by_popularity = products.order_by("-popularity")
    brands = Brand.objects.all()[:12]
    articles = Article.objects.all()
    user = request.user
    cart_items_count = 0
    google_api_key = os.getenv("GOOGLE_API_KEY")

    if user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()

    context = {
        "search_form": search_form,
        "categories": product_categories,
        "products_by_date": products_by_date,
        "products_by_popularity": products_by_popularity,
        "brands": brands,
        "articles": articles,
        "cart_items_count": cart_items_count,
        "google_api_key": google_api_key,
    }

    return render(request, "Zoo.html", context)


def catalog_filter_by_id(request, product_category_id):
    """
    Представление, отдающее шаблон каталога
    с фильтрацией по ProductCategory
    """
    context = {}
    search_form = SearchForm()

    categories = ProductCategory.objects.all()
    current_category = categories.get(id=product_category_id)
    products_by_popularity = Product.objects.all().order_by("-popularity")
    choices = ProductType.objects.all()
    brands = Brand.objects.filter(product_category=product_category_id)
    articles = Article.objects.all()

    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()
        context["cart_items_count"] = cart_items_count

    def get_category_name():
        category = categories.get(id=product_category_id)
        return category.name

    context.update(
        {
            "search_form": search_form,
            "category_name": get_category_name,
            "current_category": current_category,
            "choices": choices,
            "brands": brands,
            "categories": categories,
            "products_by_popularity": products_by_popularity,
            "articles": articles,
        }
    )

    return render(request, "catalogZooFilteredByCategory.html", context)


def catalog(request):
    """
    Представление, отдающее шаблон каталога
    для всех товаров
    """
    search_form = SearchForm()

    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    prods_by_popularity = products.order_by("-popularity")
    brands = Brand.objects.all()
    articles = Article.objects.all()
    user = request.user
    cart_items_count = 0

    if user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()

    paginator = Paginator(products, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "search_form": search_form,
        "products": products,
        "prods_by_popularity": prods_by_popularity,
        "brands": brands,
        "categories": categories,
        "page_obj": page_obj,
        "articles": articles,
        "cart_items_count": cart_items_count,
    }

    return render(request, "catalogZoo.html", context)


def card_product(request, id):
    """
    Представление, отдающее шаблон карточки товара
    """
    products = Product.objects.all()
    product = products.get(id=id)

    search_form = SearchForm()

    products_by_popularity = products.order_by("-popularity")
    products_by_category = products.filter(
        product_category=product.product_category.all().first()
    )
    articles = Article.objects.all()
    user = request.user
    cart_items_count = 0

    if user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()

    context = {
        "search_form": search_form,
        "product": product,
        "products_by_popularity": products_by_popularity,
        "products_by_category": products_by_category,
        "cart_items_count": cart_items_count,
        "articles": articles,
    }

    return render(request, "cardProduct.html", context)


def brands(request):
    """
    Представление, отдающее шаблон страницы
    со списком брендов
    """
    search_form = SearchForm()

    brands = Brand.objects.all()
    user = request.user
    cart_items_count = 0

    if user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()

    context = {
        "search_form": search_form,
        "brands": brands,
        "cart_items_count": cart_items_count,
    }

    return render(request, "brands.html", context)

    products = Product.objects.filter(brand=brand_id)
    paginator = Paginator(products, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj}

    return render(request, "catalogZoo.html", context)


def search_results(request):
    """
    Представление, отдающее шаблон каталога с результатами поиска
    """
    search_form = SearchForm()

    context = {}

    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    prods_by_popularity = products.order_by("-popularity")
    articles = Article.objects.all()

    context.update(
        {
            "search_form": search_form,
            "categories": categories,
            "products": products,
            "prods_by_popularity": prods_by_popularity,
            "articles": articles,
        }
    )

    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()
        context["cart_items_count"] = cart_items_count

    return render(request, "search.html", context)


def articles(request):
    """
    Представлние, отдающее шаблон страницы с со статьями
    """
    search_form = SearchForm()

    yandex_api_key = os.getenv("YANDEX_API_KEY")
    products_by_popularity = Product.objects.all().order_by("-popularity")
    articles = Article.objects.all()
    categories = ProductCategory.objects.all()
    user = request.user
    cart_items_count = 0

    if user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=user).count()

    context = {
        "search_form": search_form,
        "cart_items_count": cart_items_count,
        "products_by_popularity": products_by_popularity,
        "articles": articles,
        "yandex_api_key": yandex_api_key,
    }

    return render(request, "articles.html", context)


def sales(request):
    """
    Представление, отдающее шаблон страницы с акциями
    """
    search_form = SearchForm()

    yandex_api_key = os.getenv("YANDEX_API_KEY")
    sales = Sale.objects.all()
    products_by_popularity = Product.objects.all().order_by("-popularity")
    user = request.user
    cart_items_count = 0

    if user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=user).count()

    context = {
        "search_form": search_form,
        "sales": sales,
        "cart_items_count": cart_items_count,
        "products_by_popularity": products_by_popularity,
        "yandex_api_key": yandex_api_key,
    }

    return render(request, "sales.html", context)


def get_full_article(request, article_id):
    """
    Представление, отдающее шаблон полной статьи
    """
    form = SearchForm()

    article = Article.objects.get(id=article_id)
    user = request.user
    cart_items_count = 0

    if user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=user).count()

    context = {
        "search_form": form,
        "article": article,
        "cart_items_count": cart_items_count,
    }

    return render(request, "full_article.html", context)
