from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=24, verbose_name='Категория мастер класса')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title