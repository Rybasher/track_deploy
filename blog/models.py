from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Новость")
    content = models.TextField(verbose_name="Текст поста", help_text="Заполните описание",
                               blank=False)
    content_two = models.TextField(verbose_name='Второй текст поста')
    image_one = models.ImageField(null=True, blank=True, verbose_name=_('Фото'), height_field="height_field",
                                  width_field="width_field", upload_to=upload_location)
    image_two = models.ImageField(null=True, blank=True, verbose_name=_("Фото2"), height_field='height_field',
                                  width_field='width_field', upload_to=upload_location)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    views = models.IntegerField('Просмотры', default=0)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата'), db_index=True)

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