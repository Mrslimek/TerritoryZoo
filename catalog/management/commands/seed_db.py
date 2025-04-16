from django.core.management.base import BaseCommand
from faker import Faker
from PIL import Image, ImageDraw
import os
from django.conf import settings
from catalog.models import (
    Brand,
    ProductCategory,
    Product,
    ProductDescription,
    Promotion,
    ProductType,
    ProductImage
)


class Command(BaseCommand):
    help = "Заполняет базу тестовыми данными"

    def handle(self, *args, **kwargs):
        fake = Faker(locale="ru_RU")  # Генерируем русские данные

        self.stdout.write("🔄 Начинаем наполнение базы тестовыми данными...")

        # 2️⃣ Создание случайных брендов
        for _ in range(5):
            brand = Brand.objects.create(
                name=fake.company(), image=f"brands/{fake.file_name(category='image')}"
            )
            self.stdout.write(f"✅ Добавлен бренд: {brand}")

        # 3️⃣ Создание категорий товаров
        for _ in range(5):
            category = ProductCategory.objects.create(
                name=fake.word(), image=f"categories/{fake.file_name(category='image')}"
            )
            self.stdout.write(f"✅ Добавлена категория: {category}")

        # 4️⃣ Создание типов продуктов
        for _ in range(5):
            product_type = ProductType.objects.create(
                name=fake.word()
            )

        # 5️⃣ Создание случайных товаров
        for _ in range(10):
            product = Product.objects.create(
                title=fake.word(),
                price=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
                amount=fake.random_int(min=1, max=100),
                unit=fake.random_element(["кг", "л", "г", "шт"]),
                brand=Brand.objects.order_by("?").first(),
                product_type=ProductType.objects.order_by("?").first(),
                date_added=fake.date_time_this_year(),
                popularity=fake.random_int(min=0, max=100),
            )
            self.stdout.write(f"✅ Добавлен продукт: {product}")

            # 6️⃣ Генерация изображений с Pillow
            image_folder = os.path.join(settings.MEDIA_ROOT, "products")
            os.makedirs(image_folder, exist_ok=True)  # Создаем папку, если ее нет

            for _ in range(fake.random_int(min=1, max=3)):  # Каждому продукту 1-3 изображения
                image_path = os.path.join(image_folder, f"{product.id}_{fake.uuid4()}.png")
                self.generate_image(image_path)  # Создаем изображение

                image = ProductImage.objects.create(
                    product=product,
                    image=f"products/{os.path.basename(image_path)}"
                )
                self.stdout.write(f"🖼️ Создано изображение: {image.image}")

        # 7️⃣ Описание продукта
        for product in Product.objects.all():
            desc = ProductDescription.objects.create(
                product=product,
                description=fake.text(),
                key_features=fake.text(),
                ingridients=fake.text(),
                guaranteed_analysis=fake.text(),
                food_additives=fake.text(),
            )
            self.stdout.write(f"✅ Добавлено описание: {desc}")

        # 8️⃣ Акции и скидки
        for product in Product.objects.all():
            if fake.boolean():
                promo = Promotion.objects.create(
                    product=product,
                    discount=fake.pydecimal(
                        left_digits=2, right_digits=2, positive=True
                    ),
                    start_date=fake.date_time_this_year(),
                    end_date=fake.date_time_this_year(),
                )
                self.stdout.write(f"✅ Добавлена акция: {promo}")

        self.stdout.write("🎉 Наполнение базы завершено!")

    def generate_image(self, path):
        fake = Faker(locale='ru_RU')
        """Генерирует случайное изображение с Pillow и сохраняет его"""
        img = Image.new("RGB", (200, 200), color=(fake.random_int(0, 255), fake.random_int(0, 255), fake.random_int(0, 255)))
        draw = ImageDraw.Draw(img)
        draw.text((50, 90), "Product", fill=(255, 255, 255))  # Текст на картинке
        img.save(path, "PNG")
