# Generated by Django 5.1.3 on 2025-02-11 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_userprofile_apartment_num_userprofile_city_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="apartment_num",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="city",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="entrance_num",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="house_num",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="postal_code",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="street",
        ),
        migrations.CreateModel(
            name="UserProfileAddress",
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
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.userprofile",
                        verbose_name="Профиль пользователя",
                    ),
                ),
            ],
        ),
    ]
