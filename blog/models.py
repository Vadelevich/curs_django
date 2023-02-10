from django.conf import settings
from django.db import models

NULLUBLE = {'blank': True, 'null': True}


class Blog(models.Model):
    """ Модель блога с полями :
    - заголовок
    - содержимое статьи
    - изображение
    - количество просмотров
    - дата публикации
    """
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLUBLE)
    title = models.CharField(max_length=150, verbose_name='заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение')
    count = models.BigIntegerField(verbose_name='количество просмотров')
    date = models.DateField(auto_created=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
