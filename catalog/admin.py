from django.contrib import admin
from .models import (
    ProductDescription,
    ProductProperties,
    FavouriteProduct,
    ProductCategory,
    ProductImage,
    ProductType,
    Promotion,
    Product,
    Article,
    Brand,
    Sale,
)


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(ProductProperties)
admin.site.register(Promotion)
admin.site.register(Brand)
admin.site.register(ProductDescription)
admin.site.register(ProductType)
admin.site.register(FavouriteProduct)
admin.site.register(Article)
admin.site.register(Sale)
