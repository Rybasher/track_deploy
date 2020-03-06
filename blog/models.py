from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Новость")
    content = models.TextField(verbose_name="Текст поста", help_text="Заполните описание",
                               blank=False)
    published_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата', db_index=True)

    def clean(self):
        errors = {}
        if errors:
            raise ValidationError
        if not self.content:
            errors['content'] = ValidationError('Укажите описание поста')
        if not self.title:
            errors['title'] = ValidationError('Укажите название поста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        unique_together = ('published_date', )
        ordering = ['-published_date']