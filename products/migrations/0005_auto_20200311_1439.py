# Generated by Django 3.0.4 on 2020-03-11 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200311_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_uk',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title_uk',
        ),
    ]
