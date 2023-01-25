# Generated by Django 4.1.5 on 2023-01-25 05:49

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0003_mailing_first_date_mailing_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='first_date',
            field=models.DateField(default=django.utils.datetime_safe.date.today, verbose_name='начальная_дата'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='last_date',
            field=models.DateField(default=django.utils.datetime_safe.date.today, verbose_name='конечная_дата'),
        ),
    ]
