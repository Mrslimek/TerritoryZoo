from django.contrib import admin
from django.urls import include, path
from .views import (
    catalog_filter_by_id,
    get_full_article,
    search_results,
    card_product,
    articles,
    catalog,
    brands,
    sales,
    home,
)


urlpatterns = [
    path("", home),
    path("catalog/", catalog, name="catalog"),
    path(
        "catalog/<int:product_category_id>",
        catalog_filter_by_id,
        name="filtered_products",
    ),
    path("details/<int:id>", card_product, name="card_product"),
    path("brands/", brands, name="brands"),
    path("articles/", articles, name="articles"),
    path("full_article/<int:article_id>", get_full_article, name="full_article"),
    path("search/", search_results, name="search_results"),
    path("sales/", sales, name="sales"),
]
