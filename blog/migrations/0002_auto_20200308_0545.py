# Generated by Django 3.0.4 on 2020-03-08 03:45

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_two',
            field=models.CharField(default='', max_length=50, verbose_name='Новость 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='image_one',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=blog.models.upload_location, verbose_name='Фото', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='post',
            name='image_two',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=blog.models.upload_location, verbose_name='Фото2', width_field='width_field'),
        ),
        migrations.AddField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
