# Generated by Django 5.0.3 on 2024-03-31 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='Место проведения')),
            ],
            options={
                'verbose_name': 'Место проведения',
                'verbose_name_plural': 'Места проведения',
            },
        ),
        migrations.CreateModel(
            name='MasterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Информация о мастер классе')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время проведения')),
                ('price', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Цена')),
                ('author', models.CharField(max_length=36, verbose_name='Автор')),
                ('photo', models.ImageField(upload_to='%Y%d%m', verbose_name='Картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.category', verbose_name='Категория мастер класса')),
                ('locate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.locate', verbose_name='Место проведения')),
            ],
            options={
                'verbose_name': 'Мастер класс',
                'verbose_name_plural': 'Мастер классы',
            },
        ),
    ]
