# Generated by Django 5.0.3 on 2024-04-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0003_locate_url_masterclass_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locate',
            name='url',
        ),
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
