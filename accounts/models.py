from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    phone_number = models.CharField(
        verbose_name="Номер телефона", max_length=15, null=True, blank=True
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", null=True, blank=True
    )

    def __str__(self):
        return self.phone_number


class UserProfileAddress(models.Model):
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, verbose_name="Профиль пользователя"
    )
    city = models.CharField(
        verbose_name="Город",
    )
    street = models.CharField(verbose_name="Улица/Переулок")
    house_num = models.CharField(verbose_name="Номер дома")
    entrance_num = models.CharField(
        blank=True, null=True, verbose_name="Номер подъезда"
    )
    apartment_num = models.CharField(
        blank=True, null=True, verbose_name="Номер квартиры"
    )
    postal_code = models.CharField(verbose_name="Почтовый индекс")

    def __str__(self):
        return f"{self.city}, {self.street}, {self.house_num}, {self.entrance_num}, {self.apartment_num}, {self.postal_code}"
