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
def get_products(request):

    products = Product.objects.all()
    serializer = FilterProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_products_filtered(request):

    filters = {}
    fields = ['product_category', 'product_type', 'promotion', 'brand', 'order_by']

    for field in fields:
        value = request.data.get(field)
        if value:
            if field == 'product_type':
                filters['product_type_id']

    if promotion:
        products = Product.objects.filter(**filters).filter(promotion__isnull=False)
    else:
        products = Product.objects.filter(**filters)

    if order_by:
        products = products.order_by(order_by)

    paginator = PageNumberPagination()
    page_obj = paginator.paginate_queryset(products, request)

    serializer = FilterProductSerializer(page_obj, many=True)

    return paginator.get_paginated_response(serializer.data)
