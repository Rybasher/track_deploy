from django.db import models

# Create your models here.


class Spare(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ваше имя')
    phone = models.CharField(max_length=50, verbose_name='Ваш телефон')
    model_one = models.CharField(max_length=100, verbose_name='Модель')
    model_two = models.CharField(max_length=100, verbose_name='Модель')
    published_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = 'Запросы на подбор запчастей'
        verbose_name = 'Запрос на подбор запчастей'
        ordering = ['-published_date']
