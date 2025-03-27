from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Order(models.Model):

    ORDER_STATUS_CHOICES = (
        (1, "Создан"),
        (2, "Оформлен"),
        (3, "Ожидает оплату"),
        (4, "Оплачен"),
        (5, "Подтвержден"),
        (6, "Выполнен"),
        (7, "Аннулирован"),
        (8, "Ошибка оплаты"),
    )

    DELIVERY_TYPE_CHOICES = (
        (1, "Самовывоз"),
        (2, "Доставка курьером"),
    )

    PAYMENT_TYPE_CHOICES = (
        (1, "Наличными при получении"),
        (2, "Картой"),
    )

    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name="Пользователь"
    )
    order_num = models.CharField(verbose_name="Номер заказа")
    order_sum = models.DecimalField(
        null=True, max_digits=15, decimal_places=2, verbose_name="Сумма заказа"
    )
    payment_type = models.PositiveSmallIntegerField(
        null=True, choices=PAYMENT_TYPE_CHOICES, verbose_name="Способ оплаты"
    )
    delivery_type = models.PositiveSmallIntegerField(
        null=True, choices=DELIVERY_TYPE_CHOICES, verbose_name="Способ получения товара"
    )
    status = models.PositiveSmallIntegerField(
        choices=ORDER_STATUS_CHOICES, verbose_name="Статус заказа"
    )
    city = models.CharField(
        blank=True, null=True, verbose_name="Город"
        )
    street = models.CharField(
        blank=True, null=True, verbose_name="Улица/Переулок"
        )
    house_num = models.CharField(
        blank=True, null=True, verbose_name="Номер дома"
    )
    entrance_num = models.CharField(
        blank=True, null=True, verbose_name="Номер подъезда"
    )
    apartment_num = models.CharField(
        blank=True, null=True, verbose_name="Номер квартиры"
    )
    postal_code = models.CharField(
        blank=True, null=True, verbose_name="Почтовый индекс"
    )
    date_created = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заказ"
        verbose_name = "Заказы"

    def __str__(self):
        return self.order_num


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name="Номер заказа"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Название продукта"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кол-во продукта")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена продукта"
    )

    class Meta:
        verbose_name = "Продукт в заказе"
        verbose_name_plural = "Продукты в заказе"

    def __str__(self):
        return self.quantity
