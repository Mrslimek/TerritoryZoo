from django.contrib import admin
from .models import Product, ProductCategory, ProductProperties, Promotion, Brand, ProductImage, ProductDescription

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(ProductProperties)
admin.site.register(Promotion)
admin.site.register(Brand)
admin.site.register(ProductDescription)