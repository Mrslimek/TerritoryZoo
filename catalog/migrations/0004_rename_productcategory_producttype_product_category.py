# Generated by Django 5.1.3 on 2025-01-02 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_producttype_productcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producttype',
            old_name='productCategory',
            new_name='product_category',
        ),
    ]
