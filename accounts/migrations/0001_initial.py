# Generated by Django 5.1.7 on 2025-04-16 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата рождения"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
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
                ("city", models.CharField(verbose_name="Город")),
                ("street", models.CharField(verbose_name="Улица/Переулок")),
                ("house_num", models.CharField(verbose_name="Номер дома")),
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
                ("postal_code", models.CharField(verbose_name="Почтовый индекс")),
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
