# Generated by Django 3.2 on 2021-05-08 07:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0055_alter_cradmin_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cradmin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 15, 58, 5, 160605, tzinfo=utc)),
        ),
    ]
