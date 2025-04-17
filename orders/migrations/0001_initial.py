# Generated by Django 5.1.7 on 2025-04-16 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("catalog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_num", models.CharField(verbose_name="Номер заказа")),
                (
                    "order_sum",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=15,
                        null=True,
                        verbose_name="Сумма заказа",
                    ),
                ),
                (
                    "payment_type",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Наличными при получении"), (2, "Картой")],
                        null=True,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "delivery_type",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Самовывоз"), (2, "Доставка курьером")],
                        null=True,
                        verbose_name="Способ получения товара",
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Создан"),
                            (2, "Оформлен"),
                            (3, "Ожидает оплату"),
                            (4, "Оплачен"),
                            (5, "Подтвержден"),
                            (6, "Выполнен"),
                            (7, "Аннулирован"),
                            (8, "Ошибка оплаты"),
                        ],
                        verbose_name="Статус заказа",
                    ),
                ),
                ("city", models.CharField(blank=True, null=True, verbose_name="Город")),
                (
                    "street",
                    models.CharField(
                        blank=True, null=True, verbose_name="Улица/Переулок"
                    ),
                ),
                (
                    "house_num",
                    models.CharField(blank=True, null=True, verbose_name="Номер дома"),
                ),
                (
                    "entrance_num",
                    models.CharField(
                        blank=True, null=True, verbose_name="Номер подъезда"
                    ),
                ),
                (
                    "apartment_num",
                    models.CharField(
                        blank=True, null=True, verbose_name="Номер квартиры"
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True, null=True, verbose_name="Почтовый индекс"
                    ),
                ),
                (
                    "date_created",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказы",
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Кол-во продукта"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена продукта"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.order",
                        verbose_name="Номер заказа",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                        verbose_name="Название продукта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт в заказе",
                "verbose_name_plural": "Продукты в заказе",
            },
        ),
    ]
