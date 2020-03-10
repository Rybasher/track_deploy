# Generated by Django 3.0.4 on 2020-03-10 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ваше имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Ваш телефон')),
                ('model_one', models.CharField(max_length=100, verbose_name='Модель')),
                ('model_two', models.CharField(max_length=100, verbose_name='Модель')),
                ('published_date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Запрос на подбор запчастей',
                'verbose_name_plural': 'Запросы на подбор запчастей',
                'ordering': ['-published_date'],
            },
        ),
    ]
