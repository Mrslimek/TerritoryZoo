from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .pagination import CustomPagination


@api_view(["GET"])
def get_products_paginated(request):
    """
    Апи представление. Возвращает все продукты с пагинацией
    """
    products = Product.objects.all()
    paginator = CustomPagination()
    page_obj = paginator.paginate_queryset(products, request)

    serializer = FilterProductSerializer(page_obj, many=True)
    response_data = {
        "results": serializer.data,
        "user_authenticated": request.user.is_authenticated,
    }

    return paginator.get_paginated_response(response_data)


@api_view(["GET", "POST"])
def get_products_filtered(request):
    """
    Апи представление. Возвращает продукты с участием фильтрации
    и пагинацией.
    TODO: Рассмотреть возможность рефакторинга фильтрации здесь с помощью django фильтров
    """
    filters = {}
    response_data = {}
    fields = ["title__icontains", "product_category", "product_type_id", "brand_id__in"]

    for field in fields:
        value = request.data.get(field)
        if value:
            filters[field] = value

    if "promotion" in request.data:
        products = Product.objects.filter(**filters).filter(promotion__isnull=False)
        if not products:
            response_data["message"] = "По вашему запросу ничего не найдено"
            return Response(response_data)
    else:
        products = Product.objects.filter(**filters)
        if not products:
            response_data["message"] = "По вашему запросу ничего не найдено"
            return Response(response_data)

    if "is_search" in request.data:
        brands = {item.brand for item in products}
        brand_serializer = BrandSerializer(brands, many=True)
        response_data["brands"] = brand_serializer.data

    if "order_by" in request.data:
        allowed_order_fields = [
            "-price",
            "price",
            "-popularity",
            "-title",
            "title",
            "-date_added",
        ]
        if request.data["order_by"] in allowed_order_fields:
            products = products.order_by(request.data["order_by"])

    paginator = CustomPagination()
    page_obj = paginator.paginate_queryset(products, request)

    serializer = FilterProductSerializer(page_obj, many=True)

    response_data.update(
        {
            "results": serializer.data,
            "user_authenticated": request.user.is_authenticated,
        }
    )

    return paginator.get_paginated_response(response_data)
