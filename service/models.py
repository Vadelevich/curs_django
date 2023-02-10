from django.conf import settings
from django.db import models
from django.utils.datetime_safe import date

NULLUBLE = {'blank': True, 'null': True}


class Customers(models.Model):
    """ Модель для клиентов сервиса поля :
    - контактный email
    - фио
    - комментарий"""

    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                                    **NULLUBLE)
    email = models.CharField(max_length=150, verbose_name='контактный email')
    name = models.CharField(max_length=250, verbose_name='фио')
    comment = models.TextField(verbose_name='комментарий', **NULLUBLE)

    def __str__(self):
        return self.name


class Mailing(models.Model):
    """ Модель для Рассылки (настройки) поля:
    - время рассылких
    - периодичность: раз в день, раз в неделю, раз в месяц
    - статус рассылки (завершена, создана, запущена)
    """

    objects = None
    PERIOD_ONE_DAY = 'once_day'
    PERIOD_ONE_WEEK = 'once_week'
    PERIOD_ONE_MONTH = 'once_month'
    PERIODS = (
        ('once_day', 'раз в день'),
        ('once_week', 'раз в неделю'),
        ('once_month', 'раз в месяц'),
    )
    STATUSE_COMPLETED = 'completed,'
    STATUSE_CREATED = 'created'
    STATUSE_LAUNCHED = 'launched'
    STATUSE_DEACTIVATION = 'deactivated'
    STATUSES = (
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('deactivated', 'деактивирован'),
    )
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE,
                                    **NULLUBLE)
    add_customer = models.ForeignKey('service.Customers', verbose_name='Клиент', on_delete=models.SET_NULL, null=True)
    add_message = models.ForeignKey('service.Message', verbose_name='Сообщение', on_delete=models.SET_NULL, null=True)
    time_mailing = models.TimeField(verbose_name='время рассылки', **NULLUBLE)
    change_time = models.CharField(choices=PERIODS, default=PERIOD_ONE_WEEK, max_length=15,
                                   verbose_name='периодичность')
    state_mail = models.CharField(choices=STATUSES, default=STATUSE_COMPLETED, max_length=15,
                                  verbose_name='статус рассылки')
    first_date = models.DateField(default=date.today, verbose_name='начальная_дата', )
    last_date = models.DateField(default=date.today, verbose_name='конечная_дата', )

    class Meta:
        permissions = [
            ('turn_off',
             'Can turn off mailing')
        ]


class Message(models.Model):
    """ Модель для   Cообщений (настройки) поля:
    - тема письма
    - тело письма
    """

    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь', on_delete=models.CASCADE,
                                    **NULLUBLE)
    topic_message = models.CharField(max_length=250, verbose_name='тема письма', **NULLUBLE)
    letter = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.topic_message


class TryMail(models.Model):
    """ Моделька Попытка рассылки заполняется автоматически, поля:
    - дата и время последней попытки
    - статус попытки
    - ответ почтового сервера, если он был
    """

    date = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=15, verbose_name='статус попытки')
    answer = models.CharField(max_length=150, verbose_name='ответ почтового сервера', **NULLUBLE)
