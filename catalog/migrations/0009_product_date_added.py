# Generated by Django 5.1.3 on 2024-12-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(null=True, verbose_name='Дата добавления продукта'),
        ),
    ]
