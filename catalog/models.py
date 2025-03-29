from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile


class FavouriteProduct(models.Model):
    """
    Модель для Продукта, добавленного в избранное.
    Пока что не используется.
    """
    user_profile = models.ForeignKey(
        UserProfile, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "Product", verbose_name="Продукт", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user_profile}"


class Brand(models.Model):
    """
    Модель для бренда продукта
    """
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Название продукта"
    )
    image = models.FileField(verbose_name="Картинка бренда")
    product_category = models.ManyToManyField(
        "ProductCategory", verbose_name="Категория продукта"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Брэнд"
        verbose_name_plural = "Брэнды"


class ProductCategory(models.Model):
    """
    Модель для категории продукта
    """
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Категория продукта"
    )
    image = models.FileField(verbose_name="Картинка категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категория товаров"


class ProductType(models.Model):
    """
    Модель для типа продукта
    """
    name = models.CharField(max_length=255, verbose_name="Тип продукта")
    product_category = models.ManyToManyField(
        "ProductCategory", verbose_name="Категория продукта"
    )  # TODO: НАЗНАЧИТЬ КАЖДОМУ ТИПУ СВОЙ БРЕНД

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"


class Product(models.Model):
    """
    Модель для продукта
    """
    UNIT_CHOICES = [("кг", "кг"), ("л", "л"), ("г", "г"), ("шт", "шт")]
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, verbose_name="Бренд")
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    amount = models.IntegerField(verbose_name="Кол-во продукта")
    unit = models.CharField(
        max_length=255, choices=UNIT_CHOICES, verbose_name="Единица измерения"
    )
    product_type = models.ForeignKey(
        "ProductType", on_delete=models.DO_NOTHING, verbose_name="Тип продукта"
    )
    product_category = models.ManyToManyField(
        "ProductCategory", verbose_name="Категория продукта"
    )
    date_added = models.DateTimeField(
        verbose_name="Дата добавления продукта", null=True
    )
    popularity = models.IntegerField(verbose_name="Популярность продукта", default=0)

    def price_with_discount(self):
        # Этот метод был написан, когда поле discount у Promotion было указано в процентах.
        # Сейчас там итоговая скидка
        promotions = self.promotion_set.all()
        if promotions.exists():
            discount = promotions.first().discount
            final_price = round(self.price - (self.price * discount / 100), 2)
            return final_price

        return self.price

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductDescription(models.Model):
    """
    Модель для описания продукта
    """
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    description = models.TextField(null=True, verbose_name="Описание", blank=True)
    key_features = models.TextField(
        null=True, verbose_name="Ключевые особенности", blank=True
    )
    ingridients = models.TextField(null=True, verbose_name="Состав", blank=True)
    guaranteed_analysis = models.TextField(
        null=True, verbose_name="Гарантированный анализ", blank=True
    )
    food_additives = models.TextField(
        null=True, verbose_name="Пищевые добавки", blank=True
    )

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "Описание продукта"
        verbose_name_plural = "Описание продуктов"


class ProductImage(models.Model):
    """
    Модель для изображений продукта
    """
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, verbose_name="Продукт"
    )
    image = models.FileField(verbose_name="Картинка продукта")

    def __str__(self):
        return f"{self.product} --- {self.image}"

    class Meta:
        verbose_name = "Картинка продукта"
        verbose_name_plural = "Картинки продуктов"


class ProductProperties(models.Model):
    """
    Модель для характеристик продукта.
    Например, вариант фасовки и его цена
    """
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, verbose_name="Продукт"
    )
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Вес")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена", default=0.00
    )

    def __str__(self):
        return f"{self.product} --- {self.weight} --- {self.price}"

    class Meta:
        verbose_name = "Расфасовка продукта"
        verbose_name_plural = "Расфасовка продуктов"


class Promotion(models.Model):
    """
    Модель для акций.
    TODO: Нужно объединить товары на акции под конкретные акции, типа "Черная пятница"
    """
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, verbose_name="Продукт"
    )
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Цена со скидкой"
    )
    start_date = models.DateTimeField(verbose_name="Дата начала акции")
    end_date = models.DateTimeField(verbose_name="Дата окончания акции")

    class Meta:
        verbose_name = "Акционный товар"
        verbose_name_plural = "Акционные товары"

    def is_active(self):
        from django.utils import timezone

        return self.start_date <= timezone.now() <= self.end_date

    def __str__(self):
        return f"{self.product} --- {self.discount}"


class Article(models.Model):
    """
    Модель для статьи
    """
    title = models.CharField(max_length=255, verbose_name="Название статьи")
    article_text = models.TextField(verbose_name="Текст статьи")
    reading_time = models.IntegerField(verbose_name="Время чтения")
    date_published = models.DateField(verbose_name="Дата публикации")
    image = models.FileField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Sale(models.Model):
    """
    Модель для именованных акций на товары.
    TODO: Нужно как-то связать с моделью Promotion
    """
    title = models.CharField(max_length=255, verbose_name="Название акции")
    text = models.TextField(verbose_name="Текст акции")
    image = models.ImageField(verbose_name="Картинка акции")
    start_date = models.DateTimeField(verbose_name="Начало акции")
    end_date = models.DateTimeField(verbose_name="Конец акции")

    def __str__(self):
        return self.title
