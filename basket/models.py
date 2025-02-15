from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product, ProductProperties

# Create your models here.

class CartItem(models.Model):

    '''
    Модель, описывающая товар в корзине.
    Имеет связь с пользователем.
    На шаблонах нельзя добавить товар в корзину неаутентифицированным пользователям.
    СУЩЕСТВУЕТ БЕСКОНЕЧНО, НО МОЖНО ПРИКРУТИТЬ ПЛАНИРОВЩИК ЗАДАЧ, ЧТОБЫ СМОТРЕЛ НА ДАТУ СОЗДАНИЯ И УДАЛЯЛ ЧЕРЕЗ ~МЕСЯЦ 
    '''

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    product_weight = models.ForeignKey(ProductProperties, verbose_name='Объем продукта', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.user} --- {self.product}'
    
    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
    
    def calculate_final_price(self):
        products = CartItem.objects.filter(user=self.user)

        total_price = 0

        for item in products:
            if item.product.promotion_set.exists():
                for promotion in item.product.promotion_set.all():
                    total_price += promotion.discount * item.quantity
            else:
                total_price += item.product.price * item.quantity

        return total_price