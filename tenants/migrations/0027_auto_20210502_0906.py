# Generated by Django 3.2 on 2021-05-02 09:06

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc
import re


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0026_alter_cradmin_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequest',
            name='phone',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\-\\d+)*\\Z'), code='invalid', message='valid format: 1234-5678')]),
        ),
        migrations.AlterField(
            model_name='cradmin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 17, 6, 7, 346598, tzinfo=utc)),
        ),
    ]
