#Django
from django.shortcuts import render
#Rest framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
#Project
from .serializers import *
from .pagination import CustomPagination
from catalog.forms import SearchForm
import json

# Create your views here.

# APIView
@api_view(['GET'])
def get_products_paginated(request):

    products = Product.objects.all()
    paginator = CustomPagination()
    page_obj = paginator.paginate_queryset(products, request)

    serializer = FilterProductSerializer(page_obj, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET', 'POST'])
def get_products_filtered(request):

    filters = {}
    fields = ['product_category', 'product_type', 'brand']

    for field in fields:
        value = request.data.get(field)
        if value:
            if field == 'product_type':
                filters['product_type_id'] = value
            elif field == 'brand':
                filters['brand_id__in'] = value
            else:
                filters[field] = value
    
    if 'promotion' in request.data:
        products = Product.objects.filter(**filters).filter(promotion__isnull=False)
    else:
        products = Product.objects.filter(**filters)
    
    if 'order_by' in request.data:
        products = products.order_by(request.data['order_by'])

    paginator = CustomPagination()
    page_obj = paginator.paginate_queryset(products, request)

    serializer = FilterProductSerializer(page_obj, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def search_products(request):

    if request.method == 'POST':

        query = request.data

        if query:

            search_results = Product.objects.filter(title__icontains=query)

            if search_results:

                brands = {item.brand for item in search_results}
                brand_serializer = BrandSerializer(brands, many=True)

                paginator = CustomPagination()
                page_obj = paginator.paginate_queryset(search_results, request)
                product_serializer = FilterProductSerializer(page_obj, many=True)

                response_data = {
                    'brands': brand_serializer.data,
                    'results': product_serializer.data
                }
                return paginator.get_paginated_response(response_data)
            
            else:

                message = 'По вашему запросу ничего не найдено'
                return Response(message)
            
        return Response('Данные некорректны')