# Generated by Django 4.1.4 on 2022-12-14 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0008_alter_card_date_use_alter_card_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date_use',
            field=models.CharField(default='546 days, 23:59:59.999999', max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 8, 24, 41, 461452)),
        ),
    ]
