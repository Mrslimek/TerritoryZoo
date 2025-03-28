# Generated by Django 5.1.3 on 2025-02-12 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_userprofile_apartment_num_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofileaddress",
            name="city",
            field=models.CharField(verbose_name="Город"),
        ),
        migrations.AlterField(
            model_name="userprofileaddress",
            name="house_num",
            field=models.CharField(verbose_name="Номер дома"),
        ),
        migrations.AlterField(
            model_name="userprofileaddress",
            name="postal_code",
            field=models.CharField(verbose_name="Почтовый индекс"),
        ),
        migrations.AlterField(
            model_name="userprofileaddress",
            name="street",
            field=models.CharField(verbose_name="Улица/Переулок"),
        ),
    ]
