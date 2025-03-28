# Generated by Django 5.1.3 on 2025-02-18 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0016_delete_cartitem"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Заказы"},
        ),
        migrations.RemoveField(
            model_name="order",
            name="products",
        ),
        migrations.RemoveField(
            model_name="order",
            name="receipt",
        ),
        migrations.RemoveField(
            model_name="order",
            name="show_order_to_user",
        ),
        migrations.AlterField(
            model_name="order",
            name="delivery_type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Самовывоз"), (2, "Доставка курьером")],
                null=True,
                verbose_name="Способ получения товара",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_sum",
            field=models.DecimalField(
                decimal_places=2, max_digits=15, null=True, verbose_name="Сумма заказа"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Наличными при получении"), (2, "Картой")],
                null=True,
                verbose_name="Способ оплаты",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.PositiveSmallIntegerField(
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
