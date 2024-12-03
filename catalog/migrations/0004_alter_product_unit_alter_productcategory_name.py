# Generated by Django 5.1.3 on 2024-12-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_productdescription_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('Влажный корм', 'Влажный корм'), ('Сухой корм', 'Сухой корм'), ('Игрушки', 'Игрушки'), ('Переноски', 'Переноски'), ('Посуда', 'Посуда'), ('Клетки', 'Клетки')], max_length=255, verbose_name='Тип продукта'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Категория продукта'),
        ),
    ]
