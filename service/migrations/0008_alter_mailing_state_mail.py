# Generated by Django 4.1.5 on 2023-02-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('service', '0007_alter_mailing_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='state_mail',
            field=models.CharField(
                choices=[('completed', 'завершена'), ('created', 'создана'), ('launched', 'запущена'),
                         ('deactivated', 'деактивирован')], default='completed,', max_length=15,
                verbose_name='статус рассылки'),
        ),
    ]
