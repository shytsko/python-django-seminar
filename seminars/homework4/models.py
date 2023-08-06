from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    count = models.PositiveIntegerField(default=0, verbose_name='Количество')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')

    def __str__(self):
        return f"Product({self.pk}: {self.name})"
