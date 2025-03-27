# Generated by Django 5.1.3 on 2025-01-14 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0012_alter_article_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
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
                    models.CharField(max_length=255, verbose_name="Название акции"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="", verbose_name="Картинка акции"),
                ),
                ("start_date", models.DateTimeField(verbose_name="Начало акции")),
                ("end_date", models.DateTimeField(verbose_name="Конец акции")),
            ],
        ),
    ]
