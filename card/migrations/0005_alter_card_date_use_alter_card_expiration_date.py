# Generated by Django 4.1.4 on 2022-12-14 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_alter_card_expiration_date_alter_card_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date_use',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 7, 59, 52, 875542)),
        ),
    ]