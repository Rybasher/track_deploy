from django.db import models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пользователя', db_index=True,
                            help_text='Введите Ваше имя')
    email = models.EmailField(max_length=100, verbose_name='Email пользователя', help_text='Введите ваш email')
    content = models.TextField(verbose_name='Сообщение пользователя', help_text="Введите сообщение")

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите сообщение')

        if not self.name:
            errors['name'] = ValidationError('Укажите ваше имя')

        if not self.email:
            errors['email'] = ValidationError('Укажите email')

        if errors:
            raise ValidationError
        errors[NON_FIELD_ERRORS] = ValidationError('Ошибка в форме')
