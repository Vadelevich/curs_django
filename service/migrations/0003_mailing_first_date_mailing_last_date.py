# Generated by Django 4.1.5 on 2023-01-25 05:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0002_remove_customers_mailing_remove_customers_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='first_date',
            field=models.DateField(blank=True, null=True, verbose_name='начальная_дата'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='last_date',
            field=models.DateField(blank=True, null=True, verbose_name='конечная_дата'),
        ),
    ]
