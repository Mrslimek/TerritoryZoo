#Django
from django.db import models
from django.contrib.auth.models import User
#Project
from catalog.models import Product

class Order(models.Model):

    ORDER_STATUS_CHOICES = (
        (1, 'Оформлен'),
        (2, 'Ожидает оплату'),
        (3, 'Оплачен'),
        (4, 'Подтвержден'),
        (5, 'Выполнен'),
        (6, 'Аннулирован'),
        (7, 'Ошибка оплаты'),
    )

    DELIVERY_TYPE_CHOICES = (
        (1, 'Самовывоз'),
        (2, 'Доставка курьером'),
    )

    PAYMENT_TYPE_CHOICES = (
        (1, 'Наличными при получении'),
        (2, 'Картой'),
    )

    products = models.ManyToManyField(Product, verbose_name='Продукты')
    order_num = models.CharField(verbose_name='Номер заказа')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    receipt = models.FileField(upload_to='receipts', verbose_name='Чек')
    order_sum = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Сумма заказа')
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_TYPE_CHOICES, verbose_name='Способ оплаты')
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='Статус заказа')
    show_order_to_user = models.BooleanField(verbose_name='Показывать заказ пользователю')
    delivery_type = models.PositiveSmallIntegerField(choices=DELIVERY_TYPE_CHOICES, verbose_name='Способ получения товара')
    city = models.CharField(verbose_name='Город', blank=True, null=True)
    street = models.CharField(verbose_name='Улица/Переулок', blank=True, null=True)
    house_num = models.CharField(verbose_name='Номер дома', blank=True, null=True)
    entrance_num = models.CharField(verbose_name='Номер подъезда', blank=True, null=True)
    apartment_num = models.CharField(verbose_name='Номер квартиры', blank=True, null=True)
    postal_code = models.CharField(verbose_name='Почтовый индекс', blank=True, null=True)
