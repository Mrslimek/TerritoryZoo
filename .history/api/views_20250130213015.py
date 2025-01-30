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

    product_category = request.data.get('product_category')
    product_type = request.data.get('product_type')
    promotion = request.data.get('promotion')
    brand = request.data.get('brand')
    order_by = request.data.get('order_by')

    if product_category:
        filters['product_category'] = product_category

    if product_type:
        filters['product_type_id'] = product_type
        
    if brand:
        filters['brand_id__in'] = brand

    if promotion:
        products = Product.objects.filter(**filters).filter(promotion__isnull=False)
    else:
        products = Product.objects.filter(**filters)

    if order_by:
        products = products.order_by(order_by)

    paginator = PageNumberPagination()
    page_obj = paginator.paginate_queryset(products, request)

    serializer = FilterProductSerializer(page_obj, many=True)

    response_data = {
        "products": serializer.data,
        "has_previous": page_obj.has_previous(),
        "has_next": page_obj.has_next(),
        "previous_page_number": page_obj.previous_page_number() if page_obj.has_previous() else None,
        "next_page_number": page_obj.next_page_number() if page_obj.has_next() else None,
        "total_pages": paginator.num_pages,
        "current_page": page_number,
    }

    return Response(response_data)
