# Generated by Django 4.1.5 on 2023-01-23 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_mailing', models.TimeField(blank=True, null=True, verbose_name='время рассылки')),
                ('change_time', models.CharField(
                    choices=[('once_day', 'раз в день'), ('once_week', 'раз в неделю'), ('once_month', 'раз в месяц')],
                    default='once_week', max_length=15, verbose_name='периодичность')),
                ('state_mail', models.CharField(
                    choices=[('completed', 'завершена'), ('created', 'создана'), ('launched', 'запущена')],
                    default='completed,', max_length=15, verbose_name='статус рассылки')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_message', models.CharField(blank=True, max_length=250, null=True, verbose_name='тема письма')),
                ('letter', models.TextField(verbose_name='тело письма')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, verbose_name='контактный email')),
                ('name', models.CharField(max_length=250, verbose_name='фио')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
                ('mailing',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.mailing',
                                   verbose_name='Рассылка')),
                ('message',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.message',
                                   verbose_name='Сообщение')),
            ],
        ),
    ]
