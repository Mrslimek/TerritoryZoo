from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    city = models.CharField(verbose_name='Город', blank=True, null=True)
    street = models.CharField(verbose_name='Улица/Переулок', blank=True, null=True)
    house_num = models.CharField(verbose_name='Номер дома', blank=True, null=True)
    entrance_num = models.CharField(verbose_name='Номер подъезда', blank=True, null=True)
    apartment_num = models.CharField(verbose_name='Номер квартиры', blank=True, null=True)
    postal_code = models.CharField(verbose_name='Почтовый индекс', blank=True, null=True)

    def __str__(self):
        return self.phone_number