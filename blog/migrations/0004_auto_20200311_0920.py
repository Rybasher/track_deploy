# Generated by Django 3.0.4 on 2020-03-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200308_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(help_text='Заполните описание', null=True, verbose_name='Текст поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(help_text='Заполните описание', null=True, verbose_name='Текст поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_two_en',
            field=models.TextField(null=True, verbose_name='Второй текст поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_two_ru',
            field=models.TextField(null=True, verbose_name='Второй текст поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_two_uk',
            field=models.TextField(null=True, verbose_name='Второй текст поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_uk',
            field=models.TextField(help_text='Заполните описание', null=True, verbose_name='Текст поста'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Новость'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Новость'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Новость'),
        ),
    ]
