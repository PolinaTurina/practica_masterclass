from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=24, verbose_name='Категория мастер класса')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Locate(models.Model):
    title = models.CharField(max_length=24, verbose_name='Место проведения')
    class Meta:
        verbose_name = 'Место проведения'
        verbose_name_plural = 'Места проведения'

    def __str__(self):
        return self.title

class MasterClass(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория мастер класса')
    title = models.CharField(max_length=36, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Информация о мастер классе')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время проведения')
    locate = models.ForeignKey(Locate, on_delete=models.CASCADE, verbose_name='Место проведения')
    price = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Цена')
    author = models.CharField(max_length=36, verbose_name='Автор')
    photo = models.ImageField(upload_to='%Y%d%m', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Мастер класс'
        verbose_name_plural = 'Мастер классы'

    def __str__(self):
        return self.title



class Bron(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    masterclass_id = models.ForeignKey(MasterClass, on_delete=models.CASCADE, verbose_name='Мастер класс')
    count = models.PositiveSmallIntegerField(verbose_name='Количество билетов')
    status = models.IntegerField(default=0, choices=((0, 'Оформлено'), (1, 'Принято'), (2, 'Отклонено')))