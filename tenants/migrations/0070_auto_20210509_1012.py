# Generated by Django 3.2 on 2021-05-09 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0069_auto_20210509_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientrequest',
            name='lastflup',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cradmin',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 18, 12, 30, 906631)),
        ),
    ]
