# Generated by Django 5.1.3 on 2025-01-12 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_cartitem_product_weight"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                    "title",
                    models.CharField(max_length=30, verbose_name="Название статьи"),
                ),
                ("article_text", models.TextField(verbose_name="Текст статьи")),
                ("reading_time", models.IntegerField(verbose_name="Время чтения")),
                ("date_published", models.DateField(verbose_name="Дата публикации")),
            ],
        ),
    ]
