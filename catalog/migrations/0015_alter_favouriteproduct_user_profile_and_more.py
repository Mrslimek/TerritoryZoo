# Generated by Django 5.1.3 on 2025-02-05 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("catalog", "0014_sale_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favouriteproduct",
            name="user_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.userprofile",
                verbose_name="Пользователь",
            ),
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
