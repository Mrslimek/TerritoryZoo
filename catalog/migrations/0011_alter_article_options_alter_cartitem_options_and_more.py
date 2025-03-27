# Generated by Django 5.1.3 on 2025-01-12 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_article"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "Статья", "verbose_name_plural": "Статьи"},
        ),
        migrations.AlterModelOptions(
            name="cartitem",
            options={
                "verbose_name": "Товар в корзине",
                "verbose_name_plural": "Товары в корзине",
            },
        ),
        migrations.AddField(
            model_name="article",
            name="image",
            field=models.FileField(default=1, upload_to=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1, verbose_name="Количество"),
        ),
        migrations.AlterField(
            model_name="promotion",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
    ]
