# Generated by Django 5.1.3 on 2024-12-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_unit_alter_productcategory_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категория товаров'},
        ),
        migrations.AlterModelOptions(
            name='productproperties',
            options={'verbose_name': 'Расфасовка продукта', 'verbose_name_plural': 'Расфасовка продуктов'},
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('Влажный корм', 'Влажный корм'), ('Сухой корм', 'Сухой корм'), ('Игрушки', 'Игрушки'), ('Переноски', 'Переноски'), ('Посуда', 'Посуда'), ('Клетки', 'Клетки'), ('Впитывающий наполнитель', 'Впитывающий наполнитель'), ('Древесный наполнитель', 'Древесный наполнитель'), ('Комкующийся наполнитель', 'Комкующийся наполнитель')], default=('Игрушки', 'Игрушки'), max_length=255, verbose_name='Тип продукта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('кг', 'кг'), ('л', 'л'), ('г', 'г'), ('шт', 'шт')], max_length=255, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка продукта'),
        ),
        migrations.AlterField(
            model_name='productproperties',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Вес'),
        ),
    ]
