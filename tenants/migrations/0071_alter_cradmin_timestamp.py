# Generated by Django 3.2.2 on 2021-05-10 03:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0070_auto_20210509_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cradmin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 10, 11, 2, 11, 573273)),
        ),
    ]