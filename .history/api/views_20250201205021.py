#Django
from django.shortcuts import render
#Rest framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
#Project
from .serializers import *

# Create your views here.

# APIView
@api_view(['GET'])
def get_products_paginated(request):

    products = Product.objects.all()
    paginator = PageNumberPagination()
    page_obj = paginator.paginate_queryset(products, request)

    serializer = FilterProductSerializer(page_obj, many=True)
    return paginator.get_paginated_response


@api_view(['GET', 'POST'])
def get_products_filtered(request):

    filters = {}
    fields = ['product_category', 'product_type', 'promotion', 'brand']

    for field in fields:
        value = request.data.get(field)
        if value:
            if field == 'product_type':
                filters['product_type_id'] = value
            elif field == 'brand':
                filters['brand_id__in'] = value
            else:
                filters[field] = value
    
    if 'promotion' in filters:
        products = Product.objects.filter(**filters).filter(promotion__isnull=False)
    else:
        products = Product.objects.filter(**filters)
    
    if 'order_by' in request.data:
        products = products.order_by(request.data['order_by'])

    paginator = PageNumberPagination()
    page_obj = paginator.paginate_queryset(products, request)
    print(page_obj)

    serializer = FilterProductSerializer(page_obj, many=True)

    return paginator.get_paginated_response(serializer.data)
