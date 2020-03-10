from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
# Create your models here.


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + "-" + str(int(time()))


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Product(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Имя Товара')
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    image = models.ImageField(null=True, blank=True, verbose_name="фото продукта", height_field="height_field",
                              width_field="width_field", upload_to=upload_location)
    image_two = models.ImageField(null=True, blank=True, verbose_name="фото продукта2", upload_to=upload_location)
    image_three = models.ImageField(null=True, blank=True, verbose_name="фото продукта3", upload_to=upload_location)
    image_four = models.ImageField(null=True, blank=True, verbose_name="фото продукта4", upload_to=upload_location)
    image_five = models.ImageField(null=True, blank=True, verbose_name="фото продукта5", upload_to=upload_location)
    image_six = models.ImageField(null=True, blank=True, verbose_name="фото продукта6", height_field="height_field",
                                  width_field="width_field", upload_to=upload_location)
    image_seven = models.ImageField(null=True, blank=True, verbose_name="фото продукта7", upload_to=upload_location)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField(blank=True, db_index=True)
    fuel = models.CharField(max_length=50, verbose_name='Топливо', blank=True)
    rated_power = models.FloatField(verbose_name='Номинальная мощь', null=True, blank=True)
    max_power = models.FloatField(max_length=20, verbose_name='Максимальная мощь', null=True, blank=True)
    launch_sys = models.CharField(max_length=50, verbose_name='Система пуска', blank=True)
    engine = models.CharField(max_length=50, verbose_name='Тип двигателя', blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Вес',null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    manufacturer = models.ForeignKey('Manufacturer', related_name='products', on_delete=models.CASCADE)
    stok = models.PositiveIntegerField(verbose_name='На складе')
    available = models.BooleanField(default=True, verbose_name="Доступен")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано", null=True)

    def get_absolute_url(self):
        return "/product/%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['title', '-published_date']


class Manufacturer(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    category = models.ForeignKey('Category', related_name='manufactures', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "/manufacturer/%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.category) + ": " + self.title

    class Meta:
        verbose_name_plural = 'Произовдители'
        verbose_name = 'Производитель'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return "/category/%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['title']


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Обьявление', related_name='comments')
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить на экран?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['-created_at']

