# Generated by Django 5.0.3 on 2024-04-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_locate_masterclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='locate',
            name='url',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='url',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
