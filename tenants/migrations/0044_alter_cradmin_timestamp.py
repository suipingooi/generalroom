# Generated by Django 3.2 on 2021-05-02 15:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0043_alter_cradmin_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cradmin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 23, 33, 21, 666528, tzinfo=utc)),
        ),
    ]
